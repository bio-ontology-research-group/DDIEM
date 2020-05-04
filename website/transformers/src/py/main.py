import os, shutil, configparser, subprocess, sys
import unittest, ddiem_test, test
from ddiem_test import TestDdiemRDF

from datetime import datetime
from os.path import join


DATA_DIR = "raw_data"
DATA_SOURCE_DIR = DATA_DIR + "/source"
SRC_FILE_NAME = "ddiem_clinical_logs"
SRC_FILE_EXT = ".csv"
PARSED_SRC_FILE_NAME = SRC_FILE_NAME + ".parsed"
COLLAPSED_SRC_FILE_NAME = PARSED_SRC_FILE_NAME + ".collapsed"
NORMALIZED_SRC_FILE_NAME = COLLAPSED_SRC_FILE_NAME + ".clinical_logs_for_rdf_v2"


# Reading setup properties from configuration file
config_dir = os.path.expanduser("~") + "/.config"
configFile = config_dir + "/ddiem-pipeline.ini"

if not os.path.isfile(configFile):
    os.makedirs(config_dir, exist_ok=True)
    shutil.copyfile("default-ddiem-pipeline.ini", configFile)

config = configparser.RawConfigParser()
config.read(configFile)

def handle_output(process):
    if process.wait() != 0:
        exit(0)

if __name__ == "__main__":

    latest_dir = None
    latest_dir_date = None
    for file in os.listdir(DATA_DIR):
        file_obj = None
        if not os.path.isfile(file):
            if "source" in file:
                continue

            file_date = datetime.strptime(str(file), '%Y-%m-%d')
            if not latest_dir:
                latest_dir = file
                latest_dir_date = datetime.strptime(str(latest_dir), '%Y-%m-%d')
            elif file_date > latest_dir_date:
                latest_dir = file
                latest_dir_date = file_date

    now = datetime.now()
    src_csv_dataset = join(join(DATA_DIR, latest_dir), SRC_FILE_NAME + SRC_FILE_EXT)
    count_of_workers = 1
    log_file_name = "logs/BORG_DDIEM__dataset." + now.strftime("%Y-%m-%d.%H%M") + ".csv.log"
    os.system("mkdir -p $(dirname " + log_file_name + ")")
    os.system("echo `date +%Y-%m-%d` log_file_name is:" + log_file_name)

    # Adds row and column numbers to csv
    CMD_1 = "date && time python3 src/py/clinical_logs_data_transformation/BORG_DDIEM__parse_clinical_logs_CSV.py \
    -f {src_csv_dataset} -d raw_data --count_of_workers={count_of_workers} 2>&1|tee {log_file_name} \
    && date".format(src_csv_dataset=src_csv_dataset, count_of_workers=count_of_workers, log_file_name=log_file_name)
    
    process = subprocess.Popen(CMD_1, stdout=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        print(line.strip())


    # Collapses fields to below fields whereever required
    src_csv_dataset = join(join(DATA_DIR, latest_dir), PARSED_SRC_FILE_NAME + SRC_FILE_EXT)
    CMD_2 = "date && time python3 src/py/clinical_logs_data_transformation/BORG_DDIEM__collapse_clinical_logs_CSV.py \
    -f {src_csv_dataset} -d raw_data --count_of_workers={count_of_workers} 2>&1|tee {log_file_name} \
    && date".format(src_csv_dataset=src_csv_dataset, count_of_workers=count_of_workers, log_file_name=log_file_name)
    
    process = subprocess.Popen(CMD_2, stdout=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        print(line.strip())

    # Resolves entities from their source databases and normalizes field discrete values
    src_csv_dataset_col = join(join(DATA_DIR, latest_dir), COLLAPSED_SRC_FILE_NAME + SRC_FILE_EXT)
    dest_dir_file_name = join(DATA_DIR, latest_dir)
    os.system("echo `date +%Y-%m-%d` log_file_name is:" + log_file_name)
    CMD_3="date && time python3 src/py/clinical_logs_data_transformation/BORG_DDIEM__prepare_clinical_logs_for_rdf_v2.py \
        --borg_ddiem_relational_ontology_graph_csv_file_name=\"raw_data/2019-05-19/BORG_DDIEM__relational_ontology_graph.csv\" \
        --src_clinical_log_dataset_csv_file_name={src_csv_dataset_col} \
        --OMIM_mimTitles_dataset_tsv_file_name={omim_src_file} \
        --drugbank_drug_names_dataset_tsv_file_name={drugbank_src_file} \
        --ChEBI_drug_names_dataset_tsv_file_name={chebi_src_file} \
        --iembase_mapping_csv_file_name={iembase_mapping_src_file} \
        --uniprotkb_id__2__ec_number_tsv_file_name={uniprot_to_ecnumber_src_file} \
        -d {dest_dir_file_name} \
        --count_of_workers={count_of_workers} \
        2>&1|tee {log_file_name} \
        && date \
        && echo `date +%Y-%m-%d.%H%M.%S.%N.%Z` log_file_name is:'{log_file_name}'".format(
            src_csv_dataset_col=src_csv_dataset_col,
            omim_src_file=config['source']['omim'],
            drugbank_src_file=config['source']['drugbank'],
            chebi_src_file=config['source']['chebi'],
            iembase_mapping_src_file=config['source']['iembase.mapping'],
            uniprot_to_ecnumber_src_file=config['source']['uniprot.kb_id__2__ec_number'],
            dest_dir_file_name=dest_dir_file_name,
            count_of_workers=count_of_workers,
            log_file_name=log_file_name
        ) 
    
    process = subprocess.Popen(CMD_3, stdout=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        print(line.strip())

    src_csv_dataset_norm = join(join(DATA_DIR, latest_dir), NORMALIZED_SRC_FILE_NAME + SRC_FILE_EXT)
    src_drugbank_json = join(join(DATA_DIR, latest_dir), NORMALIZED_SRC_FILE_NAME + ".drugbank_drug_names.json")
    src_chebi_json = join(join(DATA_DIR, latest_dir), NORMALIZED_SRC_FILE_NAME + ".ChEBI_drug_names.json")

    # transformers normalized source data to rdf format
    CMD_4 = "python src/py/collapsed_ddiem_csv_transformer.py \
        {src_file} {drugbank_file} {chebi_file} {whocc_file} {data_dir}".format(
            src_file=src_csv_dataset_norm,
            drugbank_file=src_drugbank_json,
            chebi_file=src_chebi_json,
            whocc_file=config['source']['whocc'],
            data_dir=config["data"]["dir"]
        )

    process = subprocess.Popen(CMD_4, text=True, shell=True)
    # for line in process.stdout:
    #     print(line.strip())
    handle_output(process)

    # Run tests over the generated 
    TestDdiemRDF.RDF_FILE = "ddiem-data." + now.strftime("%Y-%m-%d") + ".rdf"
    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    test_runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    
    suite.addTests(loader.loadTestsFromModule(ddiem_test))
    result = test_runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(0)

    sparql_query="CLEAR GRAPH '" + config["rdfstore"]["graph"] + "'"  
    CMD_5 = "time curl --user " + config["rdfstore"]["user"] + ":" + config["rdfstore"]["pwd"] + " \
        -X POST " + config["rdfstore"]["endpoint"] + "\
        -H \"Content-Type: application/x-www-form-urlencoded\" \
        -H \"Accept:application/sparql-results+json\" \
        --data-urlencode 'format=json' --data-urlencode 'default-graph-uri=" + config["rdfstore"]["graph"] + "' \
        --data-urlencode \"query=" + sparql_query + "\" \
        --write-out '%{url_effective};%{http_code};%{time_total};%{time_namelookup};%{time_connect};%{size_download};%{speed_download}\\n' \
        ;date;"

    process = subprocess.Popen(CMD_5, stdout=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        print(line.strip())

    src_rdf_file = config["data"]["dir"] + "/ddiem-data." + now.strftime("%Y-%m-%d") + ".rdf"
    print(src_rdf_file)
    curd_endpoint = config["rdfstore"]["endpoint"] + "-graph-crud-auth?graph-uri=" + config["rdfstore"]["graph"]
    CMD_6 = "time curl --digest --user " + config["rdfstore"]["user"] + ":" + config["rdfstore"]["pwd"] + " --verbose -X POST \
        --url " + curd_endpoint + " \
        --upload-file '" + src_rdf_file + "' \
        --write-out '%{url_effective};%{http_code};%{time_total};%{time_namelookup};%{time_connect};%{size_download};%{speed_download}\\n' \
        && echo `date +%Y-%m-%d.%H%M.%S.%N` Processing file '" + src_rdf_file + "' completed with exit status:$e_status at `date +%Y-%m-%d.%H%Mhrs:%S.%N`;"

    process = subprocess.Popen(CMD_6, stdout=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        print(line.strip())
