#!/bin/python3;
a="""



Incooperate drugbank drug metadata from "/local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-08-01/drugbank/drugbank_drugnames.full_database.tsv"
Incooperate ChEBI drug metadata from "/local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-08-04/ChEBI/names.tsv"
Incooperate IEMbase data from "/local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-10-17/disorderID_omimID.csv"
#https://www.whocc.no/atc_ddd_index/?code=M01AX
#Incooperate WHOCC drug names from "/local/data/development.minor/KAUST/BORG/raw_data/2019-09-01/WHOCC/BORG_DDIEM__clinical_logs.2019-09-01.1348hrs.collapsed.clinical_logs_for_rdf_part1.WHOCC_drug_names.json"
Incooperate WHOCC drug names from "/local/data/development.minor/KAUST/BORG/raw_data/2020-01-12/WHOCC/BORG_DDIEM__clinical_logs.2020-01-13.0859hrs.collapsed.clinical_logs_for_rdf_part1.WHOCC_drug_names.json"


#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-05-27/BORG_DDIEM__clinical_logs.2019-05-27.1340hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-09-01/BORG_DDIEM__clinical_logs.2019-09-01.1348hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-10-01/BORG_DDIEM__clinical_logs.2019-10-01.1418hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-10-10/BORG_DDIEM__clinical_logs.2019-10-10.0958hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-10-16/BORG_DDIEM__clinical_logs.2019-10-16.0900hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-10-27/BORG_DDIEM__clinical_logs.2019-10-27.1048hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-10-31/BORG_DDIEM__clinical_logs.2019-10-31.1014hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-11-22/BORG_DDIEM__clinical_logs.2019-11-22.0032hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-12-03/BORG_DDIEM__clinical_logs.2019-12-03.1025hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-12-03/BORG_DDIEM__clinical_logs.2019-12-03.1140hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-12-04/BORG_DDIEM__clinical_logs.2019-12-04.0804hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-12-05/BORG_DDIEM__clinical_logs.2019-12-05.0910hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2019-12-05/BORG_DDIEM__clinical_logs.2019-12-05.0959hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-12/BORG_DDIEM__clinical_logs.2020-01-12.1611hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-13/BORG_DDIEM__clinical_logs.2020-01-13.1726hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-15/BORG_DDIEM__clinical_logs.2020-01-15.1207hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.0958hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.1116hrs.collapsed.csv";
#export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.1301hrs.collapsed.csv";
export src_clinical_log_dataset_csv_file_name="../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.1646hrs.collapsed.csv";



export dest_dir_file_name="$(dirname ${src_clinical_log_dataset_csv_file_name})";

working_dir_file_name="/local/data/tmp/BORG_DDIEM/BORG_DDIEM__prepare_clinical_logs_for_rdf_part1.working_dir" \
 && count_of_workers=1 \
 && log_file_name="/local/data/tmp/BORG_DDIEM/logs/BORG_DDIEM__dataset.csv.log.`date +%Y-%m-%d.%H%M.%S.%N.%Z`" \
 && echo `date +%Y-%m-%d.%H%M.%S.%N.%Z`", log_file_name is:'${log_file_name}'" \
 && mkdir -p "$(dirname ${log_file_name})" \
 && pushd . && cd /local/data/development.minor/KAUST/BORG/try1 \
 && PYTHON_HOME="/local/data/apps/python/3.7.4" \
 && date && time "${PYTHON_HOME}"/bin/python3 src/py/clinical_logs_data_transformation/amqp/BORG_DDIEM__prepare_clinical_logs_for_rdf_part1.py \
 --borg_ddiem_relational_ontology_graph_csv_file_name="../raw_data/2019-05-19/BORG_DDIEM__relational_ontology_graph.csv" \
 --src_clinical_log_dataset_csv_file_name="${src_clinical_log_dataset_csv_file_name}" \
 --OMIM_mimTitles_dataset_tsv_file_name="../raw_data/2019-08-08/OMIM/mimTitles.txt" \
 --drugbank_drug_names_dataset_tsv_file_name="../raw_data/2019-08-01/drugbank/drugbank_drugnames.full_database.tsv" \
 --ChEBI_drug_names_dataset_tsv_file_name="../raw_data/2019-08-04/ChEBI/names.tsv" \
 --gene_info_tsv_file_name="../raw_data/2019-08-05/ncbi_gene/gene_info" \
 --iembase_mapping_csv_file_name="../raw_data/2019-10-17/disorderID_omimID.csv" \
 --gene_id__2__uniprotkb_id_tsv_file_name="../raw_data/2019-10-31/gene_id__to__uniprotkb_id.tab" \
 --uniprotkb_id__2__ko_id_tsv_file_name="../raw_data/2019-10-31/uniprotkb_id__to__ko_id.tab" \
 --uniprotkb_id__2__ec_number_tsv_file_name="../raw_data/2019-10-31/uniprotkb_id__to__ec_number.tab" \
 --PubChem_CID_csv_file_name="../raw_data/2019-12-03/PubChem_CID.csv" \
 -d"${dest_dir_file_name}" \
 --count_of_workers=${count_of_workers} \
 2>&1|tee "${log_file_name}" \
 && popd && date \
 && echo `date +%Y-%m-%d.%H%M.%S.%N.%Z`", log_file_name is:'${log_file_name}'" \
;


date;time ls -tr /local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-11-22/;date;


date;time tail -n+2 /local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-10-16/BORG_DDIEM__clinical_logs.2019-10-16.0900hrs.collapsed.gene_id__list.csv|head -n3|sed -r "s:^([^,]+),(.+)$:\2:g"|head -n3;date;
date;time tail -n+2 /local/data/development.minor/KAUST/BORG/try1/../raw_data/2019-10-16/BORG_DDIEM__clinical_logs.2019-10-16.0900hrs.collapsed.gene_id__list.csv|sed -r "s:^([^,]+),(.+)$:\2:g">/local/data/tmp/gene_id.csv;date;
TODO 2019-10-21 1502hrs

1) capture the various distinct key field values to file.
2) include the gene_id to uniprot_id file.
3) include the omim_id to IEMbase file.

""";

#from xml.sax import saxutils;
#import xml.sax;

import sys;
import os;
import getopt;
from optparse import OptionParser;
import errno;
import csv;
import re;
import time;
import json;
import logging;
import errno;
import sys, traceback;
import datetime;
import socket;
import multiprocessing;
import io;

import xml.etree.ElementTree;
import hashlib;




LOG_FORMAT=('%(levelname) -5s processes_id:%(process)d time:%(asctime)s %(name) -10s [%(pathname)s %(module)s %(funcName) '
    '-15s %(lineno) -5d]: %(message)s');
LOGGER = logging.getLogger(__name__);

def run_BORG_DDIEM__prepare_clinical_logs_for_rdf_part1(
    w
    ,queue
    ,worker_id
):
    try:
        w.run();
        queue.put(w._processing_outcome__dict);
    except KeyboardInterrupt:
        d.stop();
class BORG_DDIEM__prepare_clinical_logs_for_rdf_part1():
    def __init__(
        self
        ,hostname,ipAddress,ppid
        ,task_id
        ,task_formulation_timestamp
        ,worker_id
        ,worker_number
        ,working_dir_file_name
        ,_borg_ddiem_relational_ontology_graph_csv_file_name
        ,_src_clinical_log_dataset_csv_file_name
        ,_dest_dir_file_name
        ,_OMIM_mimTitles_dataset_tsv_file_name
        ,_drugbank_drug_names_dataset_tsv_file_name
        ,_ChEBI_drug_names_dataset_tsv_file_name
        ,_gene_info_tsv_file_name
        ,_iembase_mapping_csv_file_name
        ,_gene_id__2__uniprotkb_id_tsv_file_name
        ,_uniprotkb_id__2__ko_id_tsv_file_name
        ,_uniprotkb_id__2__ec_number_tsv_file_name
        ,_PubChem_CID_csv_file_name
    ):
        doc="""
        an object if this class performs the tranformation of XML to JSON.
        """;
        self.LOG_FORMAT=('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
            '-35s %(lineno) -5d: %(message)s');
        self.logging_level__value="INFO";
        
        self.working_dir_file_name=working_dir_file_name;
        self.hostname=hostname;
        self.ipAddress=ipAddress;
        self.ppid=os.getppid();
        self.pid=os.getpid();
        self.task_formulation_timestamp=task_formulation_timestamp;
        self.task_id=task_id;
        self.worker_id=worker_id;
        self.worker_number=worker_number;
        self._borg_ddiem_relational_ontology_graph_csv_file_name=_borg_ddiem_relational_ontology_graph_csv_file_name;
        self._src_clinical_log_dataset_csv_file_name=_src_clinical_log_dataset_csv_file_name;
        self._dest_dir_file_name=_dest_dir_file_name;
        self._OMIM_mimTitles_dataset_tsv_file_name=_OMIM_mimTitles_dataset_tsv_file_name;
        self._drugbank_drug_names_dataset_tsv_file_name=_drugbank_drug_names_dataset_tsv_file_name;
        self._ChEBI_drug_names_dataset_tsv_file_name=_ChEBI_drug_names_dataset_tsv_file_name;
        self._gene_info_tsv_file_name=_gene_info_tsv_file_name;
        self._iembase_mapping_csv_file_name=_iembase_mapping_csv_file_name;
        self._gene_id__2__uniprotkb_id_tsv_file_name=_gene_id__2__uniprotkb_id_tsv_file_name;
        self._uniprotkb_id__2__ko_id_tsv_file_name=_uniprotkb_id__2__ko_id_tsv_file_name;
        self._uniprotkb_id__2__ec_number_tsv_file_name=_uniprotkb_id__2__ec_number_tsv_file_name;
        self._PubChem_CID_csv_file_name=_PubChem_CID_csv_file_name;
        self._processing_outcome__dict=None;
        
        try:
            if(_src_clinical_log_dataset_csv_file_name==None or len(_src_clinical_log_dataset_csv_file_name.strip())<0):
                pass;
                raise ValueError("_src_clinical_log_dataset_csv_file_name is empty the supplied value is '%s'"%(_src_clinical_log_dataset_csv_file_name));
            if(_dest_dir_file_name==None or len(_dest_dir_file_name.strip())<0):
                pass;
                raise ValueError("_dest_dir_file_name is empty the supplied value is '%s'"%(_dest_dir_file_name));
            if(_OMIM_mimTitles_dataset_tsv_file_name==None or len(_OMIM_mimTitles_dataset_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_OMIM_mimTitles_dataset_tsv_file_name is empty the supplied value is '%s'"%(_OMIM_mimTitles_dataset_tsv_file_name));
            if(_drugbank_drug_names_dataset_tsv_file_name==None or len(_drugbank_drug_names_dataset_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_drugbank_drug_names_dataset_tsv_file_name is empty the supplied value is '%s'"%(_drugbank_drug_names_dataset_tsv_file_name));
            if(_ChEBI_drug_names_dataset_tsv_file_name==None or len(_ChEBI_drug_names_dataset_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_ChEBI_drug_names_dataset_tsv_file_name is empty the supplied value is '%s'"%(_ChEBI_drug_names_dataset_tsv_file_name));
            if(_gene_info_tsv_file_name==None or len(_gene_info_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_gene_info_tsv_file_name is empty the supplied value is '%s'"%(_gene_info_tsv_file_name));
            if(_iembase_mapping_csv_file_name==None or len(_iembase_mapping_csv_file_name.strip())<0):
                pass;
                raise ValueError("_iembase_mapping_csv_file_name is empty the supplied value is '%s'"%(_iembase_mapping_csv_file_name));
            if(_gene_id__2__uniprotkb_id_tsv_file_name==None or len(_gene_id__2__uniprotkb_id_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_gene_id__2__uniprotkb_id_tsv_file_name is empty the supplied value is '%s'"%(_gene_id__2__uniprotkb_id_tsv_file_name));
            if(_uniprotkb_id__2__ko_id_tsv_file_name==None or len(_uniprotkb_id__2__ko_id_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_uniprotkb_id__2__ko_id_tsv_file_name is empty the supplied value is '%s'"%(_uniprotkb_id__2__ko_id_tsv_file_name));
            if(_uniprotkb_id__2__ec_number_tsv_file_name==None or len(_uniprotkb_id__2__ec_number_tsv_file_name.strip())<0):
                pass;
                raise ValueError("_uniprotkb_id__2__ec_number_tsv_file_name is empty the supplied value is '%s'"%(_uniprotkb_id__2__ec_number_tsv_file_name));
            if(_PubChem_CID_csv_file_name==None or len(_PubChem_CID_csv_file_name.strip())<0):
                pass;
                raise ValueError("_PubChem_CID_csv_file_name is empty the supplied value is '%s'"%(_PubChem_CID_csv_file_name));
                
                
        except ValueError as error:
            #see "/local/data/BCL_FE_ABI3730_sequencer_plate_data_generator_jobs_data/2018/2018-09/2018-09-20/2018-09-20_171025_103.processing_outcome.json"
            #LOGGER.info(" '%s', -------------- cmd is:'%s', row_cnt is:%d"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cmd,row_cnt));
            LOGGER.exception(error);
            LOGGER.exception(traceback.format_exc());
            
            raise error;
    def run(self):
        self._distinct_ids__list__dict=obtain_distinct_values(
            self.hostname,self.ipAddress,self.ppid,self.pid
            ,self.working_dir_file_name
            ,self.task_id
            ,self.task_formulation_timestamp
            ,self.worker_id
            ,self.worker_number
            ,self._src_clinical_log_dataset_csv_file_name
        );
        """
            return {
                "omim_id__list":omim_id__list
                ,"gene_affected__list":gene_affected__list
                ,"gene_affected_unresolved__list":gene_affected_unresolved__list
                ,"gene_symbol__list":gene_symbol__list
                ,"uniprot_ID__list":uniprot_ID__list
                ,"ec_number__list":ec_number__list
                ,"enzyme_or_protein_detected_unresolved__list":enzyme_or_protein_detected_unresolved__list
                ,"drugbank_ID__list":drugbank_ID__list
                ,"chEBI_ID__list":chEBI_ID__list
                ,"pubChem_CID__list":pubChem_CID__list
                ,"pubChem_SID__list":pubChem_SID__list
                ,"pubChem_AID__list":pubChem_AID__list
                ,"wHOCC_ID__list":wHOCC_ID__list
            };
        """;
        LOGGER.info("self._distinct_ids__list__dict is:'%s'"%(json.dumps(self._distinct_ids__list__dict,indent=4)));
        
        self._pubChem_CID_info__dict=None;
        self._pubChem_SID_info__dict=None;
        self._pubChem_AID_info__dict=None;
        
        self._pubChem_CID_info__dict, self._pubChem_CID__list2=package_pubChem_CID_info(
            self._PubChem_CID_csv_file_name
            ,self._distinct_ids__list__dict["pubChem_CID__list"]
        );
        self._distinct_ids__list__dict["pubChem_CID__list2"]=self._pubChem_CID__list2;
        
        self._omim_id__dict, self._iembase_id__list=package_omim_id(
            self._iembase_mapping_csv_file_name
            ,self._distinct_ids__list__dict["omim_id__list"]
        );
        self._distinct_ids__list__dict["iembase_id__list"]=self._iembase_id__list;
        
        self._gene_info__dict, self._gene_id__list=package_gene_info(
            self._gene_info_tsv_file_name
            ,self._distinct_ids__list__dict["gene_symbol__list"]
        );
        self._distinct_ids__list__dict["gene_id__list"]=self._gene_id__list;
        #LOGGER.info("self._distinct_ids__list__dict[\"gene_symbol__list\"] is:'%s'"%(json.dumps(self._distinct_ids__list__dict["gene_symbol__list"],indent=4)));
        #LOGGER.info("self._gene_info__dict is:'%s'"%(json.dumps(self._gene_info__dict,indent=4)));
        
        self._gene_id__2__uniprotkb_id__dict, self._uniprotkb_id__list=package_gene_id__2__uniprotkb_id(
            self._gene_id__2__uniprotkb_id_tsv_file_name
            ,self._distinct_ids__list__dict["gene_id__list"]
        );
        self._distinct_ids__list__dict["uniprotkb_id__list"]=self._uniprotkb_id__list;
        #LOGGER.info("self._distinct_ids__list__dict[\"uniprotkb_id__list\"] is:'%s'"%(json.dumps(self._distinct_ids__list__dict["uniprotkb_id__list"],indent=4)));
        #LOGGER.info("self._gene_id__2__uniprotkb_id__dict is:'%s'"%(json.dumps(self._gene_id__2__uniprotkb_id__dict,indent=4)));
        
        self._uniprotkb_id__2__ko_id__dict, self._ko_id__list=package_uniprotkb_id__2__ko_id(
            self._uniprotkb_id__2__ko_id_tsv_file_name
            ,self._distinct_ids__list__dict["uniprotkb_id__list"]
        );
        self._distinct_ids__list__dict["ko_id__list"]=self._ko_id__list;
        #LOGGER.info("self._distinct_ids__list__dict[\"uniprotkb_id__list\"] is:'%s'"%(json.dumps(self._distinct_ids__list__dict["uniprotkb_id__list"],indent=4)));
        #LOGGER.info("self._uniprotkb_id__2__ko_id__dict is:'%s'"%(json.dumps(self._uniprotkb_id__2__ko_id__dict,indent=4)));
        
        self._uniprotkb_id__2__ec_number__dict, self._ec_number__list=package_uniprotkb_id__2__ec_number(
            self._uniprotkb_id__2__ec_number_tsv_file_name
            ,self._distinct_ids__list__dict["uniprotkb_id__list"]
        );
        self._distinct_ids__list__dict["ec_number__list"]=self._ec_number__list;
        #LOGGER.info("self._distinct_ids__list__dict[\"uniprotkb_id__list\"] is:'%s'"%(json.dumps(self._distinct_ids__list__dict["uniprotkb_id__list"],indent=4)));
        #LOGGER.info("self._uniprotkb_id__2__ec_number__dict is:'%s'"%(json.dumps(self._uniprotkb_id__2__ec_number__dict,indent=4)));
        
        self._DDIEM_drugbank_drug_name__dict=package_drugbank_drug_names(
            self._drugbank_drug_names_dataset_tsv_file_name
            ,self._distinct_ids__list__dict["drugbank_ID__list"]
        );
        #LOGGER.info("self._DDIEM_drugbank_drug_name__dict is:'%s'"%(json.dumps(self._DDIEM_drugbank_drug_name__dict,indent=4)));
        dest_dataset_json_file_name=os.path.join(self._dest_dir_file_name,"%s.clinical_logs_for_rdf_part1.drugbank_drug_names.json"%(os.path.splitext(os.path.basename(self._src_clinical_log_dataset_csv_file_name))[0]));
        dest_dataset_json_fh=None;
        dest_dataset_json_writer=None;
        dest_dataset_json_fh=open(dest_dataset_json_file_name,"wb");
        import codecs;
        json.dump(self._DDIEM_drugbank_drug_name__dict, codecs.getwriter("utf-8")(dest_dataset_json_fh), ensure_ascii=False, indent=4);
        dest_dataset_json_fh.flush();
        dest_dataset_json_fh.close();
        dest_dataset_json_fh=None;
        
        self._DDIEM_ChEBI_drug_name__dict=package_ChEBI_drug_names(
            self._ChEBI_drug_names_dataset_tsv_file_name
            ,self._distinct_ids__list__dict["chEBI_ID__list"]
        );
        
        ####for each distinct class of datatype found in the self._distinct_ids__list__dict write to file (start) 2019-10-21 1528hrs###
        for datatype_name, datatype_value__list in self._distinct_ids__list__dict.items():
            #construct file to write out these values.
            dest_dataset_csv_file_name=os.path.join(self._dest_dir_file_name,"%s.%s.csv"%(os.path.splitext(os.path.basename(self._src_clinical_log_dataset_csv_file_name))[0],datatype_name));
            dest_dataset_csv_fh=None;
            dest_dataset_csv_writer=None;
            dest_dataset_csv_fh=open(dest_dataset_csv_file_name,"w");
            dest_dataset_csv_writer=csv.writer(dest_dataset_csv_fh,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL);
            
            dest_dataset_csv_writer.writerow(["row_id","datatype_value"]);
            row_cnt=0;
            #iterate through the list of values.
            for datatype_value in datatype_value__list:
                row_cnt+=1;
                dest_dataset_csv_writer.writerow([row_cnt,datatype_value]);
            
            dest_dataset_csv_fh.flush();
            dest_dataset_csv_fh.close();
            dest_dataset_csv_fh=None;
        ####for each distinct class of datatype found in the self._distinct_ids__list__dict write to file (end) 2019-10-21 1538hrs###
        
        
        
        #LOGGER.info("self._DDIEM_ChEBI_drug_name__dict is:'%s'"%(json.dumps(self._DDIEM_ChEBI_drug_name__dict,indent=4)));
        dest_dataset_json_file_name=os.path.join(self._dest_dir_file_name,"%s.clinical_logs_for_rdf_part1.ChEBI_drug_names.json"%(os.path.splitext(os.path.basename(self._src_clinical_log_dataset_csv_file_name))[0]));
        dest_dataset_json_fh=None;
        dest_dataset_json_writer=None;
        dest_dataset_json_fh=open(dest_dataset_json_file_name,"wb");
        import codecs;
        json.dump(self._DDIEM_ChEBI_drug_name__dict, codecs.getwriter("utf-8")(dest_dataset_json_fh), ensure_ascii=False, indent=4);
        dest_dataset_json_fh.flush();
        dest_dataset_json_fh.close();
        dest_dataset_json_fh=None;
        
        if(1==1):
            self._processing_outcome__dict=cascade_fields_values(
                self.hostname,self.ipAddress,self.ppid,self.pid
                ,self.working_dir_file_name
                ,self.task_id
                ,self.task_formulation_timestamp
                ,self.worker_id
                ,self.worker_number
                ,self._borg_ddiem_relational_ontology_graph_csv_file_name
                ,self._src_clinical_log_dataset_csv_file_name
                ,self._dest_dir_file_name
                ,self._OMIM_mimTitles_dataset_tsv_file_name
                ,self._gene_info__dict
                ,self._omim_id__dict
                ,self._gene_id__2__uniprotkb_id__dict
                ,self._uniprotkb_id__2__ko_id__dict
                ,self._uniprotkb_id__2__ec_number__dict
                ,self._pubChem_CID_info__dict
                ,self._pubChem_SID_info__dict
                ,self._pubChem_AID_info__dict
            );
            LOGGER.info("self._processing_outcome__dict is:'%s'"%(json.dumps(self._processing_outcome__dict,indent=4)));
    def get_processing_outcome(self):
        return self._processing_outcome__dict;

oRegPattern_phenotype_ID=re.compile("^\s*(?P<phenotype_ID>[^\s\*]+)\s*(?P<phenotype_ID_is_superclass>\*?)\s*$",re.IGNORECASE);
oRegPattern_drugbank_ID=re.compile("^(?P<drugbank_ID>DB[0-9]+)$",re.IGNORECASE);
oRegPattern_chEBI_ID=re.compile("^CHEBI\:(?P<chEBI_ID>[0-9]+)$",re.IGNORECASE);
oRegPattern_pubChem_CID=re.compile("^PubChem\s*CID\s*\:\s*(?P<pubChem_CID>[0-9]+)\s*$",re.IGNORECASE);#PubChemCID:14049689 PubChem SID: 384573165
oRegPattern_pubChem_SID=re.compile("^PubChem\s*SID\s*\:\s*(?P<pubChem_SID>[0-9]+)\s*$",re.IGNORECASE);
oRegPattern_pubChem_AID=re.compile("^PubChem\s*AID\s*\:\s*(?P<pubChem_AID>[0-9]+)\s*$",re.IGNORECASE);
oRegPattern_whitespace=re.compile("\s+");
oRegPattern_digits=re.compile("^.*?(?P<digits>[0-9]+).*$",re.IGNORECASE);
oRegPattern_ec_number=re.compile("^\s*(EC\s*:?)?(?P<ec_number>([0-9]+|\-)\.([0-9]+|\-)\.([0-9]+|\-)\.([0-9]+|\-))\s*$",re.IGNORECASE);
#oRegPattern_uniprot_ID=re.compile("^\s*(?P<uniprot_ID>[A-Z][A-Z,0-9]{5})\s*$");
oRegPattern_uniprot_ID=re.compile("^\s*(?P<uniprot_ID>[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})\s*$");#see "https://www.uniprot.org/help/accession_numbers" thanks Ali for sharing this resource.

    
def package_omim_id(
    _iembase_mapping_csv_file_name
    ,_omim_id__list
):
    pass;
    _omim_id__dict={};
    _iembase_id__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_iembase_mapping_csv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter=","
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            taxon_id=None;
            gene_id=None;
            gene_symbol=None;
            locus_tag=None;
            record_ordinal_position=row_cnt;
            iembase_id=row[0];
            iembase_name=row[1];
            omim_id_raw=row[2];
            #import re;omim_id_value="612940; 614438";omim_id_value__list=re.split('\s*;\s*|\s*,\s*',omim_id_value);omim_id_value__list;
            #import re;omim_id_value="615350, 615351, 615352";omim_id_value__list=re.split('\s*;\s*|\s*,\s*',omim_id_value);omim_id_value__list;
            omim_id_value__list=re.split('\s*;\s*|\s*,\s*',omim_id_raw);
            for omim_id_value in omim_id_value__list:
                if(omim_id_value in _omim_id__list):
                    _omim_id__dict[omim_id_value]={
                        "record_ordinal_position":record_ordinal_position
                        ,"iembase_id":iembase_id
                        ,"omim_id":omim_id_value
                    };
                    _iembase_id__list.append(iembase_id);
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _iembase_id__list=list(set(_iembase_id__list));
    _iembase_id__list.sort(reverse=False)
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_iembase_id__list is:'%s'"%(json.dumps(_iembase_id__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_omim_id__dict is:'%s'"%(json.dumps(_omim_id__dict,indent=4)));
    return (_omim_id__dict, _iembase_id__list);

def package_pubChem_CID_info(
    _PubChem_CID_csv_file_name
    ,_pubChem_CID__list
):
    pass;
    _pubChem_CID_info__dict={};
    _CID_id__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_PubChem_CID_csv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter=","
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            #cid,cmpdname,cmpdsynonym,mw,mf,polararea,complexity,xlogp,heavycnt,hbonddonor,hbondacc,rotbonds,inchikey,iupacname,meshheadings,annothits,annothitcnt,aids,cidcdate,dois
            row_id=None;
            record_ordinal_position=None;
            cid=None;
            cmpdname=None;
            cmpdsynonym=None;
            mw=None;
            mf=None;
            polararea=None;
            
            record_ordinal_position=row_cnt;
            CID_id=row[0];
            cmpdname=row[1];
            
            for _pubChem_CID in _pubChem_CID__list:
                _pubChem_CID_number=_pubChem_CID.split("CID:")[-1];
                LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_pubChem_CID_number is:'{0}', CID_id is:'{1}'".format(json.dumps(_pubChem_CID_number,indent=4),CID_id));
                if(_pubChem_CID_number==CID_id):
                    _CID_id__list.append(CID_id);
                    _pubChem_CID_info__dict[_pubChem_CID]={
                        "record_ordinal_position":record_ordinal_position
                        ,"pubChem_CID":_pubChem_CID
                        ,"CID_id":CID_id
                        ,"cmpdname":cmpdname
                    };
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _CID_id__list=list(set(_CID_id__list));
    _CID_id__list.sort(reverse=False)
    
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_pubChem_CID__list is:'{0}'".format(json.dumps(_pubChem_CID__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_CID_id__list is:'%s'"%(json.dumps(_CID_id__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_pubChem_CID_info__dict is:'%s'"%(json.dumps(_pubChem_CID_info__dict,indent=4)));
    return (_pubChem_CID_info__dict, _CID_id__list);

def package_gene_info(
    _gene_info_tsv_file_name
    ,_gene_symbol__list
):
    pass;
    _gene_info__dict={};
    _gene_id__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_gene_info_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            taxon_id=None;
            gene_id=None;
            gene_symbol=None;
            locus_tag=None;
            record_ordinal_position=row_cnt;
            taxon_id=row[0];
            gene_id=row[1];
            gene_symbol=row[2];
            locus_tag=row[3];
            
            if(gene_symbol.upper() in _gene_symbol__list and taxon_id=="9606"):
                gene_symbol_ordinal_position=_gene_symbol__list.index(gene_symbol.upper());
                _gene_info__dict[gene_symbol.upper()]={
                    "record_ordinal_position":record_ordinal_position
                    ,"taxon_id":taxon_id
                    ,"gene_id":gene_id
                    ,"gene_symbol":gene_symbol
                    ,"gene_symbol_ordinal_position":gene_symbol_ordinal_position
                    ,"locus_tag":locus_tag
                };
                _gene_id__list.append(gene_id);
                #_gene_id__list.append("%s,%s,%d"%(gene_id,gene_symbol,gene_symbol_ordinal_position));
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _gene_id__list=list(set(_gene_id__list));
    _gene_id__list.sort(reverse=False)
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_gene_id__list is:'%s'"%(json.dumps(_gene_id__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_gene_info__dict is:'%s'"%(json.dumps(_gene_info__dict,indent=4)));
    return (_gene_info__dict, _gene_id__list);

def package_gene_id__2__uniprotkb_id(
    _gene_id__2__uniprotkb_id_tsv_file_name
    ,_gene_id__list
):
    pass;
    _gene_id__2__uniprotkb_id__dict={};
    _uniprotkb_id__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_gene_id__2__uniprotkb_id_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            taxon_id=None;
            gene_id=None;
            gene_symbol=None;
            locus_tag=None;
            record_ordinal_position=row_cnt;
            gene_id=row[0];
            uniprotkb_id=row[1];
            
            if(gene_id in _gene_id__list):
                gene_id_ordinal_position=_gene_id__list.index(gene_id);
                _gene_id__2__uniprotkb_id__dict[gene_id]={
                    "record_ordinal_position":record_ordinal_position
                    ,"gene_id":gene_id
                    ,"uniprotkb_id":uniprotkb_id
                };
                _uniprotkb_id__list.append(uniprotkb_id);
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _gene_id__list=list(set(_gene_id__list));
    _gene_id__list.sort(reverse=False)
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_uniprotkb_id__list is:'%s'"%(json.dumps(_uniprotkb_id__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_gene_id__2__uniprotkb_id__dict is:'%s'"%(json.dumps(_gene_id__2__uniprotkb_id__dict,indent=4)));
    return (_gene_id__2__uniprotkb_id__dict, _uniprotkb_id__list);

def package_uniprotkb_id__2__ko_id(
    _uniprotkb_id__2__ko_id_tsv_file_name
    ,_uniprotkb_id__list
):
    pass;
    _uniprotkb_id__2__ko_id__dict={};
    _ko_id__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_uniprotkb_id__2__ko_id_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            uniprotkb_id=None;
            ko_id=None;
            record_ordinal_position=row_cnt;
            uniprotkb_id=row[0];
            ko_id=row[1];
            
            if(uniprotkb_id in _uniprotkb_id__list):
                gene_id_ordinal_position=_uniprotkb_id__list.index(uniprotkb_id);
                _uniprotkb_id__2__ko_id__dict[uniprotkb_id]={
                    "record_ordinal_position":record_ordinal_position
                    ,"uniprotkb_id":uniprotkb_id
                    ,"ko_id":ko_id
                };
                _ko_id__list.append(ko_id);
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _ko_id__list=list(set(_ko_id__list));
    _ko_id__list.sort(reverse=False)
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_ko_id__list is:'%s'"%(json.dumps(_ko_id__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_uniprotkb_id__2__ko_id__dict is:'%s'"%(json.dumps(_uniprotkb_id__2__ko_id__dict,indent=4)));
    return (_uniprotkb_id__2__ko_id__dict, _ko_id__list);

def package_uniprotkb_id__2__ec_number(
    _uniprotkb_id__2__ec_number_tsv_file_name
    ,_uniprotkb_id__list
):
    pass;
    _uniprotkb_id__2__ec_number__dict={};
    _ec_number__list=[];
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_uniprotkb_id__2__ec_number_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            uniprotkb_id=None;
            ec_number=None;
            record_ordinal_position=row_cnt;
            uniprotkb_id=row[0];
            ec_number=row[1];
            
            if(uniprotkb_id in _uniprotkb_id__list):
                gene_id_ordinal_position=_uniprotkb_id__list.index(uniprotkb_id);
                _uniprotkb_id__2__ec_number__dict[uniprotkb_id]={
                    "record_ordinal_position":record_ordinal_position
                    ,"uniprotkb_id":uniprotkb_id
                    ,"ec_number":ec_number
                };
                _ec_number__list.append(ec_number);
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    _ec_number__list=list(set(_ec_number__list));
    _ec_number__list.sort(reverse=False)
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_ec_number__list is:'%s'"%(json.dumps(_ec_number__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>_uniprotkb_id__2__ec_number__dict is:'%s'"%(json.dumps(_uniprotkb_id__2__ec_number__dict,indent=4)));
    return (_uniprotkb_id__2__ec_number__dict, _ec_number__list);

def package_drugbank_drug_names(
    _drugbank_drug_names_dataset_tsv_file_name
    ,_drugbank_ID__list
):
    pass;
    _DDIEM_drugbank_drug_name__dict={};
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_drugbank_drug_names_dataset_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            record_ordinal_position=None;
            drugbank_id__value=None;
            drug_name=None;
            drug_type=None;
            drug_date_of_update_str=None;
            drug_date_of_construction_str=None;
            drug_description=None;
            record_ordinal_position=row[0];
            drugbank_id__value=row[1];
            drug_name=row[2];
            drug_type=row[3];
            drug_date_of_update_str=row[4];
            drug_date_of_construction_str=row[5];
            drug_description=row[6];
            if(drugbank_id__value in _drugbank_ID__list):
                _DDIEM_drugbank_drug_name__dict[drugbank_id__value]={
                    "record_ordinal_position":record_ordinal_position
                    ,"drugbank_id__value":drugbank_id__value
                    ,"drug_name":drug_name
                    ,"drug_type":drug_type
                    ,"drug_date_of_update_str":drug_date_of_update_str
                    ,"drug_date_of_construction_str":drug_date_of_construction_str
                    ,"drug_description":drug_description
                };
                
                
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    return _DDIEM_drugbank_drug_name__dict;

def package_ChEBI_drug_names(
    _ChEBI_drug_names_dataset_tsv_file_name
    ,_ChEBI_ID__list
):
    pass;
    _DDIEM_ChEBI_drug_name__dict={};
    """
    "chEBI_ID__list": [
        "CHEBI_17012",
        "CHEBI_32362",
        "CHEBI_113373",
        "CHEBI_26537",
        "CHEBI_25548",
        "CHEBI_15724",
        "CHEBI_32030",
        "CHEBI_28384"
    ],
    """;
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(_ChEBI_drug_names_dataset_tsv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    cnt_of_fields__max=0;
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(row_cnt>1):
            row_id=None;
            _ChEBI_names_id=None;
            _compound_id=None;
            _type=None;
            _source=None;
            _name=None;
            _adapted_language=None;
            ChEBI_id__value=None;
            _ChEBI_names_id=row[0];
            _compound_id=row[1];
            _type=row[2];
            _source=row[3];
            _name=row[4];
            _adapted_language=row[5];
            ChEBI_id__value="CHEBI_%s"%(_compound_id);
            if(ChEBI_id__value in _ChEBI_ID__list):
                _DDIEM_ChEBI_drug_name__minor__dict__list=[];
                if(ChEBI_id__value in _DDIEM_ChEBI_drug_name__dict):
                    _DDIEM_ChEBI_drug_name__minor__dict__list=_DDIEM_ChEBI_drug_name__dict[ChEBI_id__value];
                _DDIEM_ChEBI_drug_name__minor__dict__list.append(
                    {
                        "ChEBI_names_id":_ChEBI_names_id
                        ,"compound_id":_compound_id
                        ,"type":_type
                        ,"source":_source
                        ,"name":_name
                        ,"adapted_language":_adapted_language
                    }
                );
                _DDIEM_ChEBI_drug_name__dict[ChEBI_id__value]=_DDIEM_ChEBI_drug_name__minor__dict__list;
                
                
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    return _DDIEM_ChEBI_drug_name__dict;

def obtain_distinct_values(
    hostname,ipAddress,ppid,pid
    ,working_dir_file_name
    ,task_id
    ,task_formulation_timestamp
    ,worker_id
    ,worker_number
    ,_src_clinical_log_dataset_csv_file_name
):
    pass;
    processing_outcome__dict={};
    task_commencement_time_obj=datetime.datetime.now();
    task_commencement_time_str=task_commencement_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f');
    
    row_id__selection__list=[];
    if(1==2):
        #row_id__selection__list.extend([1]);#The first data row.
        for row_id in range(973,974,1):
            print("row_id is:%d"%row_id);
            row_id__selection__list.append(row_id);
        row_id__selection__list.extend([1293]);
    if(1==2):
        row_id__selection__list.extend([1]);#The first data row.
        for row_id in range(3,14+1,1):
            row_id__selection__list.append(row_id);
        for row_id in range(22,26+1,1):#Row 24 has uniprot_ID
            row_id__selection__list.append(row_id);
        for row_id in range(106,118+1,1):
            row_id__selection__list.append(row_id);
        row_id__selection__list.extend([367]);#row_id 367 has uniprot_ID
        row_id__selection__list.extend([388]);#row_id 388 has ec number "EC 3.4.14.9"
        row_id__selection__list.extend([437]);#row_id 437 has uniprot_ID "Q3US15*"
        row_id__selection__list.extend([678]);#row_id 678 has drug_id "DB14502 orDB09449 +DB11094"
        for row_id in range(1254,1262+1,1):
            row_id__selection__list.append(row_id);
        #row_id__selection__list.extend([677,678,806,1260,1426,1513,1562]);
        """
        row_id 1353 has "ec_number (col 8)":"4.2.1.22"
        row_id 1353 has "mutations improved by treatment (col 13)":"P49L, A114V, I278T, R266K, or R336H"
        row_id 1353 has "mutations not improved by treatment (col 15)":"R125Q, E176K, T191M, T262M, or G307S"
        """
        row_id__selection__list.extend([1353]);
        for row_id in range(1383,1390+1,1):
            row_id__selection__list.append(row_id);
        for row_id in range(1558,1565+1,1):
            row_id__selection__list.append(row_id);
    """
date;time screen -S "backup__db__all";date;
task_formulation_timestamp_str="$(date +%Y%m%d_%H%M%S_%N)" \
 && dest_dir_file_name="/local/data/backups/bioinfo.cbrc.kaust.edu.sa/postgreSQL/${task_formulation_timestamp_str}" \
 && dest_dir_file_name="/biocorelab/BCLCustomers/kamauaa/backups/bioinfo.cbrc.kaust.edu.sa/postgreSQL/${task_formulation_timestamp_str}" \
 && mkdir -p "${dest_dir_file_name}" \
 && dest_sql_file_name="${dest_dir_file_name}/all.${task_formulation_timestamp_str}.sql" \
 && dest_sql_file_basename="$(basename ${dest_sql_file_name})" \
 && log_file_name="${dest_dir_file_name}/${dest_sql_file_basename%.*}.log" \
 && echo `date +%Y-%m-%d.%H%Mhrs.%S.%N`", log_file_name is:'${log_file_name}'" \
 && date && time /local/data/apps/postgreSQL/pgsql-11.1/bin/pg_dumpall -Upostgres -hlocalhost -p5432 --clean --if-exists --file="${dest_sql_file_name}">"${log_file_name}" 2>&1 && date;
date;time less "${log_file_name}";date;
    """
    """
5,drug,Field 10 (J),drugbank_ID,DB00741,https://www.drugbank.ca/drugs/DB00741
6,drug,Field 10 (J),ChEBI_ID,ChEBI:28384,http://purl.obolibrary.org/obo/ChEBI_28384
7,drug,Field 10 (J),WHOCC_ID,M01AX,https://www.whocc.no/atc_ddd_index/?code=M01AX
    """
    
    
    src_clinical_log_dataset_csv_file_name=_src_clinical_log_dataset_csv_file_name;
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(src_clinical_log_dataset_csv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter=","
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    
    
    row_id=None;
    oMIM_ID=None;
    gene_affected=None;
    enzyme_or_protein_detected=None;#Enzyme or protein short name
    enzyme_or_protein_detected__sha256=None;
    ec_number=None;
    uniprot_ID=None;
    drug_ID=None;
    drug_ID_normalized=None;
    
    drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
    
    omim_id__list=[];
    gene_symbol__list=[];
    gene_affected__list=[];
    gene_affected_unresolved__list=[];
    uniprot_ID__list=[];
    ec_number__list=[];
    enzyme_or_protein_detected_unresolved__list=[];
    drugbank_ID__list=[];
    chEBI_ID__list=[];
    pubChem_CID__list=[];
    pubChem_SID__list=[];
    pubChem_AID__list=[];
    wHOCC_ID__list=[];
    
    
    cnt_of_fields__max=0;
    populated_fields__dict={};
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(1==1):
            row_id=None;
            oMIM_ID=None;
            disease_name=None;
            gene_affected=None;
            enzyme_or_protein_detected=None;#Enzyme or protein short name
            enzyme_or_protein_detected__sha256=None;
            ec_number=None;
            uniprot_ID=None;
            enzyme_or_protein_detected_unresolved=None;
            drug_formulation_dosage=None;
            drug_ID=None;
            drug_ID_normalized=None;
            drug_ID_logical_operator__dict=None;
            drug_ID__ORed__list=None;
            drug_ID__ANDed__list=None;
            
            drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
            
            if(row_cnt<=2):
                pass;
                #row2=row[:];
                #populated_fields__dict={};
            else:
                row_id=row[0];
                #if(row_cnt>1182 and row_cnt<1193):
                if(len(row_id)>0 and (1==2 or row_id__selection__list==None or len(row_id__selection__list)==0 or int(row_id)in row_id__selection__list)):
                    pass;
                    #LOGGER.info("Processing row with row_id %s, row_id__selection__list is:'%s', row is:'%s'"%(row_id,row_id__selection__list,row));
                    drug_formulation_dosage=None;
                    drug_ID2=None;
                    drug_ID__list=None;
                    drug_ID2__sha256=None;
                    drug_ID__ORed__list=None;
                    drug_ID__ORed__csv=None;
                    drugbank_ID__ORed__csv=None;
                    chEBI_ID__ORed__csv=None;
                    pubChem_CID__ORed__csv=None;
                    pubChem_SID__ORed__csv=None;
                    pubChem_AID__ORed__csv=None;
                    wHOCC_ID__ORed__csv=None;
                    
                    drug_ID__ANDed__list=None;
                    drug_ID__ANDed__csv=None;
                    drugbank_ID__ANDed__csv=None;
                    chEBI_ID__ANDed__csv=None;
                    pubChem_CID__ANDed__csv=None;
                    pubChem_SID__ANDed__csv=None;
                    pubChem_AID__ANDed__csv=None;
                    wHOCC_ID__ANDed__csv=None;
                    
                    disease_name=None;
                    disease_comment=None;
                    regimen_name=None;
                    regimen_comment=None;
                    phenotype_improved_by_treatment_comment=None;
                    
                    
                    """
                    Now assign values to the key variables
                    """;
                    #LOGGER.info("row is:'%s'"%(json.dumps(row,indent=4)));
                    match=oRegPattern_digits.search(row[2]);
                    if(match!=None and match.group(0)!=None):
                        oMIM_ID=match.group("digits");
                        omim_id__list.append(oMIM_ID);
                        """
                        if(oMIM_ID in OMIM_mimTitles_dict):
                            omim_number_prefix=OMIM_mimTitles_dict[oMIM_ID][0];
                            omim_number=OMIM_mimTitles_dict[oMIM_ID][1];
                            omim_title_preferred=OMIM_mimTitles_dict[oMIM_ID][2];
                            omim_title_alternative=OMIM_mimTitles_dict[oMIM_ID][3];
                            omim_title_included=OMIM_mimTitles_dict[oMIM_ID][4];
                        """;
                    disease_name=row[3];
                    disease_comments=row[4];
                    """
                    tmp_str__list=None;
                    tmp_str__list=re.sub("\s+"," ",row[5]).strip().replace("/",",").replace(" ",",").split(",");
                    #tmp_str__list=re.sub("\s+","",row[5]).strip().replace("/",",").split(",");
                    if(tmp_str__list!=None):
                        for tmp_str in tmp_str__list:
                            #gene_affected=tmp_str.strip(" gene").strip();gene_affected__list.append(gene_affected);
                            if(tmp_str!="gene"):
                                gene_affected=tmp_str.strip(" gene").strip();
                                if("?" in gene_affected):
                                    gene_affected_unresolved__list.append(gene_affected);
                                else:
                                    gene_affected__list.append(gene_affected);
                                    
                    """;
                    
                    #############
                    #gene_affected=row[5].strip(" gene").strip();
                    gene_affected=None;gene_affected__list__minor=[];gene_affected__csv=None;
                    genes_affected__str=row[5];
                    genes_affected__str__transformed=genes_affected__str.strip(" gene").strip().replace(" and ",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(" or ",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("+",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("/",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("(","");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(")","");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("+",",");
                    genes_affected__str__transformed=re.sub("\s+", " ", genes_affected__str__transformed).strip();
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(" ",",");
                    genes_affected__str__transformed=re.sub(",+", ",", genes_affected__str__transformed).strip();
                    
                    
                    
                    #gene_affected__list__minor=remove_empty_values_from_list(csv_to_list(genes_affected__str__transformed));
                    gene_affected__list__minor2=csv_to_list(genes_affected__str__transformed);
                    gene_affected__list__minor2=remove_empty_values_from_list(gene_affected__list__minor2);
                    gene_affected__list__minor3=[];
                    if(gene_affected__list__minor!=None):
                        for gene_affected in gene_affected__list__minor2:
                            if("?" in gene_affected):
                                gene_affected_unresolved__list.append(gene_affected);
                            else:
                                gene_affected__list__minor3.append(gene_affected);
                        gene_affected__list__minor2=gene_affected__list__minor3;
                        gene_affected__list.extend(gene_affected__list__minor2);
                    #############
                                    
                    enzyme_or_protein_detected=row[6];#Enzyme or protein short name
                    enzyme_or_protein_detected__sha256=encrypt_string(enzyme_or_protein_detected);
                    ec_number=None;
                    uniprot_ID=None;
                    tmp_str__list=None;
                    #tmp_str__list=re.sub("\s+"," ",row[7]).strip().replace("/",",").replace(" ",",").split(",");
                    tmp_str__list=re.sub("\s+"," ",row[7]).strip().replace("/",",").replace("+",",").replace("or",",").replace("and",",").replace("(","").replace(")",",").split(",");
                    if(tmp_str__list!=None):
                        for tmp_str in tmp_str__list:
                            match=oRegPattern_ec_number.search(tmp_str);
                            if(match!=None and match.group(0)!=None):
                                ec_number=match.group("ec_number");
                                ec_number__list.append(ec_number);
                            else:
                                match=oRegPattern_uniprot_ID.search(tmp_str);
                                if(match!=None and match.group(0)!=None):
                                    uniprot_ID=match.group("uniprot_ID");
                                    uniprot_ID__list.append(uniprot_ID);
                                else:
                                    enzyme_or_protein_detected_unresolved=tmp_str;
                                    enzyme_or_protein_detected_unresolved__list.append(enzyme_or_protein_detected_unresolved);
                    drug_formulation_dosage=row[8];#this column was introduced in the 2019-11-22.0032hrs version of the DDIEM dataset. 
                    regimen_name=row[9];#this should be ignored and the regimen_name obtained from ontology resource via drug_ID should be used instead.
                    drug_ID=row[11];
                    
                    """
    5,drug,Field 10 (J),drugbank_ID,DB00741,https://www.drugbank.ca/drugs/DB00741
    6,drug,Field 10 (J),chEBI_ID,ChEBI:28384,http://purl.obolibrary.org/obo/ChEBI_28384
    7,drug,Field 10 (J),WHOCC_ID,M01AX,https://www.whocc.no/atc_ddd_index/?code=M01AX
    
    
                    """
                    #drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
                    drug_ID2=re.sub("\s+","",drug_ID).strip();
                    drug_ID2=drug_ID2.replace("+"," + ");
                    drug_ID2=drug_ID2.replace("or"," or ");
                    drug_ID2=drug_ID2.replace("/"," / ");
                    #drug_ID2=oRegPattern_whitespace.sub(" ",drug_ID2);
                    #drug_ID2=drug_ID2.strip();
                    drug_ID2=drug_ID2.replace("(","");
                    drug_ID2=drug_ID2.replace(")","");
                    drug_ID2=re.sub("\s+"," ",drug_ID2).strip();
                    if(drug_ID2=="NA"):
                        drug_ID2="";
                    if(len(drug_ID2)>0):
                        drug_ID2__sha256=encrypt_string(drug_ID2);
                    drug_ID_tmp="";
                    drug_ID_current=None;
                    drug_ID_operator_tmp=None;
                    drug_ID_operator_current=None;
                    drug_ID_operator_previous=None;
                    drug_ID_normalized="";
                    in_operator_section=False;
                    
                    #bracketed_group__dict__stack=generate_stack_from_bracketed_list(drug_ID2);
                    #LOGGER.info("-------------------------------row_id:%s, bracketed_group__dict__stack is:'%s'"%(row_id, json.dumps(bracketed_group__dict__stack, indent=4)));
                    
                    #drug_group__dict__stack=compose_regimen__into_JSON(row_id, drug_ID2);
                    #LOGGER.info("-------------------------------row_id:%s, drug_group__dict__stack is:'%s'"%(row_id, json.dumps(drug_group__dict__stack, indent=4)));
                    regimen_decomposition__dict=compose_regimen(row_id, drug_ID2);
                    
                    c=regimen_decomposition__dict["c"];
                    drug_ID_tmp=regimen_decomposition__dict["drug_ID_tmp"];
                    drug_ID__ORed__list=regimen_decomposition__dict["drug_ID__ORed__list"];
                    drug_ID__ANDed__list=regimen_decomposition__dict["drug_ID__ANDed__list"];
                    drug_ID_operator_current=regimen_decomposition__dict["drug_ID_operator_current"];
                    if(row_cnt>1468 and row_cnt<1472):
                        pass;
                        LOGGER.info("row_cnt:%s, row_id:%s, c is:'%s', drug_ID2 is:'%s', drug_ID_tmp is:'%s', drug_ID__ORed__list:'%s', drug_ID__ANDed__list:'%s', drug_ID_operator_current:'%s'"%(row_cnt,row_id,c,drug_ID2,drug_ID_tmp,drug_ID__ORed__list,drug_ID__ANDed__list,drug_ID_operator_current));
                        #LOGGER.info("row_id:%s, drug_ID_tmp is:'%s'"%(row_id,drug_ID_tmp));
                        
                    #generate the various drug database drug_id lists that are to be ORed
                    drug_ID__ORed__csv=list_to_csv(remove_empty_values_from_list(drug_ID__ORed__list));
                    drug_ID__list=drug_ID__ORed__list;
                    grouped_drug_ids_by_database=group_drug_ids_by_database(
                        drug_ID__list
                    );
                    drugbank_ID__ORed__csv=grouped_drug_ids_by_database["drugbank_ID__csv"];
                    chEBI_ID__ORed__csv=grouped_drug_ids_by_database["chEBI_ID__csv"];
                    pubChem_CID__ORed__csv=grouped_drug_ids_by_database["pubChem_CID__csv"];
                    pubChem_SID__ORed__csv=grouped_drug_ids_by_database["pubChem_SID__csv"];
                    pubChem_AID__ORed__csv=grouped_drug_ids_by_database["pubChem_AID__csv"];
                    wHOCC_ID__ORed__csv=grouped_drug_ids_by_database["wHOCC_ID__csv"];
                    
                    if(drugbank_ID__ORed__csv!=None and len(drugbank_ID__ORed__csv.strip())>0):
                        drugbank_ID__list.extend(remove_empty_values_from_list(csv_to_list(drugbank_ID__ORed__csv)));
                    if(chEBI_ID__ORed__csv!=None and len(chEBI_ID__ORed__csv.strip())>0):
                        chEBI_ID__list.extend(remove_empty_values_from_list(csv_to_list(chEBI_ID__ORed__csv)));
                    if(pubChem_CID__ORed__csv!=None and len(pubChem_CID__ORed__csv.strip())>0):
                        pubChem_CID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_CID__ORed__csv)));
                    if(pubChem_SID__ORed__csv!=None and len(pubChem_SID__ORed__csv.strip())>0):
                        pubChem_SID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_SID__ORed__csv)));
                    if(pubChem_AID__ORed__csv!=None and len(pubChem_AID__ORed__csv.strip())>0):
                        pubChem_AID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_AID__ORed__csv)));
                    if(wHOCC_ID__ORed__csv!=None and len(wHOCC_ID__ORed__csv.strip())>0):
                        wHOCC_ID__list.extend(remove_empty_values_from_list(csv_to_list(wHOCC_ID__ORed__csv)));
                    
                    #generate the various drug database drug_id lists that are to be ANDed
                    drug_ID__ANDed__csv=list_to_csv(remove_empty_values_from_list(drug_ID__ANDed__list));
                    drug_ID__list=drug_ID__ANDed__list;
                    grouped_drug_ids_by_database=group_drug_ids_by_database(
                        drug_ID__list
                    );
                    drugbank_ID__ANDed__csv=grouped_drug_ids_by_database["drugbank_ID__csv"];
                    pubChem_CID__ANDed__csv=grouped_drug_ids_by_database["pubChem_CID__csv"];
                    pubChem_SID__ANDed__csv=grouped_drug_ids_by_database["pubChem_SID__csv"];
                    pubChem_AID__ANDed__csv=grouped_drug_ids_by_database["pubChem_AID__csv"];
                    chEBI_ID__ANDed__csv=grouped_drug_ids_by_database["chEBI_ID__csv"];
                    wHOCC_ID__ANDed__csv=grouped_drug_ids_by_database["wHOCC_ID__csv"];
                    if(drugbank_ID__ANDed__csv!=None and len(drugbank_ID__ANDed__csv.strip())>0):
                        drugbank_ID__list.extend(remove_empty_values_from_list(csv_to_list(drugbank_ID__ANDed__csv)));
                    if(pubChem_CID__ANDed__csv!=None and len(pubChem_CID__ANDed__csv.strip())>0):
                        pubChem_CID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_CID__ANDed__csv)));
                    if(pubChem_SID__ANDed__csv!=None and len(pubChem_SID__ANDed__csv.strip())>0):
                        pubChem_SID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_SID__ANDed__csv)));
                    if(pubChem_AID__ANDed__csv!=None and len(pubChem_AID__ANDed__csv.strip())>0):
                        pubChem_AID__list.extend(remove_empty_values_from_list(csv_to_list(pubChem_AID__ANDed__csv)));
                    if(chEBI_ID__ANDed__csv!=None and len(chEBI_ID__ANDed__csv.strip())>0):
                        chEBI_ID__list.extend(remove_empty_values_from_list(csv_to_list(chEBI_ID__ANDed__csv)));
                    if(wHOCC_ID__ANDed__csv!=None and len(wHOCC_ID__ANDed__csv.strip())>0):
                        wHOCC_ID__list.extend(remove_empty_values_from_list(csv_to_list(wHOCC_ID__ANDed__csv)));
    
    omim_id__list=list(set(omim_id__list));
    gene_affected__list=list(set(gene_affected__list));
    gene_affected_unresolved__list=list(set(gene_affected_unresolved__list));
    uniprot_ID__list=list(set(uniprot_ID__list));
    ec_number__list=list(set(ec_number__list));
    enzyme_or_protein_detected_unresolved__list=list(set(enzyme_or_protein_detected_unresolved__list));
    drugbank_ID__list=list(set(drugbank_ID__list));
    chEBI_ID__list=list(set(chEBI_ID__list));
    pubChem_CID__list=list(set(pubChem_CID__list));
    pubChem_SID__list=list(set(pubChem_SID__list));
    pubChem_AID__list=list(set(pubChem_AID__list));
    wHOCC_ID__list=list(set(wHOCC_ID__list));
    
    if(omim_id__list!=None):
        omim_id__list.sort(reverse=False);
    if(gene_affected__list!=None):
        gene_affected__list.sort(reverse=False);
    if(gene_affected_unresolved__list!=None):
        gene_affected_unresolved__list.sort(reverse=False);
    if(uniprot_ID__list!=None):
        uniprot_ID__list.sort(reverse=False);
    if(ec_number__list!=None):
        ec_number__list.sort(reverse=False);
    if(enzyme_or_protein_detected_unresolved__list!=None):
        enzyme_or_protein_detected_unresolved__list.sort(reverse=False);
    if(drugbank_ID__list!=None):
        drugbank_ID__list.sort(reverse=False);
    if(chEBI_ID__list!=None):
        chEBI_ID__list.sort(reverse=False);
    if(pubChem_CID__list!=None):
        pubChem_CID__list.sort(reverse=False);
    if(pubChem_SID__list!=None):
        pubChem_SID__list.sort(reverse=False);
    if(pubChem_AID__list!=None):
        pubChem_AID__list.sort(reverse=False);
    if(wHOCC_ID__list!=None):
        wHOCC_ID__list.sort(reverse=False);
    
    src_dataset_csv_fh.close();
    src_dataset_csv_fh=None;
    
    for gene_affected in gene_affected__list:
        gene_symbol__list.append(gene_affected.upper());
    
    
    task_completion_time_obj=datetime.datetime.now();
    task_completion_time_str="%s"%(task_completion_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f'));
    duration_obj=task_completion_time_obj-task_commencement_time_obj;
    duration_ms=duration_obj.total_seconds()*1000;
    
    processing_outcome__dict["task_commencement_time_str"]=task_commencement_time_str;
    processing_outcome__dict["task_completion_time_str"]=task_completion_time_str;
    processing_outcome__dict["duration_ms"]=duration_ms;
    
    processing_outcome__dict["hostname"]=hostname;
    processing_outcome__dict["ipAddress"]=ipAddress;
    processing_outcome__dict["ppid"]=ppid;
    processing_outcome__dict["pid"]=pid;
    processing_outcome__dict["task_id"]=task_id;
    processing_outcome__dict["task_formulation_timestamp_str"]=task_formulation_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f');
    processing_outcome__dict["worker_id"]=worker_id;
    processing_outcome__dict["worker_number"]=worker_number;
    processing_outcome__dict["src_clinical_log_dataset_csv_file_name"]=src_clinical_log_dataset_csv_file_name;
    processing_outcome__dict["cnt_of_fields__max"]=cnt_of_fields__max;
    distinct_ids__list__dict={
        "omim_id__list":omim_id__list
        ,"gene_affected__list":gene_affected__list
        ,"gene_affected_unresolved__list":gene_affected_unresolved__list
        ,"gene_symbol__list":gene_symbol__list
        ,"uniprot_ID__list":uniprot_ID__list
        ,"ec_number__list":ec_number__list
        ,"enzyme_or_protein_detected_unresolved__list":enzyme_or_protein_detected_unresolved__list
        ,"drugbank_ID__list":drugbank_ID__list
        ,"chEBI_ID__list":chEBI_ID__list
        ,"pubChem_CID__list":pubChem_CID__list
        ,"pubChem_SID__list":pubChem_SID__list
        ,"pubChem_AID__list":pubChem_AID__list
        ,"wHOCC_ID__list":wHOCC_ID__list
    };
    return distinct_ids__list__dict;
    
def compose_regimen(row_id,drug_ID2):
    regimen_decomposition__dict={};
    drug_ID_tmp=None;
    in_operator_section=False;
    drug_ID__ORed__list=None;
    drug_ID__ANDed__list=None;
    drug_ID_operator_current=None;
    drug_ID_operator_tmp=None;
    drug_ID_operator_previous=None;
    c=None;
    
    #LOGGER.info("At compose_regimen, drug_ID2 is:'%s'"%(drug_ID2));
    
    
    for c in drug_ID2:
        if(c==" "):
            if(in_operator_section):
                doc="""
                we assume that this whitespace comes after an operator, and that the operator has been defined.
                Depending on just captured operator send the previously captured drug_ID to the appropriate list. 
                """;
                if(drug_ID_operator_current==","):
                    if(drug_ID__ORed__list==None):
                        drug_ID__ORed__list=[];
                    if(drug_ID_current!=None):
                        if(drug_ID_operator_previous!=None and drug_ID_operator_previous=="+"):
                            drug_ID__ANDed__list.append(drug_ID_current);
                        else:
                            drug_ID__ORed__list.append(drug_ID_current);
                    drug_ID_current=None;
                    drug_ID_tmp=None;
                elif(drug_ID_operator_current=="+"):
                    if(drug_ID__ANDed__list==None):
                        drug_ID__ANDed__list=[];
                    if(drug_ID_current!=None):
                        if(drug_ID_operator_previous!=None and drug_ID_operator_previous==","):
                            drug_ID__ORed__list.append(drug_ID_current);
                        else:
                            drug_ID__ANDed__list.append(drug_ID_current);
                    drug_ID_current=None;
                    drug_ID_tmp=None;
                in_operator_section=False;
            else:
                #signifies end of a drug name and we expect the operator to come next.
                drug_ID_current=drug_ID_tmp;
                drug_ID_tmp=None;
                in_operator_section=True;
        elif(in_operator_section):
            if(drug_ID_operator_tmp==None):
                drug_ID_operator_tmp="";
            drug_ID_operator_tmp="%s%s"%(drug_ID_operator_tmp,c);
            #test if the drug_ID_operator_tmp contains "+" or "or"
            if(drug_ID_operator_tmp=="+" or drug_ID_operator_tmp=="and"):
                if(drug_ID_operator_current!=None and len(drug_ID_operator_current)>0):
                    drug_ID_operator_previous=drug_ID_operator_current;
                drug_ID_operator_current="+";
                drug_ID_operator_tmp=None;
                in_operator_section=True;
            elif(drug_ID_operator_tmp=="," or drug_ID_operator_tmp=="or" or drug_ID_operator_tmp=="/"):
                if(drug_ID_operator_current!=None and len(drug_ID_operator_current)>0):
                    drug_ID_operator_previous=drug_ID_operator_current;
                drug_ID_operator_current=",";
                drug_ID_operator_tmp=None;
                in_operator_section=True;
        else:
            if(drug_ID_tmp==None):
                drug_ID_tmp="";
            drug_ID_tmp="%s%s"%(drug_ID_tmp,c);
        #LOGGER.info("row_id:%s, c is:'%s', drug_ID_tmp is:'%s', drug_ID__ORed__list:'%s', drug_ID__ANDed__list:'%s', drug_ID_operator_current:'%s'"%(row_id,c,drug_ID_tmp,drug_ID__ORed__list,drug_ID__ANDed__list,drug_ID_operator_current));
    #Now we address the any drug_ID term that could be still remaining 
    if(drug_ID_tmp!=None):
        drug_ID_current=drug_ID_tmp;
        if(drug_ID_operator_current==None or drug_ID_operator_current==","):
            if(drug_ID__ORed__list==None):
                drug_ID__ORed__list=[];
            drug_ID__ORed__list.append(drug_ID_current);
            drug_ID_current=None;
            drug_ID_tmp=None;
        elif(drug_ID_operator_current=="+"):
            if(drug_ID__ANDed__list==None):
                drug_ID__ANDed__list=[];
            drug_ID__ANDed__list.append(drug_ID_current);
            drug_ID_current=None;
            drug_ID_tmp=None;
    regimen_decomposition__dict={
        #"row_id":row_id
        "c":c
        ,"drug_ID_tmp":drug_ID_tmp
        ,"drug_ID__ORed__list":drug_ID__ORed__list
        ,"drug_ID__ANDed__list":drug_ID__ANDed__list
        ,"drug_ID_operator_current":drug_ID_operator_current
    };
    return regimen_decomposition__dict;

for row_id in range(973,974,1):
    print("row_id is:%d"%row_id);

def cascade_fields_values(
    hostname,ipAddress,ppid,pid
    ,working_dir_file_name
    ,task_id
    ,task_formulation_timestamp
    ,worker_id
    ,worker_number
    ,_borg_ddiem_relational_ontology_graph_csv_file_name
    ,_src_clinical_log_dataset_csv_file_name
    ,_dest_dir_file_name
    ,_OMIM_mimTitles_dataset_tsv_file_name
    ,_gene_info__dict
    ,_omim_id__dict
    ,_gene_id__2__uniprotkb_id__dict
    ,_uniprotkb_id__2__ko_id__dict
    ,_uniprotkb_id__2__ec_number__dict
    ,_pubChem_CID_info__dict
    ,_pubChem_SID_info__dict
    ,_pubChem_AID_info__dict
):
    pass;
    processing_outcome__dict={};
    gene_affected__symbol__found_in_geneinfo__list=[];
    gene_affected__symbol__not_found_in_geneinfo__list=[];
    
    task_commencement_time_obj=datetime.datetime.now();
    task_commencement_time_str=task_commencement_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f');
    
    row_id__selection__list=[];
    if(1==2):
        #row_id__selection__list.extend([1]);#The first data row.
        #for row_id in range(973,974,1):
        for row_id in range(1683,1687,1):
            print("row_id is:%d"%row_id);
            row_id__selection__list.append(row_id);
    if(1==2):
        row_id__selection__list.extend([1]);#The first data row.
        for row_id in range(3,14+1,1):
            row_id__selection__list.append(row_id);
        for row_id in range(22,26+1,1):#Row 24 has uniprot_id
            row_id__selection__list.append(row_id);
        for row_id in range(106,118+1,1):
            row_id__selection__list.append(row_id);
        row_id__selection__list.extend([367]);#row_id 367 has uniprot_id
        row_id__selection__list.extend([388]);#row_id 388 has ec number "EC 3.4.14.9"
        row_id__selection__list.extend([437]);#row_id 437 has uniprot_id "Q3US15*"
        row_id__selection__list.extend([678]);#row_id 678 has drug_id "DB14502 orDB09449 +DB11094"
        for row_id in range(1254,1262+1,1):
            row_id__selection__list.append(row_id);
        #row_id__selection__list.extend([677,678,806,1260,1426,1513,1562]);
        """
        row_id 1353 has "ec_number (col 8)":"4.2.1.22"
        row_id 1353 has "mutations improved by treatment (col 13)":"P49L, A114V, I278T, R266K, or R336H"
        row_id 1353 has "mutations not improved by treatment (col 15)":"R125Q, E176K, T191M, T262M, or G307S"
        """
        row_id__selection__list.extend([1353]);
        for row_id in range(1383,1390+1,1):
            row_id__selection__list.append(row_id);
        for row_id in range(1558,1565+1,1):
            row_id__selection__list.append(row_id);
    """
date;time screen -S "backup__db__all";date;
task_formulation_timestamp_str="$(date +%Y%m%d_%H%M%S_%N)" \
 && dest_dir_file_name="/local/data/backups/bioinfo.cbrc.kaust.edu.sa/postgreSQL/${task_formulation_timestamp_str}" \
 && dest_dir_file_name="/biocorelab/BCLCustomers/kamauaa/backups/bioinfo.cbrc.kaust.edu.sa/postgreSQL/${task_formulation_timestamp_str}" \
 && mkdir -p "${dest_dir_file_name}" \
 && dest_sql_file_name="${dest_dir_file_name}/all.${task_formulation_timestamp_str}.sql" \
 && dest_sql_file_basename="$(basename ${dest_sql_file_name})" \
 && log_file_name="${dest_dir_file_name}/${dest_sql_file_basename%.*}.log" \
 && echo `date +%Y-%m-%d.%H%Mhrs.%S.%N`", log_file_name is:'${log_file_name}'" \
 && date && time /local/data/apps/postgreSQL/pgsql-11.1/bin/pg_dumpall -Upostgres -hlocalhost -p5432 --clean --if-exists --file="${dest_sql_file_name}">"${log_file_name}" 2>&1 && date;
date;time less "${log_file_name}";date;
    """
    """
5,drug,Field 10 (J),drugbank_ID,DB00741,https://www.drugbank.ca/drugs/DB00741
6,drug,Field 10 (J),ChEBI_ID,ChEBI:28384,http://purl.obolibrary.org/obo/ChEBI_28384
7,drug,Field 10 (J),WHOCC_ID,M01AX,https://www.whocc.no/atc_ddd_index/?code=M01AX
    """
    
    
    src_clinical_log_dataset_csv_file_name=_src_clinical_log_dataset_csv_file_name;
    OMIM_mimTitles_dataset_tsv_file_name=_OMIM_mimTitles_dataset_tsv_file_name;
    dest_dataset_csv_file_name=os.path.join(_dest_dir_file_name,"%s.clinical_logs_for_rdf_part1.csv"%(os.path.splitext(os.path.basename(_src_clinical_log_dataset_csv_file_name))[0]));
    dest_DB_DBA_RDF_LOAD_RDFXML_MT__file_name=os.path.join(_dest_dir_file_name,"%s.DB.DBA.RDF_LOAD_RDFXML_MT.txt"%(os.path.splitext(os.path.basename(_src_clinical_log_dataset_csv_file_name))[0]));
    dest_DB_DBA_RDF_LOAD_RDFXML_MT__fh=open(dest_DB_DBA_RDF_LOAD_RDFXML_MT__file_name,"w");
    
    OMIM_mimTitles_dict=None;
    OMIM_mimTitles_dataset_tsv_fh=None;
    OMIM_mimTitles_dataset_tsv_reader=None;
    OMIM_mimTitles_dataset_tsv_fh=open(OMIM_mimTitles_dataset_tsv_file_name,"r");
    OMIM_mimTitles_dataset_tsv_fh.seek(0);
    OMIM_mimTitles_dataset_tsv_reader=csv.reader(
        OMIM_mimTitles_dataset_tsv_fh
        ,delimiter="\t"
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    OMIM_mimTitles_dict={};
    row_cnt=0;
    for row in OMIM_mimTitles_dataset_tsv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(len(row)>=3):
            OMIM_mimTitles_dict[row[1]]=row;
    OMIM_mimTitles_dataset_tsv_fh.close();
    OMIM_mimTitles_dataset_tsv_fh=None;
    OMIM_mimTitles_dataset_tsv_reader=None;
    
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(src_clinical_log_dataset_csv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter=","
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    
    dest_dataset_csv_fh=None;
    dest_dataset_csv_writer=None;
    dest_dataset_csv_fh=open(dest_dataset_csv_file_name,"w");
    dest_dataset_csv_writer=csv.writer(dest_dataset_csv_fh,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL);
    
    row_id=None;
    oMIM_ID=None;
    oMIM_ID__via_disease_name=None;
    disease_name=None;
    disease_comments=None;
    gene_affected__orig=None;gene_affected=None;gene_affected__list=[];gene_affected__csv=None;
    enzyme_or_protein_detected=None;#Enzyme or protein short name
    enzyme_or_protein_detected__sha256=None;
    uniprotids_and_or_ecnumbers_gene_product=None;uniprotids_and_or_ecnumbers_gene_product__transformed=None;ec_number=None;uniprot_ID=None;ec_number=None;ec_number__list=[];uniprot_ID=None;uniprot_ID__list=[];
    drug_formulation_dosage=None;
    regimen_name=None;#this should be ignored and the regimen_name obtained from ontology resource via drug_ID should be used instead.
    drug_IDs__str__orig=None;drug_ID=None;
    drug_ID_normalized=None;
    drug_ID_logical_operator__dict=None;
    drug_ID__ORed__list=None;
    drug_ID__ANDed__list=None;
    
    drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
    
    study_type_evidence_code__list=None;
    mutation_improved_by_treatment__list=None;
    mutation_not_improved_by_treatment__list=None;
    regimen_mechanism_of_action__list=None;
    regimen_mechanism_of_action_abbreviation__list=None;
    phenotype_improved_by_treatment__list=None;
    phenotype_ID__list=None;
    treatment_manuscript_reference__list=None;
    
    study_type_evidence_codes__str__orig=None;
    study_type_evidence_code__csv=None;
    mutation_improved_by_treatment__csv=None;
    mutation_not_improved_by_treatment__csv=None;
    regimen_mechanism_of_action__csv=None;
    regimen_mechanism_of_action_abbreviation__csv=None;
    phenotype_improved_by_treatment__csv=None;
    phenotype_ID__csv=None;
    treatment_manuscript_reference__csv=None;
    
    clinical_log_rdf_base_fields_dataset_header__list=[
        "row_id"
        ,"oMIM_ID"
        ,"oMIM_ID__via_disease_name"
        ,"omim_number_prefix"
        ,"omim_number"
        ,"omim_title_preferred"
        ,"omim_title_alternative"
        ,"omim_title_included"
        ,"disease_name"
        ,"disease_comments"
        ,"gene_affected__orig"
        ,"gene_affected__csv"
        ,"enzyme_or_protein_detected"
        ,"enzyme_or_protein_detected__sha256"
        ,"uniprotids_and_or_ecnumbers_gene_product__orig"
        ,"ec_number__csv"
        ,"uniprot_ID__csv"
        ,"drug_formulation_dosage"
        ,"regimen_name"
        ,"regimen_comments"
        ,"drug_IDs__orig"
        ,"drug_ID2"
        
        ,"drug_ID2__sha256"
        
        ,"drug_ID__ORed__csv"
        ,"drugbank_ID__ORed__csv"
        ,"chEBI_ID__ORed__csv"
        ,"wHOCC_ID__ORed__csv"
        
        ,"drug_ID__ANDed__csv"
        ,"drugbank_ID__ANDed__csv"
        ,"chEBI_ID__ANDed__csv"
        ,"wHOCC_ID__ANDed__csv"
        
        ,"study_type_evidence_codes__orig"
        ,"study_type_evidence_code__csv"
        ,"mutation_improved_by_treatment__csv"
        ,"mutation_not_improved_by_treatment__csv"
        ,"regimen_mechanism_of_action_ontology_category__csv"#"regimen_mechanism_of_action__csv"
        ,"regimen_mechanism_of_action_abbreviation__csv"
        ,"phenotype_improved_by_treatment__csv"
        ,"phenotype_ID__csv"
        ,"phenotype_improved_by_treatment_comments"
        ,"treatment_manuscript_reference__csv"
        ,"gene_id__csv"
        ,"gene_symbol__csv"
        ,"iembase_id__csv"
        ,"uniprotkb_id__csv"
        ,"ko_id__csv"
        ,"ec_number__csv"
        ,"pubChem_CID__ORed__csv"
        ,"pubChem_CID_name__ORed__csv"
        ,"pubChem_SID__ORed__csv"
        ,"pubChem_SID_name__ORed__csv"
        ,"pubChem_AID__ORed__csv"
        ,"pubChem_AID_name__ORed__csv"
        ,"pubChem_CID__ANDed__csv"
        ,"pubChem_CID_name__ANDed__csv"
        ,"pubChem_SID__ANDed__csv"
        ,"pubChem_SID_name__ANDed__csv"
        ,"pubChem_AID__ANDed__csv"
        ,"pubChem_AID_name__ANDed__csv"
        ,"drug_ID_NA_position__ORed__csv"
        ,"drug_ID_NA_position__ANDed__csv"
        ,"XML/RDF"
    ];
    dest_dataset_csv_writer.writerow(list(range(1,len(clinical_log_rdf_base_fields_dataset_header__list)+1)));
    dest_dataset_csv_writer.writerow(clinical_log_rdf_base_fields_dataset_header__list);
    
    cnt_of_fields__max=0;
    populated_fields__dict={};
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    """
id,entity class,entity instance field,subject represented by,example value,entity instance URI example
1,disease,Field 2 (B),OMIM_ID,603328,https://www.omim.org/entry/603328
2,gene,Field 5 (E),gene_name,L2HGDH,https://ghr.nlm.nih.gov/gene/L2HGDH
3,EC Number/Protein Entry,Field 7 (G),ec_number,1.14.14.19,https://enzyme.expasy.org/EC/1.14.14.19
4,EC Number/Protein Entry,Field 7 (G),uniprot_ID,Q6P5W5,https://www.uniprot.org/uniprot/Q6P5W5
5,drug,Field 10 (J),drugbank_ID,DB00741,https://www.drugbank.ca/drugs/DB00741
6,drug,Field 10 (J),chEBI_ID,ChEBI:28384,http://purl.obolibrary.org/obo/ChEBI_28384
7,drug,Field 10 (J),WHOCC_ID,M01AX,https://www.whocc.no/atc_ddd_index/?code=M01AX
8,Study Type (Evidence code),Field 11 (K),GO_ID,ECO:0000352,http://purl.obolibrary.org/obo/ECO_0000352
9,Phenotype IDS,Field 21 (U),phenotype_ID,HP:0040085,http://purl.obolibrary.org/obo/HP_0040085
10,disease_name,Field 3 (C),literal,,
11,mutation_improved_by_treatment,Field 12 (L),literal,,
12,mutation_not_improved_by_treatment,Field 14 (N),literal,,
13,reference,Field 22-23 (V-AB),URI,,    """
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        #del row2[:];
        for i, val in enumerate(row):
            if(row[i]==None):
                row[i]="";
            else:
                row[i]=row[i].strip();
            if(row[i]=='""' or row[i]=="''"):
                row[i]="";
        if(1==1):
            row_id=None;
            oMIM_ID=None;
            oMIM_ID__via_disease_name=None;
            omim_number_prefix=None;
            omim_number=None;
            omim_title_preferred=None;
            omim_title_alternative=None;
            omim_title_included=None;
            disease_name=None;
            disease_comments=None;
            gene_affected__orig=None;gene_affected=None;gene_affected__list=[];gene_affected__csv=None;
            enzyme_or_protein_detected=None;#Enzyme or protein short name
            enzyme_or_protein_detected__sha256=None;
            uniprotids_and_or_ecnumbers_gene_product=None;uniprotids_and_or_ecnumbers_gene_product__transformed=None;ec_number=None;uniprot_ID=None;ec_number=None;ec_number__list=[];uniprot_ID=None;uniprot_ID__list=[];
            
            drug_formulation_dosage=None;
            regimen_name=None;#this should be ignored and the regimen_name obtained from ontology resource via drug_ID should be used instead.
            regimen_comments=None;
            phenotype_improved_by_treatment_comments=None;
            drug_IDs__str__orig=None;drug_ID=None;
            drug_ID_normalized=None;
            drug_ID_logical_operator__dict=None;
            drug_ID__ORed__list=None;
            drug_ID__ANDed__list=None;
            
            
            drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
            study_type_evidence_codes__str__orig=None;
            study_type_evidence_code__list=None;
            mutation_improved_by_treatment__list=None;
            mutation_not_improved_by_treatment__list=None;
            regimen_mechanism_of_action__list=None;
            regimen_mechanism_of_action_abbreviation__list=None;
            regimen_mechanism_of_action_ontology_category__list=None;
            phenotype_improved_by_treatment__list=None;
            phenotype_ID__list=None;
            treatment_manuscript_reference__list=None;
            
            study_type_evidence_codes__str__orig=None;
            study_type_evidence_code__csv=None;
            mutation_improved_by_treatment__csv=None;
            mutation_not_improved_by_treatment__csv=None;
            regimen_mechanism_of_action__csv=None;
            regimen_mechanism_of_action_abbreviation__csv=None;
            phenotype_improved_by_treatment__csv=None;
            phenotype_ID__csv=None;
            treatment_manuscript_reference__csv=None;
            
            iembase_id__list=None;
            iembase_id__csv=None;
            
            
            if(row_cnt<=2):
                pass;
                #row2=row[:];
                #populated_fields__dict={};
            else:
                row_id=row[0];
                #if(row_cnt>1186 and row_cnt<1190):
                if(len(row_id)>0 and (1==2 or row_id__selection__list==None or len(row_id__selection__list)==0 or int(row_id)in row_id__selection__list)):
                    pass;
                    oMIM_ID__via_disease_name=None;
                    drug_ID2=None;
                    drug_ID__list=None;
                    """
                    drug_ID_normalized=None;
                    drug_ID_logical_operator__dict=None;
                    drug_ID__ORed__list=None;
                    drug_ID__ANDed__list=None;
                    
                    drugbank_ID=None;
                    drugbank_ID__list=None;
                    drugbank_ID__csv=None;
                    chEBI_ID=None;
                    chEBI_ID__list=None;
                    chEBI_ID__csv=None;
                    wHOCC_ID=None;
                    wHOCC_ID__list=None;
                    wHOCC_ID__csv=None;
                    """;
                    drug_formulation_dosage=None;
                    drug_ID2__sha256=None;
                    drug_ID__ORed__list=None;
                    drug_ID__ORed__csv=None;
                    drugbank_ID__ORed__csv=None;
                    chEBI_ID__ORed__csv=None;
                    pubChem_CID__ORed__csv=None;
                    wHOCC_ID__ORed__csv=None;
                    
                    drug_ID__ANDed__list=None;
                    drug_ID__ANDed__csv=None;
                    drugbank_ID__ANDed__csv=None;
                    chEBI_ID__ANDed__csv=None;
                    pubChem_CID__ANDed__csv=None;
                    wHOCC_ID__ANDed__csv=None;
                    
                    disease_name=None;
                    disease_comment=None;
                    regimen_name=None;
                    regimen_comment=None;
                    phenotype_improved_by_treatment_comment=None;
                    
                    """
                    Now assign values to the key variables
                    """;
                    #LOGGER.info("row is:'%s'"%(json.dumps(row,indent=4)));
                    match=oRegPattern_digits.search(row[2]);
                    if(match!=None and match.group(0)!=None):
                        oMIM_ID=match.group("digits");
                        if(oMIM_ID in _omim_id__dict):
                            if(iembase_id__list==None):
                                iembase_id__list=[];
                            iembase_id__list.append(_omim_id__dict[oMIM_ID]["iembase_id"]);
                        
                        if(oMIM_ID in OMIM_mimTitles_dict):
                            omim_number_prefix=OMIM_mimTitles_dict[oMIM_ID][0];
                            omim_number=OMIM_mimTitles_dict[oMIM_ID][1];
                            omim_title_preferred=OMIM_mimTitles_dict[oMIM_ID][2];
                            omim_title_alternative=OMIM_mimTitles_dict[oMIM_ID][3];
                            omim_title_included=OMIM_mimTitles_dict[oMIM_ID][4];
                    
                    disease_name=row[3];
                    #determine oMIM_ID by use of user provided disease_name
                    #oMIM_ID__via_disease_name
                    for oMIM_ID2, oMIM_data__list in OMIM_mimTitles_dict.items():
                        pass;
                        omim_number_prefix2=oMIM_data__list[0];
                        omim_number2=oMIM_data__list[1];
                        omim_title_preferred2=oMIM_data__list[2];
                        omim_title_alternative2=oMIM_data__list[3];
                        omim_title_included2=oMIM_data__list[4];
                        
                        if(disease_name.lower()==omim_title_preferred2.lower()):
                            oMIM_ID__via_disease_name=omim_number2;
                    
                    
                    disease_comments=row[4];
                    #############
                    #gene_affected=row[5].strip(" gene").strip();
                    gene_affected=None;gene_affected__list=[];gene_affected__csv=None;
                    gene_id__list=[];gene_id__csv=None;
                    gene_symbol__list=[];gene_symbol__csv=None;
                    genes_affected__str=row[5];
                    genes_affected__str__transformed=genes_affected__str.strip(" gene").strip().replace(" and ",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(" or ",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("+",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("/",",");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("(","");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(")","");
                    genes_affected__str__transformed=genes_affected__str__transformed.replace("+",",");
                    genes_affected__str__transformed=re.sub("\s+", " ", genes_affected__str__transformed).strip();
                    genes_affected__str__transformed=genes_affected__str__transformed.replace(" ",",");
                    genes_affected__str__transformed=re.sub(",+", ",", genes_affected__str__transformed).strip();
                    
                    
                    
                    #gene_affected__list=remove_empty_values_from_list(csv_to_list(genes_affected__str__transformed));
                    gene_affected__list=csv_to_list(genes_affected__str__transformed);
                    gene_affected__list=remove_empty_values_from_list(gene_affected__list);
                    if(gene_affected__list!=None):
                        #gene_affected__csv=list_to_csv(remove_empty_values_from_list(gene_affected__list));
                        gene_affected__csv=list_to_csv(gene_affected__list);
                        for gene_affected in gene_affected__list:
                            if gene_affected.upper() in _gene_info__dict:
                                gene_affected__symbol__found_in_geneinfo__list.append(gene_affected);
                                gene_id__list.append(_gene_info__dict[gene_affected.upper()]["gene_id"]);
                                gene_symbol__list.append(_gene_info__dict[gene_affected.upper()]["gene_symbol"]);
                            else:
                                gene_affected__symbol__not_found_in_geneinfo__list.append(gene_affected);
                                gene_id__list.append("");
                                gene_symbol__list.append("");
                    """
                    LOGGER.info("====genes_affected__str is:'%s', oMIM_ID:%d, row_id:%d, genes_affected__str__transformed:'%s', gene_affected__list:'%s', gene_affected__csv:'%s', list_to_csv(gene_affected__list) is:'%s'"%(
                        genes_affected__str,int(oMIM_ID),int(row_id),genes_affected__str__transformed,gene_affected__list,gene_affected__csv,list_to_csv(gene_affected__list))
                    );
                    """;
                    ##gene_affected__csv=genes_affected__str__transformed;
                    gene_id__csv=list_to_csv(gene_id__list);
                    gene_symbol__csv=list_to_csv(gene_symbol__list);
                    #############
                    
                    ####here we include the list of uniprotkb_ids, we pair each gene_id to zero or one uniprotkb_id (start) 2019-10-29 1510hrs###############
                    uniprotkb_id__csv=None;
                    uniprotkb_id__list=[];
                    for gene_id in gene_id__list:
                        if(gene_id in _gene_id__2__uniprotkb_id__dict):
                            uniprotkb_id=_gene_id__2__uniprotkb_id__dict[gene_id]["uniprotkb_id"];
                            uniprotkb_id__list.append(uniprotkb_id);
                        else:
                            uniprotkb_id__list.append("");
                    uniprotkb_id__csv=list_to_csv(uniprotkb_id__list);
                    ####here we include the list of uniprotkb_ids, we pair each gene_id to zero or one uniprotkb_id (end) 2019-10-29 1517hrs###############
                    
                    ####here we include the list of uniprotkb_ids, we pair each uniprotkb_id to zero or one ko_id (start) 2019-10-29 1650rs###############
                    ko_id__csv=None;
                    ko_id__list=[];
                    for uniprotkb_id in uniprotkb_id__list:
                        if(uniprotkb_id in _uniprotkb_id__2__ko_id__dict):
                            ko_id=_uniprotkb_id__2__ko_id__dict[uniprotkb_id]["ko_id"];
                            ko_id__list.append(ko_id);
                        else:
                            ko_id__list.append("");
                    ko_id__csv=list_to_csv(ko_id__list);
                    ####here we include the list of uniprotkb_ids, we pair each gene_id to zero or one uniprotkb_id (end) 2019-10-29 1652hrs###############
                    
                    ####here we include the list of uniprotkb_ids, we pair each uniprotkb_id to zero or one ec_number (start) 2019-10-30 1104hrs###############
                    ec_number__csv2=None;
                    ec_number__list2=[];
                    for uniprotkb_id in uniprotkb_id__list:
                        if(uniprotkb_id in _uniprotkb_id__2__ec_number__dict):
                            ec_number=_uniprotkb_id__2__ec_number__dict[uniprotkb_id]["ec_number"];
                            ec_number__list2.append(ec_number);
                        else:
                            ec_number__list2.append("");
                    ec_number__csv2=list_to_csv(ec_number__list2);
                    ####here we include the list of uniprotkb_ids, we pair each gene_id to zero or one uniprotkb_id (end) 2019-10-30 1104hrs###############
                    
                    
                    
                    
                    
                    enzyme_or_protein_detected=row[6];#Enzyme or protein short name
                    enzyme_or_protein_detected__sha256=encrypt_string(enzyme_or_protein_detected);
                    ec_number=None;ec_number__list=[];ec_number__csv=None;
                    uniprot_ID=None;uniprot_ID__list=[];uniprot_ID__csv=None;
                    uniprotids_and_or_ecnumbers_gene_product=row[7];
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product.replace(" and ",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace(" or ",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace("+",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace("/",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace("(","");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace(")","");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace("+",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=re.sub("\s+", " ", uniprotids_and_or_ecnumbers_gene_product__transformed).strip();
                    uniprotids_and_or_ecnumbers_gene_product__transformed=uniprotids_and_or_ecnumbers_gene_product__transformed.replace(" ",",");
                    uniprotids_and_or_ecnumbers_gene_product__transformed=re.sub(",+", ",", uniprotids_and_or_ecnumbers_gene_product__transformed).strip();
                    
                    
                    
                    uniprotids_and_or_ecnumbers_gene_product__list=remove_empty_values_from_list(csv_to_list(uniprotids_and_or_ecnumbers_gene_product__transformed));
                    if(uniprotids_and_or_ecnumbers_gene_product__list!=None):
                        for uniprotids_and_or_ecnumbers_gene_product in uniprotids_and_or_ecnumbers_gene_product__list:
                            match=oRegPattern_ec_number.search(uniprotids_and_or_ecnumbers_gene_product);
                            if(match!=None and match.group(0)!=None):
                                ec_number=match.group("ec_number");
                                ec_number__list.append(ec_number);
                            else:
                                uniprot_ID=uniprotids_and_or_ecnumbers_gene_product;
                                uniprot_ID__list.append(uniprot_ID);
                        uniprot_ID__csv=list_to_csv(remove_empty_values_from_list(uniprot_ID__list));
                        ec_number__csv=list_to_csv(remove_empty_values_from_list(ec_number__list));
                    drug_formulation_dosage=row[8];#this column was introduced in the 2019-11-22.0032hrs version of the DDIEM dataset.
                    regimen_name=row[9];#this should be ignored and the regimen_name obtained from ontology resource via drug_ID should be used instead.
                    regimen_comments=row[10];
                    
                    drug_IDs__str__orig=row[11];
                    
                    """
    5,drug,Field 10 (J),drugbank_ID,DB00741,https://www.drugbank.ca/drugs/DB00741
    6,drug,Field 10 (J),chEBI_ID,ChEBI:28384,http://purl.obolibrary.org/obo/ChEBI_28384
    7,drug,Field 10 (J),WHOCC_ID,M01AX,https://www.whocc.no/atc_ddd_index/?code=M01AX
                    """
                    #drugbank_ID=None;chEBI_ID=None;wHOCC_ID=None;
                    drug_ID2=drug_IDs__str__orig.replace("+"," + ");
                    drug_ID2=drug_ID2.replace(" or"," or ");
                    drug_ID2=drug_ID2.replace("/"," / ");
                    drug_ID2=oRegPattern_whitespace.sub(" ",drug_ID2);
                    drug_ID2=drug_ID2.strip();
                    if(1==3 and drug_ID2=="NA"):
                        drug_ID2="";
                    if(len(drug_ID2)>0):
                        drug_ID2__sha256=encrypt_string(drug_ID2);
                    drug_ID_tmp="";
                    drug_ID_current=None;
                    drug_ID_operator_tmp=None;
                    drug_ID_operator_current=None;
                    drug_ID_operator_previous=None;
                    drug_ID_normalized="";
                    in_operator_section=False;
                    
                    #a="PubChem SID: 384573165";import re;re.sub(r"PubChem\s*((C|S|A)ID)\s*:\s*",r"PubChem\1:",a);
                    drug_ID2=re.sub(r"PubChem\s*((C|S|A)ID)\s*:\s*",r"PubChem\1:",drug_ID2);
                    regimen_decomposition__dict=compose_regimen(row_id, drug_ID2);
                    
                    c=regimen_decomposition__dict["c"];
                    drug_ID_tmp=regimen_decomposition__dict["drug_ID_tmp"];
                    
                    drug_ID__ORed__list=regimen_decomposition__dict["drug_ID__ORed__list"];
                    drug_ID_NA_position__ORed__list=[];
                    drug_ID_NA_position__ORed__csv=None;
                    if(drug_ID__ORed__list!=None):
                        drug_ID_ordinal_position=0;
                        for drug_ID in drug_ID__ORed__list:
                            drug_ID_ordinal_position+=1;
                            if(drug_ID.upper()=="NA"):
                                drug_ID_NA_position__ORed__list.append(drug_ID_ordinal_position);
                        drug_ID_NA_position__ORed__csv=list_to_csv(remove_empty_values_from_list(drug_ID_NA_position__ORed__list));
                    
                    drug_ID__ANDed__list=regimen_decomposition__dict["drug_ID__ANDed__list"];
                    drug_ID_NA_position__ANDed__list=[];
                    drug_ID_NA_position__ANDed__csv=None;
                    if(drug_ID__ANDed__list!=None):
                        drug_ID_ordinal_position=0;
                        for drug_ID in drug_ID__ANDed__list:
                            drug_ID_ordinal_position+=1;
                            if(drug_ID.upper()=="NA"):
                                drug_ID_NA_position__ANDed__list.append(drug_ID_ordinal_position);
                        drug_ID_NA_position__ANDed__csv=list_to_csv(remove_empty_values_from_list(drug_ID_NA_position__ANDed__list));
                    
                    
                    drug_ID_operator_current=regimen_decomposition__dict["drug_ID_operator_current"];
                    if(row_id=="52"):
                        pass;
                        #LOGGER.info("row_id:%s, c is:'%s', drug_ID_tmp is:'%s', drug_ID__ORed__list:'%s', drug_ID__ANDed__list:'%s', drug_ID_operator_current:'%s'"%(row_id,c,drug_ID_tmp,drug_ID__ORed__list,drug_ID__ANDed__list,drug_ID_operator_current));
                        #LOGGER.info("row_id:%s, drug_ID_tmp is:'%s'"%(row_id,drug_ID_tmp));
                        
                    #generate the various drug database drug_id lists that are to be ORed
                    drug_ID__ORed__csv=list_to_csv(remove_empty_values_from_list(drug_ID__ORed__list));
                    drug_ID__list=drug_ID__ORed__list;
                    grouped_drug_ids_by_database=group_drug_ids_by_database(
                        drug_ID__list
                    );
                    #LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>row_id is:{0}, drug_ID2 is:'{1}', drug_ID__list is:'{2}', grouped_drug_ids_by_database is:'{3}'".format(row_id,drug_ID2,json.dumps(drug_ID__list),json.dumps(grouped_drug_ids_by_database,indent=4)));
                    drugbank_ID__ORed__csv=grouped_drug_ids_by_database["drugbank_ID__csv"];
                    chEBI_ID__ORed__csv=grouped_drug_ids_by_database["chEBI_ID__csv"];
                    pubChem_CID__ORed__csv=grouped_drug_ids_by_database["pubChem_CID__csv"];
                    pubChem_SID__ORed__csv=grouped_drug_ids_by_database["pubChem_SID__csv"];
                    pubChem_AID__ORed__csv=grouped_drug_ids_by_database["pubChem_AID__csv"];
                    wHOCC_ID__ORed__csv=grouped_drug_ids_by_database["wHOCC_ID__csv"];
                    
                    #generate the various drug database drug_id lists that are to be ANDed
                    drug_ID__ANDed__csv=list_to_csv(remove_empty_values_from_list(drug_ID__ANDed__list));
                    drug_ID__list=drug_ID__ANDed__list;
                    grouped_drug_ids_by_database=group_drug_ids_by_database(
                        drug_ID__list
                    );
                    #LOGGER.info("===========================row_id is:{0}, drug_ID2 is:'{1}', drug_ID__list is:'{2}', grouped_drug_ids_by_database is:'{3}', _pubChem_CID_info__dict is:'{4}'".format(row_id,drug_ID2,json.dumps(drug_ID__list),json.dumps(grouped_drug_ids_by_database,indent=4),json.dumps(_pubChem_CID_info__dict,indent=4)));
                    drugbank_ID__ANDed__csv=grouped_drug_ids_by_database["drugbank_ID__csv"];
                    chEBI_ID__ANDed__csv=grouped_drug_ids_by_database["chEBI_ID__csv"];
                    pubChem_CID__ANDed__csv=grouped_drug_ids_by_database["pubChem_CID__csv"];
                    pubChem_SID__ANDed__csv=grouped_drug_ids_by_database["pubChem_SID__csv"];
                    pubChem_AID__ANDed__csv=grouped_drug_ids_by_database["pubChem_AID__csv"];
                    wHOCC_ID__ANDed__csv=grouped_drug_ids_by_database["wHOCC_ID__csv"];
                    
                    
                    pubChem_CID_name__ORed__csv=None;
                    pubChem_CID_name__ORed__list=[];
                    if(pubChem_CID__ORed__csv!=None):
                        pubChem_CID__ORed__list=csv_to_list(pubChem_CID__ORed__csv);
                        for pubChem_CID__ORed in pubChem_CID__ORed__list:
                            pubChem_CID__ORed2=pubChem_CID__ORed.upper().replace("PUBCHEM","");
                            #LOGGER.info("000000000000000000000row_id is:{0}, drug_ID2 is:'{1}', pubChem_CID__ORed is:'{2}', pubChem_CID__ORed2 is:'{3}', _pubChem_CID_info__dict is:'{4}'".format(row_id,drug_ID2,pubChem_CID__ORed,pubChem_CID__ORed2,json.dumps(_pubChem_CID_info__dict,indent=4)));
                            if(_pubChem_CID_info__dict!=None and pubChem_CID__ORed in _pubChem_CID_info__dict):
                                cmpdname=_pubChem_CID_info__dict[pubChem_CID__ORed]["cmpdname"];
                                #LOGGER.info("111111111111111111111row_id is:{0}, drug_ID2 is:'{1}', pubChem_CID__ORed is:'{2}' has been found as key in _pubChem_CID_info__dict is:'{3}', cmpdname is:'{4}'".format(row_id,drug_ID2,pubChem_CID__ORed,json.dumps(_pubChem_CID_info__dict,indent=4),cmpdname));
                                pubChem_CID_name__ORed__list.append(cmpdname);
                            else:
                                pubChem_CID_name__ORed__list.append(None);
                    pubChem_CID_name__ORed__csv=list_to_csv(pubChem_CID_name__ORed__list);
                    
                    pubChem_SID_name__ORed__csv=None;
                    pubChem_SID_name__ORed__list=[];
                    if(pubChem_SID__ORed__csv!=None):
                        pubChem_SID__ORed__list=csv_to_list(pubChem_SID__ORed__csv);
                        for pubChem_SID__ORed in pubChem_SID__ORed__list:
                            if(_pubChem_SID_info__dict!=None and pubChem_SID__ORed in _pubChem_SID_info__dict):
                                pubChem_SID_name__ORed__list.append(_pubChem_SID_info__dict[pubChem_SID__ORed.upper().replace("PUBCHEM","")]["cmpdname"]);
                            else:
                                pubChem_SID_name__ORed__list.append(None);
                    pubChem_SID_name__ORed__csv=list_to_csv(pubChem_SID_name__ORed__list);
                    
                    pubChem_AID_name__ORed__csv=None;
                    pubChem_AID_name__ORed__list=[];
                    if(pubChem_AID__ORed__csv!=None):
                        pubChem_AID__ORed__list=csv_to_list(pubChem_AID__ORed__csv);
                        for pubChem_AID__ORed in pubChem_AID__ORed__list:
                            if(_pubChem_AID_info__dict!=None and pubChem_AID__ORed in _pubChem_AID_info__dict):
                                pubChem_AID_name__ORed__list.append(_pubChem_AID_info__dict[pubChem_AID__ORed.upper().replace("PUBCHEM","")]["cmpdname"]);
                            else:
                                pubChem_AID_name__ORed__list.append(None);
                    pubChem_AID_name__ORed__csv=list_to_csv(pubChem_AID_name__ORed__list);
                    
                    
                    
                    pubChem_CID_name__ANDed__csv=None;
                    pubChem_CID_name__ANDed__list=[];
                    if(pubChem_CID__ANDed__csv!=None):
                        pubChem_CID__ANDed__list=csv_to_list(pubChem_CID__ANDed__csv);
                        for pubChem_CID__ANDed in pubChem_CID__ANDed__list:
                            #LOGGER.info("000000000000000000000row_id is:{0}, drug_ID2 is:'{1}', pubChem_CID__ANDed is:'{2}', _pubChem_CID_info__dict is:'{3}'".format(row_id,drug_ID2,pubChem_CID__ANDed,json.dumps(_pubChem_CID_info__dict,indent=4)));
                            if(_pubChem_CID_info__dict!=None and pubChem_CID__ANDed in _pubChem_CID_info__dict):
                                pubChem_CID_name__ANDed__list.append(_pubChem_CID_info__dict[pubChem_CID__ANDed.upper().replace("PUBCHEM","")]["cmpdname"]);
                            else:
                                pubChem_CID_name__ANDed__list.append(None);
                    pubChem_CID_name__ANDed__csv=list_to_csv(pubChem_CID_name__ANDed__list);
                    
                    pubChem_SID_name__ANDed__csv=None;
                    pubChem_SID_name__ANDed__list=[];
                    if(pubChem_SID__ANDed__csv!=None):
                        pubChem_SID__ANDed__list=csv_to_list(pubChem_SID__ANDed__csv);
                        for pubChem_SID__ANDed in pubChem_SID__ANDed__list:
                            if(_pubChem_SID_info__dict!=None and pubChem_SID__ANDed in _pubChem_SID_info__dict):
                                pubChem_SID_name__ANDed__list.append(_pubChem_SID_info__dict[pubChem_SID__ANDed.upper().replace("PUBCHEM","")]["cmpdname"]);
                            else:
                                pubChem_SID_name__ANDed__list.append(None);
                    pubChem_SID_name__ANDed__csv=list_to_csv(pubChem_SID_name__ANDed__list);
                    
                    pubChem_AID_name__ANDed__csv=None;
                    pubChem_AID_name__ANDed__list=[];
                    if(pubChem_AID__ANDed__csv!=None):
                        pubChem_AID__ANDed__list=csv_to_list(pubChem_AID__ANDed__csv);
                        for pubChem_AID__ANDed in pubChem_AID__ANDed__list:
                            if(_pubChem_AID_info__dict!=None and pubChem_AID__ANDed in _pubChem_AID_info__dict):
                                pubChem_AID_name__ANDed__list.append(_pubChem_AID_info__dict[pubChem_AID__ANDed.upper().replace("PUBCHEM","")]["cmpdname"]);
                            else:
                                pubChem_AID_name__ANDed__list.append(None);
                    pubChem_AID_name__ANDed__csv=list_to_csv(pubChem_AID_name__ANDed__list);
                    
                    
                    
                    
                    
                    
                    
                    
                    study_type_evidence_codes__str__orig=row[12];
                    study_type_evidence_codes__transformed=study_type_evidence_codes__str__orig.replace(" and ",",");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace(" or ",",");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace("+",",");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace("/",",");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace("(","");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace(")","");
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace("+",",");
                    study_type_evidence_codes__transformed=re.sub("\s+", " ", study_type_evidence_codes__transformed).strip();
                    study_type_evidence_codes__transformed=study_type_evidence_codes__transformed.replace(" ",",");
                    study_type_evidence_codes__transformed=re.sub(",+", ",", study_type_evidence_codes__transformed).strip();
                    
                    study_type_evidence_code__list=remove_empty_values_from_list(csv_to_list(study_type_evidence_codes__transformed));
                    #study_type_evidence_code__csv=list_to_csv(study_type_evidence_code__list);
                    
                    
                    
                    mutation_improved_by_treatment__list=row[13].split("\n");
                    mutation_not_improved_by_treatment__list=row[15].split("\n");
                    regimen_mechanism_of_action__list=row[17].split("/");
                    regimen_mechanism_of_action_abbreviation__list=row[18].split("/");
                    regimen_mechanism_of_action_ontology_category__list=row[19].split("/");
                    phenotype_improved_by_treatment__list=row[21].split("/");
                    if(len(phenotype_improved_by_treatment__list)>1):
                        #Found multiple phenotype_improved_by_treatments
                        #print the ommim_id and row_id
                        pass;
                    phenotype_improved_by_treatment_comments=row[22];
                    phenotype_ID__list=row[23].split("/");
                    if(treatment_manuscript_reference__list!=None):
                        del treatment_manuscript_reference__list[0:len(treatment_manuscript_reference__list)-1];
                    else:
                        treatment_manuscript_reference__list=[];
                    for i in range(24,32):
                        if(len(row[i])>0):
                            if(row[i]=='""' or row[i]=="''" or row[i]==""):
                                pass;
                                #do nothing
                                if(1==1 and row_cnt==3):
                                    LOGGER.info("row[%d] is:'%s'"%(i,json.dumps(row[i],indent=4)));
                            else:
                                treatment_manuscript_reference__list.append(row[i]);
                    
                    study_type_evidence_code__csv=list_to_csv(remove_empty_values_from_list(study_type_evidence_code__list));
                    mutation_improved_by_treatment__csv=list_to_csv(remove_empty_values_from_list(mutation_improved_by_treatment__list));
                    mutation_not_improved_by_treatment__csv=list_to_csv(remove_empty_values_from_list(mutation_not_improved_by_treatment__list));
                    regimen_mechanism_of_action__csv=list_to_csv(remove_empty_values_from_list(regimen_mechanism_of_action__list));
                    regimen_mechanism_of_action_abbreviation__csv=list_to_csv(remove_empty_values_from_list(regimen_mechanism_of_action_abbreviation__list));
                    regimen_mechanism_of_action_ontology_category__csv=list_to_csv(remove_empty_values_from_list(regimen_mechanism_of_action_ontology_category__list));
                    phenotype_improved_by_treatment__csv=list_to_csv(remove_empty_values_from_list(phenotype_improved_by_treatment__list));
                    phenotype_ID__csv=list_to_csv(remove_empty_values_from_list(phenotype_ID__list));
                    treatment_manuscript_reference__csv=list_to_csv(remove_empty_values_from_list(treatment_manuscript_reference__list));
                    iembase_id__csv=list_to_csv(remove_empty_values_from_list(iembase_id__list));
                    
                    
                    
                    clinical_log_rdf_base_fields_dataset_row__dict={
                        "row_id":row_id
                        ,"oMIM_ID":oMIM_ID
                        ,"oMIM_ID__via_disease_name":oMIM_ID__via_disease_name
                        ,"omim_number_prefix":omim_number_prefix
                        ,"omim_number":omim_number
                        ,"omim_title_preferred":omim_title_preferred
                        ,"omim_title_alternative":omim_title_alternative
                        ,"omim_title_included":omim_title_included
                        ,"disease_name":disease_name
                        ,"disease_comments":disease_comments
                        ,"gene_affected__orig":genes_affected__str
                        ,"gene_affected__csv":gene_affected__csv
                        ,"enzyme_or_protein_detected":enzyme_or_protein_detected
                        ,"enzyme_or_protein_detected__sha256":enzyme_or_protein_detected__sha256
                        ,"uniprotids_and_or_ecnumbers_gene_product__orig":uniprotids_and_or_ecnumbers_gene_product
                        ,"ec_number__csv":ec_number__csv
                        ,"uniprot_ID__csv":uniprot_ID__csv
                        ,"drug_formulation_dosage":drug_formulation_dosage#this column was introduced in the 2019-11-22.0032hrs version of the DDIEM dataset.
                        ,"regimen_name":regimen_name
                        ,"regimen_comments":regimen_comments
                        ,"drug_IDs__orig":drug_IDs__str__orig
                        ,"drug_ID2":drug_ID2
                        
                        ,"drug_ID2__sha256":drug_ID2__sha256
                        
                        ,"drug_ID__ORed__csv":drug_ID__ORed__csv
                        ,"drugbank_ID__ORed__csv":drugbank_ID__ORed__csv
                        ,"chEBI_ID__ORed__csv":chEBI_ID__ORed__csv
                        ,"wHOCC_ID__ORed__csv":wHOCC_ID__ORed__csv
                        
                        ,"drug_ID__ANDed__csv":drug_ID__ANDed__csv
                        ,"drugbank_ID__ANDed__csv":drugbank_ID__ANDed__csv
                        ,"chEBI_ID__ANDed__csv":chEBI_ID__ANDed__csv
                        ,"wHOCC_ID__ANDed__csv":wHOCC_ID__ANDed__csv
                        
                        ,"study_type_evidence_codes__orig":study_type_evidence_codes__str__orig
                        ,"study_type_evidence_code__csv":study_type_evidence_code__csv
                        ,"mutation_improved_by_treatment__csv":mutation_improved_by_treatment__csv
                        ,"mutation_not_improved_by_treatment__csv":mutation_not_improved_by_treatment__csv
                        ,"regimen_mechanism_of_action_ontology_category__csv":regimen_mechanism_of_action_ontology_category__csv#,"regimen_mechanism_of_action__csv":regimen_mechanism_of_action__csv
                        ,"regimen_mechanism_of_action_abbreviation__csv":regimen_mechanism_of_action_abbreviation__csv
                        ,"phenotype_improved_by_treatment__csv":phenotype_improved_by_treatment__csv
                        ,"phenotype_ID__csv":phenotype_ID__csv
                        ,"phenotype_improved_by_treatment_comments":phenotype_improved_by_treatment_comments
                        ,"treatment_manuscript_reference__csv":treatment_manuscript_reference__csv
                        ,"gene_id__csv":gene_id__csv
                        ,"gene_symbol__csv":gene_symbol__csv
                        ,"iembase_id__csv":iembase_id__csv
                        ,"uniprotkb_id__csv":uniprotkb_id__csv
                        ,"ko_id__csv":ko_id__csv
                        ,"ec_number__csv":ec_number__csv2
                        ,"pubChem_CID__ORed__csv":pubChem_CID__ORed__csv
                        ,"pubChem_CID_name__ORed__csv":pubChem_CID_name__ORed__csv
                        ,"pubChem_SID__ORed__csv":pubChem_SID__ORed__csv
                        ,"pubChem_SID_name__ORed__csv":pubChem_SID_name__ORed__csv
                        ,"pubChem_AID__ORed__csv":pubChem_AID__ORed__csv
                        ,"pubChem_AID_name__ORed__csv":pubChem_AID_name__ORed__csv
                        ,"pubChem_CID__ANDed__csv":pubChem_CID__ANDed__csv
                        ,"pubChem_CID_name__ANDed__csv":pubChem_CID_name__ANDed__csv
                        ,"pubChem_SID__ANDed__csv":pubChem_SID__ANDed__csv
                        ,"pubChem_SID_name__ANDed__csv":pubChem_SID_name__ANDed__csv
                        ,"pubChem_AID__ANDed__csv":pubChem_AID__ANDed__csv
                        ,"pubChem_AID_name__ANDed__csv":pubChem_AID_name__ANDed__csv
                        ,"drug_ID_NA_position__ORed__csv":drug_ID_NA_position__ORed__csv
                        ,"drug_ID_NA_position__ANDed__csv":drug_ID_NA_position__ANDed__csv
                    };
                    xml_data=None;
                    if(1==2):
                        ##generate the RDF/XML
                        dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name=os.path.join(_dest_dir_file_name,"%s"%(os.path.splitext(os.path.basename(_src_clinical_log_dataset_csv_file_name))[0]),"RDFXML","%s.clinical_log_rdf_base_fields_dataset_row_RDFXML__%d.xml"%(os.path.splitext(os.path.basename(_src_clinical_log_dataset_csv_file_name))[0],int(row_id)));
                        #construct the parent directory
                        
                        mkdir_p(os.path.abspath(os.path.join(dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name, os.pardir)));
                        xml_data=generate_XMLRDF(
                            clinical_log_rdf_base_fields_dataset_row__dict
                        );
                        ##Write the RDF/XML data to file having the path contained in the variable dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name
                        fh=open(dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name,"w");
                        fh.write(xml_data);
                        fh.flush();
                        fh.close();
                        fh=None;
                        """
                        here generate the commands to copy and paste into Virtuoso.
                        DB.DBA.RDF_LOAD_RDFXML_MT (file_to_string_output ('/local/data/development.minor/KAUST/BORG/raw_data/2019-05-27/BORG_DDIEM__clinical_logs.2019-05-27.1340hrs.collapsed/RDFXML/BORG_DDIEM__clinical_logs.2019-05-27.1340hrs.collapsed.clinical_log_rdf_base_fields_dataset_row_RDFXML__1.xml'), '', 'http://www.cbrc.kaust.edu.sa/DDIEM');
                        """
                        DB_DBA_RDF_LOAD_RDFXML_MT__cmd="DB.DBA.RDF_LOAD_RDFXML_MT (file_to_string_output ('%s'), '', 'http://www.cbrc.kaust.edu.sa/DDIEM');\n"%(dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name);
                        dest_DB_DBA_RDF_LOAD_RDFXML_MT__fh.write(DB_DBA_RDF_LOAD_RDFXML_MT__cmd);
                        DB_DBA_RDF_LOAD_RDFXML_MT__cmd=None;
                        
                        
                        dest_clinical_log_rdf_base_fields_dataset_row_RDFXML_file_name=None;
                    
                    clinical_log_rdf_base_fields_dataset_row=[
                        row_id
                        ,oMIM_ID
                        ,oMIM_ID__via_disease_name
                        ,omim_number_prefix
                        ,omim_number
                        ,omim_title_preferred
                        ,omim_title_alternative
                        ,omim_title_included
                        ,disease_name
                        ,disease_comments
                        ,genes_affected__str
                        ,gene_affected__csv
                        ,enzyme_or_protein_detected
                        ,enzyme_or_protein_detected__sha256
                        ,uniprotids_and_or_ecnumbers_gene_product
                        ,ec_number__csv
                        ,uniprot_ID__csv
                        ,drug_formulation_dosage#this column was introduced in the 2019-11-22.0032hrs version of the DDIEM dataset."
                        ,regimen_name
                        ,regimen_comments
                        ,drug_IDs__str__orig
                        ,drug_ID2
                        
                        ,drug_ID2__sha256
                        
                        ,drug_ID__ORed__csv
                        ,drugbank_ID__ORed__csv
                        ,chEBI_ID__ORed__csv
                        ,wHOCC_ID__ORed__csv
                        
                        ,drug_ID__ANDed__csv
                        ,drugbank_ID__ANDed__csv
                        ,chEBI_ID__ANDed__csv
                        ,wHOCC_ID__ANDed__csv
                        
                        ,study_type_evidence_codes__str__orig
                        ,study_type_evidence_code__csv
                        ,mutation_improved_by_treatment__csv
                        ,mutation_not_improved_by_treatment__csv
                        ,regimen_mechanism_of_action_ontology_category__csv#,regimen_mechanism_of_action__csv
                        ,regimen_mechanism_of_action_abbreviation__csv
                        ,phenotype_improved_by_treatment__csv
                        ,phenotype_ID__csv
                        ,phenotype_improved_by_treatment_comments
                        ,treatment_manuscript_reference__csv
                        ,gene_id__csv
                        ,gene_symbol__csv
                        ,iembase_id__csv
                        ,uniprotkb_id__csv
                        ,ko_id__csv
                        ,ec_number__csv2
                        ,pubChem_CID__ORed__csv
                        ,pubChem_CID_name__ORed__csv
                        ,pubChem_SID__ORed__csv
                        ,pubChem_SID_name__ORed__csv
                        ,pubChem_AID__ORed__csv
                        ,pubChem_AID_name__ORed__csv
                        ,pubChem_CID__ANDed__csv
                        ,pubChem_CID_name__ANDed__csv
                        ,pubChem_SID__ANDed__csv
                        ,pubChem_SID_name__ANDed__csv
                        ,pubChem_AID__ANDed__csv
                        ,pubChem_AID_name__ANDed__csv
                        ,drug_ID_NA_position__ORed__csv
                        ,drug_ID_NA_position__ANDed__csv
                        ,xml_data
                    ];
                    dest_dataset_csv_writer.writerow(clinical_log_rdf_base_fields_dataset_row);
                    drug_ID2=None;
                    drug_ID__list=None;
                    """
                    drug_ID_normalized=None;
                    drug_ID_logical_operator__dict=None;
                    drug_ID__ORed__list=None;
                    drug_ID__ANDed__list=None;
                    
                    drugbank_ID=None;
                    drugbank_ID__list=None;
                    drugbank_ID__csv=None;
                    chEBI_ID=None;
                    chEBI_ID__list=None;
                    chEBI_ID__csv=None;
                    wHOCC_ID=None;
                    wHOCC_ID__list=None;
                    wHOCC_ID__csv=None;
                    """;
                    drug_formulation_dosage=None;
                    drug_ID2__sha256=None;
                    drug_ID__ORed__list=None;
                    drug_ID__ORed__csv=None;
                    drug_ID_NA_position__ORed__list=None;
                    drug_ID_NA_position__ORed__csv=None;
                    drugbank_ID__ORed__csv=None;
                    chEBI_ID__ORed__csv=None;
                    wHOCC_ID__ORed__csv=None;
                    
                    drug_ID__ANDed__list=None;
                    drug_ID__ANDed__csv=None;
                    drug_ID_NA_position__ANDed__list=None;
                    drug_ID_NA_position__ANDed__csv=None;
                    drugbank_ID__ANDed__csv=None;
                    chEBI_ID__ANDed__csv=None;
                    wHOCC_ID__ANDed__csv=None;
                    
                    disease_name=None;
                    disease_comment=None;
                    regimen_name=None;
                    regimen_comment=None;
                    phenotype_improved_by_treatment_comment=None;
                    
                    
            #del row2[0:len(row2)-1];
    dest_DB_DBA_RDF_LOAD_RDFXML_MT__fh.close();
    dest_dataset_csv_fh.close();
    src_dataset_csv_fh.close();
    
    dest_DB_DBA_RDF_LOAD_RDFXML_MT__fh=None;
    dest_dataset_csv_fh=None;
    src_dataset_csv_fh=None;
    
    gene_affected__symbol__found_in_geneinfo__list=list(set(remove_empty_values_from_list(gene_affected__symbol__found_in_geneinfo__list)));gene_affected__symbol__found_in_geneinfo__list.sort(reverse=False);
    gene_affected__symbol__not_found_in_geneinfo__list=list(set(remove_empty_values_from_list(gene_affected__symbol__not_found_in_geneinfo__list)));gene_affected__symbol__not_found_in_geneinfo__list.sort(reverse=False);

    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>gene_affected__symbol__found_in_geneinfo__list is:'%s'"%(json.dumps(gene_affected__symbol__found_in_geneinfo__list,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>gene_affected__symbol__not_found_in_geneinfo__list is:'%s'"%(json.dumps(gene_affected__symbol__not_found_in_geneinfo__list,indent=4)));

    task_completion_time_obj=datetime.datetime.now();
    task_completion_time_str="%s"%(task_completion_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f'));
    duration_obj=task_completion_time_obj-task_commencement_time_obj;
    duration_ms=duration_obj.total_seconds()*1000;
    
    processing_outcome__dict["task_commencement_time_str"]=task_commencement_time_str;
    processing_outcome__dict["task_completion_time_str"]=task_completion_time_str;
    processing_outcome__dict["duration_ms"]=duration_ms;
    
    processing_outcome__dict["hostname"]=hostname;
    processing_outcome__dict["ipAddress"]=ipAddress;
    processing_outcome__dict["ppid"]=ppid;
    processing_outcome__dict["pid"]=pid;
    processing_outcome__dict["task_id"]=task_id;
    processing_outcome__dict["task_formulation_timestamp_str"]=task_formulation_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f');
    processing_outcome__dict["worker_id"]=worker_id;
    processing_outcome__dict["worker_number"]=worker_number;
    processing_outcome__dict["src_clinical_log_dataset_csv_file_name"]=src_clinical_log_dataset_csv_file_name;
    processing_outcome__dict["dest_dataset_csv_file_name"]=dest_dataset_csv_file_name;
    processing_outcome__dict["cnt_of_fields__max"]=cnt_of_fields__max;
    
    
    
    #LOGGER.info("OMIM_mimTitles_dict is:'%s'"%(json.dumps(OMIM_mimTitles_dict,indent=4)));
    LOGGER.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>dest_dataset_csv_file_name is:'%s'"%(dest_dataset_csv_file_name));
    return processing_outcome__dict;
    
def generate_XMLRDF(
    clinical_log_rdf_base_fields_dataset_row__dict
):
    #xml.etree.ElementTree;
    """
from xml.etree import ElementTree as ET

# build a tree structure
#https://stackoverflow.com/questions/8868248/how-to-create-doctype-with-pythons-celementtree
ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#");
ET.register_namespace("ddiemterms", "http://www.cbrc.kaust.edu.sa/ddiem/terms/");
#root = ET.Element("{http://www.company.com}STUFF");
rdf_RDF = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF");
#rdf_Description = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description",attrib={"rdf:about":"https://www.omim.org/entry/219800"});
rdf_Description = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
rdf_Description.set("rdf:about","https://www.omim.org/entry/219800");
ddiemterms_BORG_DDIEM__clinical_logs__version = ET.SubElement(rdf_Description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}BORG_DDIEM__clinical_logs__version");
ddiemterms_BORG_DDIEM__clinical_logs__version.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/dataset/BORG_DDIEM__clinical_logs.2019-05-27.1340hrs");

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(rdf_RDF);

doc_type = '<?xml version="1.0" encoding="UTF-8"?>' \
       '<!DOCTYPE rdf:RDF [<!ENTITY xsd "http://www.w3.org/2001/XMLSchema#">]>'
tostring = ET.tostring(rdf_RDF).decode('utf-8');
import io;
str_io = io.StringIO();
file_data = f"{doc_type}{tostring}";
str_io.write(file_data);
xml_data=str_io.getvalue();
str_io=None;
print(xml_data);
    """
    
    BORG_DDIEM__relational_ontology="""
id    Subject    Predicate label    Predicate    Object    Object description
1    disease    has_abbreviation    http://bio2vec.net/has_abbreviation    disease_abbreviation    
2    disease    has_synonym    http://bio2vec.net/has_synonym    disease_synonym    
3    disease    has_name    http://bio2vec.net/has_name    disease_name    
4    disease    has_id    http://bio2vec.net/has_id    omim_id    
5    disease    disease_has_basis_in_dysfunction    http://purl.obolibrary.org/obo/RO_0004020    gene    
6    disease    is_treated_by_substance    http://purl.obolibrary.org/obo/RO_0002302    treatment    
7    disease    has_corrected_phenotype    http://bio2vec.net/has_corrected_phenotype    phenotype    
8    gene    has_abbreviation    http://bio2vec.net/has_abbreviation    gene_abbreviation    
9    gene    has_synonym    http://bio2vec.net/has_synonym    gene_synonym    
10    gene    has_name    http://bio2vec.net/has_name    gene_name    
11    gene    has_id    http://bio2vec.net/has_id    entrez_gene_id    
12    gene    has_mutation    http://bio2vec.net/has_mutation    mutation    
13    gene    has_gene_product    http://purl.obolibrary.org/obo/RO_0002205    enzyme    EC number/Protein Entry
14    enzyme    has_id    http://bio2vec.net/has_id    expasy or uniprot_id    expasy or uniprot_id
15    phenotype    has_synonym    http://bio2vec.net/has_synonym    phenotype_synonym    
16    phenotype    has_name    http://bio2vec.net/has_name    phenotype_name    
17    phenotype    has_id    http://bio2vec.net/has_id    HP/MP/NA (not available)    HP/MP/NA (not available)
                    
                    
20    drug    has_study_type    http://bio2vec.net/has_study_type    study_type    
21    drug    has_mechanism    http://bio2vec.net/has_mechanism    treatment_mechanism    
22    drug    has_abbreviation    http://bio2vec.net/has_abbreviation    drug_abbreviation    
23    drug    has_synonym    http://bio2vec.net/has_synonym    drug_synonym    
24    drug    has_name    http://bio2vec.net/has_name    regimen_name    
    drug_set    has_drugs_as_elements    http://bio2vec.net/has_drugs_as_elements    drugs    
    regimen    consists_of_            
                    
28    reference    has_name    http://bio2vec.net/has_name    source_name    pubmed/sciencedirect/clinical trials
29    treatment    mutation_improved_by_treatment    http://bio2vec.net/mutation_improved_by_treatment    mutation    literal
31    treatment    mutation_not_improved_by_treatment    http://bio2vec.net/failed_in_treatingmutation_not_improved_by_treatment    mutation    literal
32    treatment    treatment_mechanism_of_action    http://bio2vec.net/treatment_mechanism_of_action    mutation    literal
33    treatment    treatment_mechanism_of_action_abbreviation    http://bio2vec.net/treatment_mechanism_of_action_abbreviation    mutation    literal
34    treatment    phenotypes_improved    http://bio2vec.net/phenotypes_improved    phenotype    
18    regimen    is_substance_that_treats    http://purl.obolibrary.org/obo/RO_0002606    phenotype    
19    treatment    has_evidence_in    http://bio2vec.net/has_evidence_in    reference    
25    treatment    failed_in_treating    http://bio2vec.net/failed_in_treating    mutation        
26    treatment    treated_mutation    http://bio2vec.net/treated_mutation    mutation    
27    treatment    has_id    http://bio2vec.net/has_id    treatment_id    drug_bank/CHEBI/WHO
    
""";

    from xml.etree import ElementTree as ET;
    
    # build a tree structure
    #https://stackoverflow.com/questions/8868248/how-to-create-doctype-with-pythons-celementtree
    ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#");
    ET.register_namespace("purl", "http://purl.obolibrary.org/obo/");
    ET.register_namespace("ddiemterms", "http://www.cbrc.kaust.edu.sa/ddiem/terms/");
    rdf_RDF = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF");
    
    clinical_outcome_log_entry = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
    clinical_outcome_log_entry.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/dataset/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["row_id"]));
    row_id_entry = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_row_id");
    row_id_entry.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#integer");
    if(clinical_log_rdf_base_fields_dataset_row__dict["row_id"]!=None):
        pass;
        row_id_entry.text="%d"%(int(clinical_log_rdf_base_fields_dataset_row__dict["row_id"]));
    row_id_entry = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}clinical_outcome_log_id");
    row_id_entry.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#integer");
    if(clinical_log_rdf_base_fields_dataset_row__dict["row_id"]!=None):
        pass;
        row_id_entry.text="%d"%(int(clinical_log_rdf_base_fields_dataset_row__dict["row_id"]));
        #clinical_outcome_log_id
    
    
    ddiemterms_BORG_DDIEM__clinical_logs__version = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}BORG_DDIEM__clinical_logs__version");
    ddiemterms_BORG_DDIEM__clinical_logs__version.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/dataset/BORG_DDIEM__clinical_logs.2019-05-27.1340hrs");
    
    omim_id_entry = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_id");
    omim_id_entry.set("rdf:resource","https://www.omim.org/entry/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["oMIM_ID"]));
    #omim_entry = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description",attrib={"rdf:about":"https://www.omim.org/entry/219800"});
    omim_entry = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
    omim_entry.set("rdf:about","https://www.omim.org/entry/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["oMIM_ID"]));
    
    ddiemterms_omim_id = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_id");
    ddiemterms_omim_id.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#integer");
    #ddiemterms_omim_id.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["oMIM_ID"]!=None):
        pass;
        ddiemterms_omim_id.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["oMIM_ID"]);
        
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_disease_name");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["disease_name"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["disease_name"]);
        
        
    ############
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_number_prefix");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["omim_number_prefix"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["omim_number_prefix"]);
        
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_number");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["omim_number"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["omim_number"]);
        
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_title_preferred");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_preferred"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_preferred"]);
        
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_title_alternative");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_alternative"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_alternative"]);
        
    ddiemterms_disease_name = ET.SubElement(omim_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_omim_title_included");
    ddiemterms_disease_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    #ddiemterms_disease_name.text="ABC";
    if(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_included"]!=None):
        pass;
        ddiemterms_disease_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["omim_title_included"]);
    ############
    
    if(1==1):
        if(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"]!=None and len(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"].strip())>0):
            #This means there is a regimen for this entry.
            ddiemterms_regimen = ET.SubElement(clinical_outcome_log_entry, "{http://purl.obolibrary.org/obo/}RO_0002302");
            ddiemterms_regimen.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/regimen/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"]));
            
    if(clinical_log_rdf_base_fields_dataset_row__dict["study_type_evidence_code__csv"]!=None and len(clinical_log_rdf_base_fields_dataset_row__dict["study_type_evidence_code__csv"])>0):
        has_study_type_evidence_code = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_study_type_evidence_code");
        has_study_type_evidence_code.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        has_study_type_evidence_code.text="true";
    
    if(clinical_log_rdf_base_fields_dataset_row__dict["study_type_evidence_code__csv"]!=None):
        #ddiemterms_study_type_evidence_code__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}study_type_evidence_code__collection");
        #ddiemterms_study_type_evidence_code__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/study_type_evidence_code__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["study_type_evidence_code__csv"])));
        ddiemterms_study_type_evidence_code__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}study_type_evidence_code__collection");
        ddiemterms_study_type_evidence_code__collection.set("rdf:parseType","Collection");
        
        study_type_evidence_code__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["study_type_evidence_code__csv"]));
        if(study_type_evidence_code__list!=None):
            for study_type_evidence_code in study_type_evidence_code__list:
                ddiemterms_study_type_evidence_code = ET.SubElement(ddiemterms_study_type_evidence_code__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                ddiemterms_study_type_evidence_code.set("rdf:about","http://purl.obolibrary.org/obo/%s"%(study_type_evidence_code.replace("ECO:","ECO_")));
        
    #regimen_mechanism_of_action_abbreviation__csv
    if(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action_abbreviation__csv"]!=None):
        #ddiemterms_regimen_mechanism_of_action_abbreviation__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action_abbreviation__collection");
        #ddiemterms_regimen_mechanism_of_action_abbreviation__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action_abbreviation__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action_abbreviation__csv"])));
        ddiemterms_regimen_mechanism_of_action_abbreviation__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action_abbreviation__collection");
        ddiemterms_regimen_mechanism_of_action_abbreviation__collection.set("rdf:parseType","Collection");
        
        regimen_mechanism_of_action_abbreviation__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action_abbreviation__csv"]));
        if(regimen_mechanism_of_action_abbreviation__list!=None):
            for regimen_mechanism_of_action_abbreviation in regimen_mechanism_of_action_abbreviation__list:
                ddiemterms_regimen_mechanism_of_action_abbreviation = ET.SubElement(ddiemterms_regimen_mechanism_of_action_abbreviation__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                ddiemterms_regimen_mechanism_of_action_abbreviation.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/%s"%(regimen_mechanism_of_action_abbreviation));
                
    """
    #regimen_mechanism_of_action__csv
    if(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"]!=None):
        #ddiemterms_regimen_mechanism_of_action__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action__collection");
        #ddiemterms_regimen_mechanism_of_action__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"])));
        ddiemterms_regimen_mechanism_of_action__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action__collection");
        ddiemterms_regimen_mechanism_of_action__collection.set("rdf:parseType","Collection");
        
        regimen_mechanism_of_action__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"]));
        if(regimen_mechanism_of_action__list!=None):
            for regimen_mechanism_of_action in regimen_mechanism_of_action__list:
                #ddiemterms_regimen_mechanism_of_action = ET.SubElement(ddiemterms_regimen_mechanism_of_action__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                #ddiemterms_regimen_mechanism_of_action.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/%s"%(regimen_mechanism_of_action));
                #regimen_mechanism_of_action
                ddiemterms_regimen_mechanism_of_action = ET.SubElement(ddiemterms_regimen_mechanism_of_action__collection, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action");
                ddiemterms_regimen_mechanism_of_action.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                ddiemterms_regimen_mechanism_of_action.text="%s"%(regimen_mechanism_of_action);
    """
    if(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"]!=None):
        #ddiemterms_regimen_mechanism_of_action__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}regimen_mechanism_of_action__collection");
        #ddiemterms_regimen_mechanism_of_action__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"])));
        ddiemterms_regimen_mechanism_of_action__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_regimen_mechanism_of_action__bag");
        #ddiemterms_regimen_mechanism_of_action__collection.set("rdf:parseType","Collection");
        ddiemterms_regimen_mechanism_of_action__bag = ET.SubElement(ddiemterms_regimen_mechanism_of_action__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag");
        
        regimen_mechanism_of_action__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["regimen_mechanism_of_action__csv"]));
        if(regimen_mechanism_of_action__list!=None):
            for regimen_mechanism_of_action in regimen_mechanism_of_action__list:
                #ddiemterms_regimen_mechanism_of_action = ET.SubElement(ddiemterms_regimen_mechanism_of_action__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                #ddiemterms_regimen_mechanism_of_action = ET.SubElement(ddiemterms_regimen_mechanism_of_action__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag");
                ddiemterms_regimen_mechanism_of_action=ET.SubElement(ddiemterms_regimen_mechanism_of_action__bag, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li");
                ddiemterms_regimen_mechanism_of_action.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                ddiemterms_regimen_mechanism_of_action.text="%s"%(regimen_mechanism_of_action);
        
    
    if(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_ID__csv"]!=None):
        #ddiemterms_phenotype_ID__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}phenotype_ID__collection");
        #ddiemterms_phenotype_ID__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/phenotype_ID__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_ID__csv"])));
        ddiemterms_phenotype_ID__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_phenotype_ID__collection");
        ddiemterms_phenotype_ID__collection.set("rdf:parseType","Collection");
        
        phenotype_ID__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_ID__csv"]));
        if(phenotype_ID__list!=None):
            for phenotype_ID in phenotype_ID__list:
                match=oRegPattern_phenotype_ID.search(phenotype_ID);
                if(match!=None and match.group(0)!=None):
                    phenotype_ID2=None;
                    phenotype_ID2_is_superclass=None;
                    phenotype_ID2=match.group("phenotype_ID");
                    phenotype_ID2_is_superclass=match.group("phenotype_ID_is_superclass");
                    ddiemterms_phenotype_ID = ET.SubElement(ddiemterms_phenotype_ID__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                    ddiemterms_phenotype_ID.set("rdf:about","http://purl.obolibrary.org/obo/%s"%(phenotype_ID2.replace("HP:","HP_")));
                    ddiemterms_phenotype_ID_is_superclass=ET.SubElement(ddiemterms_phenotype_ID,"{http://www.cbrc.kaust.edu.sa/ddiem/terms/}is_superclass");
                    ddiemterms_phenotype_ID_is_superclass.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#boolean");
                    if(len(match.group("phenotype_ID_is_superclass"))>0):
                        ddiemterms_phenotype_ID_is_superclass.text="%s"%("true");
                    else:
                        ddiemterms_phenotype_ID_is_superclass.text="%s"%("false");
                    phenotype_ID2=None;
                    phenotype_ID2_is_superclass=None;
                    
    if(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]!=None):
        #ddiemterms_phenotype_improved_by_treatment__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_phenotype_improved_by_treatment__bag");
        ddiemterms_gene_affected = ET.SubElement(clinical_outcome_log_entry, "{http://purl.obolibrary.org/obo/}RO_0004020");
        ddiemterms_gene_affected.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/genes/ghr.nlm.nih.gov/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
        
        ddiemterms_gene_affected__description = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
        ddiemterms_gene_affected__description.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/genes/ghr.nlm.nih.gov/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
        ddiemterms_gene_affected__description__gene_id = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}gene_id");
        ddiemterms_gene_affected__description__gene_id.set("rdf:resource","https://ghr.nlm.nih.gov/gene/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
        ddiemterms_gene_affected__description__has_abbreviation = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_abbreviation");
        ddiemterms_gene_affected__description__has_abbreviation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_abbreviation.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_synonym = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_synonym");
        ddiemterms_gene_affected__description__has_synonym.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_synonym.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_name = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_name");
        ddiemterms_gene_affected__description__has_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_id = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_id");
        ddiemterms_gene_affected__description__has_id.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_id.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_mutation = ET.SubElement(ddiemterms_gene_affected__description, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_mutation");
        ddiemterms_gene_affected__description__has_mutation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_mutation.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        if(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]!=None):
            ddiemterms_gene_affected__description__R0_0002205 = ET.SubElement(ddiemterms_gene_affected__description, "{http://purl.obolibrary.org/obo/}RO_0002205");
            ddiemterms_gene_affected__description__R0_0002205.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/EC/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]));
            
        if(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]!=None):
            ddiemterms_gene_affected__description__R0_0002205 = ET.SubElement(ddiemterms_gene_affected__description, "{http://purl.obolibrary.org/obo/}RO_0002205");
            ddiemterms_gene_affected__description__R0_0002205.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/uniprot_ID/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]));
            
    #enzyme_or_protein_detected
    if(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected"]!=None):
        ddiemterms_has_enzyme_or_protein_detected = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_enzyme_or_protein_detected");
        ddiemterms_has_enzyme_or_protein_detected.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/has_enzyme_or_protein_detected/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected__sha256"]));
    
            
    #enzyme_or_protein_detected
    enzyme_or_protein_detected=None;
    if(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected"]!=None):
        clinical_outcome_log_entry2 = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
        clinical_outcome_log_entry2.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/has_enzyme_or_protein_detected/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected__sha256"]));
        ddiemterms_has_enzyme_or_protein_detected = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_enzyme_or_protein_detected");
        ddiemterms_has_enzyme_or_protein_detected.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_has_enzyme_or_protein_detected.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected"]);
        """
        if(clinical_log_rdf_base_fields_dataset_row__dict["enzyme_or_protein_detected"] is enzyme):
            ddiemterms_gene_product_type = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}enzyme_or_protein_detected_type");
            ddiemterms_gene_product_type.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
            ddiemterms_gene_product_type.text="enzyme";
        """;
        
    ec_number=None;
    if(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]!=None):
        clinical_outcome_log_entry2 = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
        clinical_outcome_log_entry2.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/EC/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]));
        ddiemterms_has_ec_number = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_ec_number");
        ddiemterms_has_ec_number.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_has_ec_number.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]);
        ddiemterms_gene_product_type = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}gene_product_type");
        ddiemterms_gene_product_type.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_product_type.text="EC_number";
        
    uniprot_ID=None;
    if(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]!=None):
        clinical_outcome_log_entry2 = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
        clinical_outcome_log_entry2.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/uniprot_ID/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]));
        ddiemterms_has_uniprot_ID = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_uniprot_ID");
        ddiemterms_has_uniprot_ID.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_has_uniprot_ID.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]);
        ddiemterms_gene_product_type = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}gene_product_type");
        ddiemterms_gene_product_type.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_product_type.text="uniprot_ID";
        
                
        
    if(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_improved_by_treatment__csv"]!=None):
        #ddiemterms_phenotype_improved_by_treatment__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}phenotype_improved_by_treatment__collection");
        #ddiemterms_phenotype_improved_by_treatment__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/phenotype_improved_by_treatment__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_improved_by_treatment__csv"])));
        ddiemterms_phenotype_improved_by_treatment__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_phenotype_improved_by_treatment__bag");
        #ddiemterms_phenotype_improved_by_treatment__collection.set("rdf:parseType","Collection");
        ddiemterms_phenotype_improved_by_treatment__bag = ET.SubElement(ddiemterms_phenotype_improved_by_treatment__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag");
        
        phenotype_improved_by_treatment__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_improved_by_treatment__csv"]));
        if(phenotype_improved_by_treatment__list!=None):
            for phenotype_improved_by_treatment in phenotype_improved_by_treatment__list:
                #ddiemterms_phenotype_improved_by_treatment = ET.SubElement(ddiemterms_phenotype_improved_by_treatment__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                #ddiemterms_phenotype_improved_by_treatment = ET.SubElement(ddiemterms_phenotype_improved_by_treatment__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag");
                ddiemterms_phenotype_improved_by_treatment=ET.SubElement(ddiemterms_phenotype_improved_by_treatment__bag, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li");
                ddiemterms_phenotype_improved_by_treatment.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                ddiemterms_phenotype_improved_by_treatment.text="%s"%(phenotype_improved_by_treatment);
                
    """
    #phenotype_improved_by_treatment_comments
    phenotype_improved_by_treatment_comments = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_comment");
    phenotype_improved_by_treatment_comments.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
    if(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_improved_by_treatment_comments"]!=None):
        pass;
        phenotype_improved_by_treatment_comments.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["phenotype_improved_by_treatment_comments"]);
    """        
        
    if(clinical_log_rdf_base_fields_dataset_row__dict["treatment_manuscript_reference__csv"]!=None):
        #ddiemterms_treatment_manuscript_reference__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}treatment_manuscript_reference__collection");
        #ddiemterms_treatment_manuscript_reference__collection.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/treatment_manuscript_reference__collection/%s"%(encrypt_string(clinical_log_rdf_base_fields_dataset_row__dict["treatment_manuscript_reference__csv"])));
        ddiemterms_treatment_manuscript_reference__collection = ET.SubElement(clinical_outcome_log_entry, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}treatment_manuscript_reference__collection");
        ddiemterms_treatment_manuscript_reference__collection.set("rdf:parseType","Collection");
        
        treatment_manuscript_reference__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["treatment_manuscript_reference__csv"]));
        if(treatment_manuscript_reference__list!=None):
            for treatment_manuscript_reference in treatment_manuscript_reference__list:
                ddiemterms_treatment_manuscript_reference = ET.SubElement(ddiemterms_treatment_manuscript_reference__collection, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                ddiemterms_treatment_manuscript_reference.set("rdf:about","%s"%(treatment_manuscript_reference));
    ##end of first description
    
    
    if(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"]!=None and len(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"].strip())>0):
        #This means there is a regimen for this entry.
        drugbank_ID__list=[];
        chEBI_ID__list=[];
        wHOCC_ID__list=[];
        
        """
        Now we generate the description of this regimen
        """
        if(1==1):
            ddiemterms_regimen = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
            ddiemterms_regimen.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/regimen/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["drug_ID2__sha256"]));
            
            
            ##one drug from set (start) 2019-06-09 1030hrs
            ddiemterms_consistsOf = ET.SubElement(ddiemterms_regimen, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}consistsOf");
            ddiemterms_DrugAlternative = ET.SubElement(ddiemterms_consistsOf, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}DrugAlternative");
            #drugbank_ID__ORed__csv
            drugbank_ID__ORed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["drugbank_ID__ORed__csv"]));
            if(drugbank_ID__ORed__list!=None):
                drugbank_ID__list.extend(drugbank_ID__ORed__list);
                for drugbank_ID__ORed in drugbank_ID__ORed__list:
                    ddiemterms_option = ET.SubElement(ddiemterms_DrugAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}option");
                    ddiemterms_option.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/drugbank/%s"%(drugbank_ID__ORed));
            #chEBI_ID__ORed__csv
            chEBI_ID__ORed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["chEBI_ID__ORed__csv"]));
            if(chEBI_ID__ORed__list!=None):
                chEBI_ID__list.extend(chEBI_ID__ORed__list);
                for chEBI_ID__ORed in chEBI_ID__ORed__list:
                    ddiemterms_option = ET.SubElement(ddiemterms_DrugAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}option");
                    ddiemterms_option.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/chEBI/%s"%(chEBI_ID__ORed));
            #wHOCC_ID__ORed__csv
            wHOCC_ID__ORed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["wHOCC_ID__ORed__csv"]));
            if(wHOCC_ID__ORed__list!=None):
                wHOCC_ID__list.extend(wHOCC_ID__ORed__list);
                for wHOCC_ID__ORed in wHOCC_ID__ORed__list:
                    ddiemterms_option = ET.SubElement(ddiemterms_DrugAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}option");
                    ddiemterms_option.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/wHOCC/%s"%(wHOCC_ID__ORed));
            ##one drug from set (end) 2019-06-09 1100hrs
            
            
            ##all drugs from set (start) 2019-06-09 1101hrs
            ddiemterms_consistsOf = ET.SubElement(ddiemterms_regimen, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}consistsOf");
            ddiemterms_DrugNonAlternative = ET.SubElement(ddiemterms_consistsOf, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}DrugNonAlternative");
            #drugbank_ID__ANDed__csv
            drugbank_ID__ANDed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["drugbank_ID__ANDed__csv"]));
            if(drugbank_ID__ANDed__list!=None):
                drugbank_ID__list.extend(drugbank_ID__ANDed__list);
                for drugbank_ID__ANDed in drugbank_ID__ANDed__list:
                    ddiemterms_nonoptional = ET.SubElement(ddiemterms_DrugNonAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}nonoptional");
                    ddiemterms_nonoptional.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/drugbank/%s"%(drugbank_ID__ANDed));
            #chEBI_ID__ANDed__csv
            chEBI_ID__ANDed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["chEBI_ID__ANDed__csv"]));
            if(chEBI_ID__ANDed__list!=None):
                chEBI_ID__list.extend(chEBI_ID__ANDed__list);
                for chEBI_ID__ANDed in chEBI_ID__ANDed__list:
                    ddiemterms_nonoptional = ET.SubElement(ddiemterms_DrugNonAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}nonoptional");
                    ddiemterms_nonoptional.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/chEBI/%s"%(chEBI_ID__ANDed));
            #wHOCC_ID__ANDed__csv
            wHOCC_ID__ANDed__list=remove_empty_values_from_list(csv_to_list(clinical_log_rdf_base_fields_dataset_row__dict["wHOCC_ID__ANDed__csv"]));
            if(wHOCC_ID__ANDed__list!=None):
                wHOCC_ID__list.extend(wHOCC_ID__ANDed__list);
                for wHOCC_ID__ANDed in wHOCC_ID__ANDed__list:
                    ddiemterms_nonoptional = ET.SubElement(ddiemterms_DrugNonAlternative, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}nonoptional");
                    ddiemterms_nonoptional.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/drugs/wHOCC/%s"%(wHOCC_ID__ANDed));
            ##all drugs from set (end) 2019-06-09 1103hrs
            
            
            #Now expound on the drugs
            ##drugbank drugs (start) 2019-06-09 1138hrs
            if(drugbank_ID__list!=None):
                drugbank_ID__list=list(set(drugbank_ID__list));
                for drugbank_ID in drugbank_ID__list:
                    ddiemterms_drugbank = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                    ddiemterms_drugbank.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/drugs/drugbank/%s"%(drugbank_ID));
                    ddiemterms_drugbank_ID = ET.SubElement(ddiemterms_drugbank, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}drugbank_ID");
                    ddiemterms_drugbank_ID.set("rdf:resource","https://www.drugbank.ca/drugs/%s"%(drugbank_ID));
                    
                    #drug_id_database_name
                    ddiemterms_drug_id_database_name = ET.SubElement(ddiemterms_drugbank, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}drug_id_database_name");
                    ddiemterms_drug_id_database_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_drug_id_database_name.text="drugbank";
                    
                    #has_abbreviation
                    ddiemterms_has_abbreviation = ET.SubElement(ddiemterms_drugbank, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_abbreviation");
                    ddiemterms_has_abbreviation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_abbreviation.text="%s"%(drugbank_ID);
                    
                    #has_synonym
                    ddiemterms_has_synonym = ET.SubElement(ddiemterms_drugbank, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_synonym");
                    ddiemterms_has_synonym.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_synonym.text="%s"%(drugbank_ID);
                    
                    #has_name
                    ddiemterms_has_name = ET.SubElement(ddiemterms_drugbank, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_name");
                    ddiemterms_has_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_name.text="%s"%(drugbank_ID);
            ##drugbank drugs (end) 2019-06-09 1155hrs
            
            ##chEBI drugs (start) 2019-06-09 1155hrs
            #include the metadata data from the ChEBI website.
            if(chEBI_ID__list!=None):
                chEBI_ID__list=list(set(chEBI_ID__list));
                for chEBI_ID in chEBI_ID__list:
                    ddiemterms_chEBI = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                    ddiemterms_chEBI.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/drugs/chEBI/%s"%(chEBI_ID));
                    ddiemterms_chEBI_ID = ET.SubElement(ddiemterms_chEBI, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}chEBI_ID");
                    ddiemterms_chEBI_ID.set("rdf:resource","http://purl.obolibrary.org/obo/%s"%(chEBI_ID.replace("CHEBI:","CHEBI_")));
                    
                    #drug_id_database_name
                    ddiemterms_drug_id_database_name = ET.SubElement(ddiemterms_chEBI, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}drug_id_database_name");
                    ddiemterms_drug_id_database_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_drug_id_database_name.text="chEBI";
                    
                    #has_abbreviation
                    ddiemterms_has_abbreviation = ET.SubElement(ddiemterms_chEBI, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_abbreviation");
                    ddiemterms_has_abbreviation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_abbreviation.text="%s"%(chEBI_ID);
                    
                    #has_synonym
                    ddiemterms_has_synonym = ET.SubElement(ddiemterms_chEBI, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_synonym");
                    ddiemterms_has_synonym.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_synonym.text="%s"%(chEBI_ID);
                    
                    #has_name
                    ddiemterms_has_name = ET.SubElement(ddiemterms_chEBI, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_name");
                    ddiemterms_has_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_name.text="%s"%(chEBI_ID);
            ##chEBI drugs (end) 2019-06-09 1200hrs
            
            ##wHOCC drugs (start) 2019-06-09 1200hrs
            if(wHOCC_ID__list!=None):
                wHOCC_ID__list=list(set(wHOCC_ID__list));
                for wHOCC_ID in wHOCC_ID__list:
                    ddiemterms_wHOCC = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
                    ddiemterms_wHOCC.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/drugs/wHOCC/%s"%(wHOCC_ID));
                    ddiemterms_wHOCC_ID = ET.SubElement(ddiemterms_wHOCC, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}wHOCC_ID");
                    ddiemterms_wHOCC_ID.set("rdf:resource","https://www.whocc.no/atc_ddd_index/?code=%s"%(wHOCC_ID));
                    
                    #drug_id_database_name
                    ddiemterms_drug_id_database_name = ET.SubElement(ddiemterms_wHOCC, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}drug_id_database_name");
                    ddiemterms_drug_id_database_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_drug_id_database_name.text="wHOCC";
                    
                    #has_abbreviation
                    ddiemterms_has_abbreviation = ET.SubElement(ddiemterms_wHOCC, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_abbreviation");
                    ddiemterms_has_abbreviation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_abbreviation.text="%s"%(wHOCC_ID);
                    
                    #has_synonym
                    ddiemterms_has_synonym = ET.SubElement(ddiemterms_wHOCC, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_synonym");
                    ddiemterms_has_synonym.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_synonym.text="%s"%(wHOCC_ID);
                    
                    #has_name
                    ddiemterms_has_name = ET.SubElement(ddiemterms_wHOCC, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_name");
                    ddiemterms_has_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
                    ddiemterms_has_name.text="%s"%(wHOCC_ID);
            ##wHOCC drugs (end) 2019-06-09 1203hrs
        
        
    
    """
    if(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]!=None):
        ddiemterms_gene_affected = ET.SubElement(rdf_RDF, "{http://purl.obolibrary.org/obo/}RO_0004020");
        ddiemterms_gene_affected.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/genes/ghr.nlm.nih.gov/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
    
    gene_affected=None;
    if(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]!=None):
        clinical_outcome_log_entry2 = ET.SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description");
        clinical_outcome_log_entry2.set("rdf:about","http://www.cbrc.kaust.edu.sa/ddiem/genes/ghr.nlm.nih.gov/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
        ddiemterms_gene_affected__description__gene_id = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}gene_id");
        ddiemterms_gene_affected__description__gene_id.set("rdf:resource","https://ghr.nlm.nih.gov/gene/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]));
        ddiemterms_gene_affected__description__has_abbreviation = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_abbreviation");
        ddiemterms_gene_affected__description__has_abbreviation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_abbreviation.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_synonym = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_synonym");
        ddiemterms_gene_affected__description__has_synonym.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_synonym.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_name = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_name");
        ddiemterms_gene_affected__description__has_name.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_name.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_id = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_id");
        ddiemterms_gene_affected__description__has_id.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_id.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        ddiemterms_gene_affected__description__has_mutation = ET.SubElement(clinical_outcome_log_entry2, "{http://www.cbrc.kaust.edu.sa/ddiem/terms/}has_mutation");
        ddiemterms_gene_affected__description__has_mutation.set("rdf:datatype","http://www.w3.org/2001/XMLSchema#string");
        ddiemterms_gene_affected__description__has_mutation.text="%s"%(clinical_log_rdf_base_fields_dataset_row__dict["gene_affected"]);
        if(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]!=None):
            ddiemterms_gene_affected__description__R0_0002205 = ET.SubElement(clinical_outcome_log_entry2, "{http://purl.obolibrary.org/obo/}RO_0002205");
            ddiemterms_gene_affected__description__R0_0002205.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/EC/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["ec_number"]));
            
        if(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]!=None):
            ddiemterms_gene_affected__description__R0_0002205 = ET.SubElement(clinical_outcome_log_entry2, "{http://purl.obolibrary.org/obo/}RO_0002205");
            ddiemterms_gene_affected__description__R0_0002205.set("rdf:resource","http://www.cbrc.kaust.edu.sa/ddiem/gene_product/uniprot_ID/%s"%(clinical_log_rdf_base_fields_dataset_row__dict["uniprot_ID"]));
    """
    """
        http://purl.obolibrary.org/obo/ECO_0000352
    
                clinical_log_rdf_base_fields_dataset_row__dict={
                    "row_id":row_id
                    ,"oMIM_ID":oMIM_ID
                    ,"disease_name":disease_name
                    ,"disease_comments":disease_comments
                    ,"gene_affected":gene_affected
                    ,"enzyme_or_protein_detected":enzyme_or_protein_detected
                    ,"ec_number":ec_number
                    ,"uniprot_ID":uniprot_ID
                    ,"regimen_name":regimen_name
                    ,"drug_ID2":drug_ID2
                    ,"drug_ID2__sha256":drug_ID2__sha256
                    
                    ,"drug_ID__ORed__csv":drug_ID__ORed__csv
                    ,"drugbank_ID__ORed__csv":drugbank_ID__ORed__csv ->12
                    ,"chEBI_ID__ORed__csv":chEBI_ID__ORed__csv
                    ,"wHOCC_ID__ORed__csv":wHOCC_ID__ORed__csv
                    
                    ,"drug_ID__ANDed__csv":drug_ID__ANDed__csv
                    ,"drugbank_ID__ANDed__csv":drugbank_ID__ANDed__csv
                    ,"chEBI_ID__ANDed__csv":chEBI_ID__ANDed__csv
                    ,"wHOCC_ID__ANDed__csv":wHOCC_ID__ANDed__csv
                    
                    ,"study_type_evidence_code__csv":study_type_evidence_code__csv
                    ,"mutation_improved_by_treatment__csv":mutation_improved_by_treatment__csv
                    ,"mutation_not_improved_by_treatment__csv":mutation_not_improved_by_treatment__csv
                    ,"regimen_mechanism_of_action__csv":regimen_mechanism_of_action__csv
                    ,"regimen_mechanism_of_action_abbreviation__csv":regimen_mechanism_of_action_abbreviation__csv
                    ,"phenotype_improved_by_treatment__csv":phenotype_improved_by_treatment__csv
                    ,"phenotype_ID__csv":phenotype_ID__csv
                    ,"treatment_manuscript_reference__csv":treatment_manuscript_reference__csv
                };
    """;
    doc_type = '<?xml version="1.0" encoding="UTF-8"?>\n' \
               '<!DOCTYPE rdf:RDF [<!ENTITY xsd "http://www.w3.org/2001/XMLSchema#">]>\n';
    indentXML(rdf_RDF);
    tostring = ET.tostring(rdf_RDF).decode('utf-8');
    str_io = io.StringIO();
    file_data = f"{doc_type}{tostring}";
    str_io.write(file_data);
    xml_data=str_io.getvalue();
    str_io=None;
    #print(xml_data);
    rdf_RDF=None;
    return xml_data;
    
#import hashlib;

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature;



def indentXML(elem, level=0):
    #https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indentXML(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem;        
    
def group_drug_ids_by_database(
    drug_ID__list
):
    grouped_drug_ids_by_database={};
    drugbank_ID__csv=None;
    chEBI_ID__csv=None;
    wHOCC_ID__csv=None;
    drugbank_ID__list=None;
    chEBI_ID__list=None;
    wHOCC_ID__list=None;
    pubChem_CID__csv=None;#PubChem:CID
    pubChem_CID__list=None;#PubChem:CID
    pubChem_SID__csv=None;#PubChem:SID
    pubChem_SID__list=None;#PubChem:SID
    pubChem_AID__csv=None;#PubChem:AID
    pubChem_AID__list=None;#PubChem:AID
    
    if(drug_ID__list!=None):
        for drug_ID2 in drug_ID__list:
            #LOGGER.info("drug_ID2 is:'%s'"%(drug_ID2));
            #test for
            match=oRegPattern_drugbank_ID.search(drug_ID2);
            if(match!=None and match.group(0)!=None):
                drugbank_ID=match.group("drugbank_ID");
                if(drugbank_ID__list==None):
                    drugbank_ID__list=[];
                drugbank_ID__list.append(drugbank_ID);
            else:
                match=oRegPattern_chEBI_ID.search(drug_ID2);
                if(match!=None and match.group(0)!=None):
                    chEBI_ID=match.group("chEBI_ID");
                    if(chEBI_ID__list==None):
                        chEBI_ID__list=[];
                    chEBI_ID__list.append("CHEBI_%s"%(chEBI_ID));
                else:
                    match=oRegPattern_pubChem_CID.search(drug_ID2);
                    if(match!=None and match.group(0)!=None):
                        pubChem_CID=match.group("pubChem_CID");
                        if(pubChem_CID__list==None):
                            pubChem_CID__list=[];
                        pubChem_CID__list.append("CID:{0}".format(pubChem_CID));
    
                        pass;
                    else:
                        match=oRegPattern_pubChem_SID.search(drug_ID2);
                        if(match!=None and match.group(0)!=None):
                            pubChem_SID=match.group("pubChem_SID");
                            if(pubChem_SID__list==None):
                                pubChem_SID__list=[];
                            pubChem_SID__list.append("SID:{0}".format(pubChem_SID));
        
                            pass;
                        else:
                            match=oRegPattern_pubChem_AID.search(drug_ID2);
                            if(match!=None and match.group(0)!=None):
                                pubChem_AID=match.group("pubChem_AID");
                                if(pubChem_AID__list==None):
                                    pubChem_AID__list=[];
                                pubChem_AID__list.append("AID:{0}".format(pubChem_AID));
            
                                pass;
                            else:
                                #Assume it is WHOCC_ID
                                if(len(drug_ID2)>0):
                                    if(wHOCC_ID__list==None):
                                        wHOCC_ID__list=[];
                                    wHOCC_ID__list.append(drug_ID2);
    drugbank_ID__csv=list_to_csv(remove_empty_values_from_list(drugbank_ID__list));
    chEBI_ID__csv=list_to_csv(remove_empty_values_from_list(chEBI_ID__list));
    pubChem_CID__csv=list_to_csv(remove_empty_values_from_list(pubChem_CID__list));
    pubChem_SID__csv=list_to_csv(remove_empty_values_from_list(pubChem_SID__list));
    pubChem_AID__csv=list_to_csv(remove_empty_values_from_list(pubChem_AID__list));
    wHOCC_ID__csv=list_to_csv(remove_empty_values_from_list(wHOCC_ID__list));
    grouped_drug_ids_by_database={
        "drugbank_ID__csv":drugbank_ID__csv
        ,"chEBI_ID__csv":chEBI_ID__csv
        ,"pubChem_CID__csv":pubChem_CID__csv
        ,"pubChem_SID__csv":pubChem_SID__csv
        ,"pubChem_AID__csv":pubChem_AID__csv
        ,"wHOCC_ID__csv":wHOCC_ID__csv
    };
    #LOGGER.info("drug_ID__list is:'%s', grouped_drug_ids_by_database is:'%s'"%(drug_ID__list,grouped_drug_ids_by_database));
    return grouped_drug_ids_by_database;

def remove_empty_values_from_list(
    row
):
    doc="""
    This function removes all the empty elements from a list.
    """;
    if(row!=None):
        row=[x for x in row if x != "" ];
    return row;

def list_to_csv(
    row
):
    doc="""
    This function takes a list and outputs a CSV string
    The use of ','.join(list) is not recommended as there may be some ',' characters embedded in the data values.
    """;
    str_csv=None;
    if(row!=None):
        str_io=None;
        str_io=io.StringIO();
        dest_csv_writer=csv.writer(str_io,quotechar='"',quoting=csv.QUOTE_MINIMAL);
        dest_csv_writer.writerow(
            row
        );
        #dest_csv_writer.flush();
        #dest_csv_writer.close();
        dest_csv_writer=None;
        str_csv=str_io.getvalue().strip();
        str_io.close();
        str_io=None;
    return str_csv;

def csv_to_list(
    str_csv
    ,delimiter_char=","
):
    doc="""
    This function takes CSV string and a delimiter_char and outputs a list
    """;
    row=None;
    if(str_csv!=None):
        str_io=None;
        str_io=io.StringIO(str_csv);
        csv_reader=csv.reader(str_io,delimiter=delimiter_char,quotechar='"',quoting=csv.QUOTE_MINIMAL);
        row_cnt=0;
        for row in csv_reader:
            row_cnt+=1;
            for i, val in enumerate(row):
                row[i]=row[i].strip();
        str_io.close();
        str_io=None;
    return row;

def getLocalIPAddress():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
    s.connect(('google.com',80));
    return s.getsockname()[0];

def touch(file_name):
    mkdir_p(os.path.abspath(os.path.join(file_name, os.pardir)));
    with open(file_name,'a'):
        os.utime(file_name,None);

import errno;
def mkdir_p(path):
    if(not(os.path.exists(path) and os.path.isdir(path))):
        try:
            os.makedirs(path,exist_ok=True);
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise   


def format_my_nanos(nanos):
        dt = datetime.datetime.fromtimestamp(nanos / 1e9)
        #return '{}.{:09.0f}'.format(dt.strftime('%Y-%m-%dT%H:%M:%S'), nanos % 1e9);
        return '{}_{:09.0f}'.format(dt.strftime('%Y%m%d%H%M%S'), nanos % 1e9);


def timestamp_from_nano_seconds(nanos):
        dt = datetime.datetime.fromtimestamp(nanos / 1e9)
        #return '{}.{:09.0f}'.format(dt.strftime('%Y-%m-%dT%H:%M:%S'), nanos % 1e9);
        return '{}_{:09.0f}'.format(dt.strftime('%Y/%m/%d %H:%M:%S'), nanos % 1e9);


class InfiniteTimer():#see https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
    """A Timer class that does not stop, unless you want it to.""";
    def __init__(self, seconds, target, countdown__upperbound):
        self._should_continue = False;
        self.is_running = False;
        self.seconds = seconds;
        self.target = target;
        self.thread = None;
        self.countdown__upperbound=countdown__upperbound;
        
    def _handle_target(self):
        self.is_running = True;
        self.target();
        self.is_running = False;
        self._start_timer();
        
    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.;
            self.thread = threading.Timer(self.seconds, self._handle_target);
            LOGGER.info("self.countdown__upperbound is:%d"%(self.countdown__upperbound));
            if(self.countdown__upperbound>0):
                self.thread.start();
                self.countdown__upperbound-=1;
            else:
                self._should_continue=False;
            
    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True;
            self._start_timer();
        else:
            print("Timer already started or running, please wait if you're restarting.");
            
    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.;
            self.thread.cancel();
        else:
            print("Timer never started or failed to initialize.");



from xml.sax import make_parser
from xml.sax.handler import feature_namespaces

if __name__ == '__main__':
    task_formulation_timestamp=None;#datetime.datetime.strptime('20180910_135822_123456', '%Y%m%d_%H%M%S_%f');
    task_formulation_timestamp_str=None;#'20180910_135822_123456';
    working_dir_file_name=None;
    borg_ddiem_relational_ontology_graph_csv_file_name=None;
    src_clinical_log_dataset_csv_file_name=None;
    dest_dir_file_name=None;
    dest_dir_file_name=None;
    drugbank_drug_names_dataset_tsv_file_name=None;
    OMIM_mimTitles_dataset_tsv_file_name=None;
    drugbank_drug_names_dataset_tsv_file_name=None;
    ChEBI_drug_names_dataset_tsv_file_name=None;
    gene_info_tsv_file_name=None;
    iembase_mapping_csv_file_name=None;
    gene_id__2__uniprotkb_id_tsv_file_name=None;
    uniprotkb_id__2__ko_id_tsv_file_name=None;
    uniprotkb_id__2__ec_number_tsv_file_name=None;
    
    count_of_workers=1;
    usage="usage: %prog [options] arg1 [[arg2]..]"
    version="version: 0.001"

    import argparse;
    parser=argparse.ArgumentParser();
    try:
        parser.add_argument("-t","--task_formulation_timestamp_str",action="append",type=str,dest="op__task_formulation_timestamp_str",help="""
            This variable will contain the current timestamp in 'Ymd_HMS_f' format, for example '20180910_135822_123456'. This timestamp will be the bases of the task id of this job.
        """);
        parser.add_argument("-o","--working_dir_file_name",action="append",type=str,dest="op__working_dir_file_name",help="""
            The full path to the directory where temporary data will be written.
        """);
        parser.add_argument("-g","--borg_ddiem_relational_ontology_graph_csv_file_name",action="append",type=str,dest="op__borg_ddiem_relational_ontology_graph_csv_file_name",help="The full path to the BORG_DDIEM graph CSV file.")
        parser.add_argument("-f","--src_clinical_log_dataset_csv_file_name",action="append",type=str,dest="op__src_clinical_log_dataset_csv_file_name",help="The full path to the CSV file where the input dataset is to be found.")
        parser.add_argument("-d","--dest_dir_file_name",action="append",type=str,dest="op__dest_dir_file_name",help="The full directory path where the resultant CSV file will be written.")
        parser.add_argument("-m","--OMIM_mimTitles_dataset_tsv_file_name",action="append",type=str,dest="op__OMIM_mimTitles_dataset_tsv_file_name",help="The full path to the TSV morbidmap.txt file from OMIM where OMIM id to OMIM names are to be found.")
        parser.add_argument("-b","--drugbank_drug_names_dataset_tsv_file_name",action="append",type=str,dest="op__drugbank_drug_names_dataset_tsv_file_name",help="The full path to the TSV file containing the drug names of the drug entries in the drugbank dataset. This file was generated by the python script 'BORG_DDIEM__split_drugbank_xml.py', this script extracted the drug metadata from each drug entry in the large drugbank xml documents.")
        parser.add_argument("-c","--ChEBI_drug_names_dataset_tsv_file_name",action="append",type=str,dest="op__ChEBI_drug_names_dataset_tsv_file_name",help="The full path to the TSV (ordinarily named 'names.tsv') provided by ChEBI which contains the names of the drugs.")
        parser.add_argument("-e","--gene_info_tsv_file_name",action="append",type=str,dest="op__gene_info_tsv_file_name",help="The full path to the ncbi gene_info dataset encoded as a TSV text file.")
        parser.add_argument("-i","--iembase_mapping_csv_file_name",action="append",type=str,dest="op__iembase_mapping_csv_file_name",help="The full path to the IEMbase dataset encoded as a CSV text file.")
        parser.add_argument("-u","--gene_id__2__uniprotkb_id_tsv_file_name",action="append",type=str,dest="op__gene_id__2__uniprotkb_id_tsv_file_name",help="The full path to the Gene_id to UniProtKB_id mapping TSV text file.")
        parser.add_argument("-k","--uniprotkb_id__2__ko_id_tsv_file_name",action="append",type=str,dest="op__uniprotkb_id__2__ko_id_tsv_file_name",help="The full path to the UniProtKB_id to KO_id mapping TSV text file.")
        parser.add_argument("-n","--uniprotkb_id__2__ec_number_tsv_file_name",action="append",type=str,dest="op__uniprotkb_id__2__ec_number_tsv_file_name",help="The full path to the UniProtKB_id to EC number mapping TSV text file.")
        parser.add_argument("-p","--PubChem_CID_csv_file_name",action="append",type=str,dest="op__PubChem_CID_csv_file_name",help="The full path to the PubChem CID to PubChem compound_name mapping CSV text file.")
        
        
        parser.add_argument("-w","--count_of_workers",action="append",type=int,dest="op__count_of_workers",help="""
            The count of workers to launch (via multiprocessing).
        """);
        
        (options)=parser.parse_args(sys.argv[1:])
        if len(sys.argv)<4:
            parser.error("""
                ERROR: Missing required arguments
                -t, --task_formulation_timestamp_str
                    This variable will contain the current timestamp in 'Ymd_HMS_f' format, for example '20180910_135822_123456'. This timestamp will be the bases of the task id of this job.
                -o, --working_dir_file_name
                    The full path to the directory where temporary data will be written.
                -g, --borg_ddiem_relational_ontology_graph_csv_file_name
                    The full path to the BORG_DDIEM graph CSV file.
                -f, --src_clinical_log_dataset_csv_file_name
                    The full path to the CSV file where the input dataset is to be found.
                -d, --dest_dir_file_name
                    The full directory path where the resultant CSV file will be written.
                -m, --OMIM_mimTitles_dataset_tsv_file_name
                    The full path to the CSV file where the input dataset is to be found.
                -b, --drugbank_drug_names_dataset_tsv_file_name
                    The full path to the TSV file containing the drug names of the drug entries in the drugbank dataset. This file was generated by the python script 'BORG_DDIEM__split_drugbank_xml.py', this script extracted the drug metadata from each drug entry in the large drugbank xml documents.
                -c, --ChEBI_drug_names_dataset_tsv_file_name
                    The full path to the TSV (ordinarily named 'names.tsv') provided by ChEBI which contains the names of the drugs.
                -e, --gene_info_tsv_file_name
                    The full path to the ncbi gene_info dataset encoded as a TSV text file.
                -i, --iembase_mapping_csv_file_name
                    The full path to the IEMbase mapping dataset encoded as a CSV text file.
                -u, --gene_id__2__uniprotkb_id_tsv_file_name
                    The full path to the Gene_id to UniProtKB_id mapping TSV text file.
                -k, --uniprotkb_id__2__ko_id_tsv_file_name
                    The full path to the UniProtKB_id to KO_id mapping TSV text file.
                -n, --uniprotkb_id__2__ec_number_tsv_file_name
                    The full path to the UniProtKB_id to EC number mapping TSV text file.
                -p, --PubChem_CID_csv_file_name
                    The full path to the PubChem CID to PubChem compound_name mapping CSV text file.
                -w, --count_of_workers
                    The count of workers to launch (via multiprocessing).
            """);
            
        if(options.op__task_formulation_timestamp_str):
            task_formulation_timestamp_str=options.op__task_formulation_timestamp_str[0].strip();
        if(options.op__working_dir_file_name):
            working_dir_file_name=options.op__working_dir_file_name[0].strip();
        if(options.op__borg_ddiem_relational_ontology_graph_csv_file_name):
            borg_ddiem_relational_ontology_graph_csv_file_name=options.op__borg_ddiem_relational_ontology_graph_csv_file_name[0];
        if(options.op__src_clinical_log_dataset_csv_file_name):
            src_clinical_log_dataset_csv_file_name=options.op__src_clinical_log_dataset_csv_file_name[0];
        if(options.op__dest_dir_file_name):
            dest_dir_file_name=options.op__dest_dir_file_name[0];
            mkdir_p(os.path.abspath(os.path.join(dest_dir_file_name, os.pardir)));
            mkdir_p(os.path.abspath(dest_dir_file_name));
        if(options.op__OMIM_mimTitles_dataset_tsv_file_name):
            OMIM_mimTitles_dataset_tsv_file_name=options.op__OMIM_mimTitles_dataset_tsv_file_name[0];
        if(options.op__drugbank_drug_names_dataset_tsv_file_name):
            drugbank_drug_names_dataset_tsv_file_name=options.op__drugbank_drug_names_dataset_tsv_file_name[0];
        if(options.op__ChEBI_drug_names_dataset_tsv_file_name):
            ChEBI_drug_names_dataset_tsv_file_name=options.op__ChEBI_drug_names_dataset_tsv_file_name[0];
        if(options.op__gene_info_tsv_file_name):
            gene_info_tsv_file_name=options.op__gene_info_tsv_file_name[0];
        if(options.op__iembase_mapping_csv_file_name):
            iembase_mapping_csv_file_name=options.op__iembase_mapping_csv_file_name[0];
        if(options.op__gene_id__2__uniprotkb_id_tsv_file_name):
            gene_id__2__uniprotkb_id_tsv_file_name=options.op__gene_id__2__uniprotkb_id_tsv_file_name[0];
        if(options.op__uniprotkb_id__2__ko_id_tsv_file_name):
            uniprotkb_id__2__ko_id_tsv_file_name=options.op__uniprotkb_id__2__ko_id_tsv_file_name[0];
        if(options.op__uniprotkb_id__2__ec_number_tsv_file_name):
            uniprotkb_id__2__ec_number_tsv_file_name=options.op__uniprotkb_id__2__ec_number_tsv_file_name[0];
        if(options.op__PubChem_CID_csv_file_name):
            PubChem_CID_csv_file_name=options.op__PubChem_CID_csv_file_name[0];
            
        if(options.op__count_of_workers):
            count_of_workers=int(options.op__count_of_workers[0]);

        #parser.destroy()
    except argparse.ArgumentError:
        #print help infor and exit
        usage();
        sys.exit(2);
    
    print("dest_dir_file_name is:'%s'"%(dest_dir_file_name));
    #print("dest_ddl_file_name is:'%s'"%(dest_ddl_file_name));
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT);
    
    task_formulation_timestamp=None;
    if(task_formulation_timestamp_str!=None and len(task_formulation_timestamp_str)>0):
        task_formulation_timestamp=datetime.datetime.strptime(task_formulation_timestamp_str, '%Y%m%d_%H%M%S_%f');
    else:
        task_formulation_timestamp=datetime.datetime.now();
    task_id="%s"%(task_formulation_timestamp.strftime('%Y-%m-%d_%H%M%S_%f')[:-3]);#import datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-1]
    
    hostname=socket.gethostname().strip();
    ipAddress=getLocalIPAddress();
    pid=os.getpid();
    worker_id='%s_%s_%d'%(hostname,ipAddress,pid);
    LOGGER.info(" '%s', -------------- hostname:'%s', ipAddress:'%s', pid:%d, worker_id:'%s', task_id:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),hostname,ipAddress,pid,worker_id,task_id));
    LOGGER.info(" '%s', -------------- borg_ddiem_relational_ontology_graph_csv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),borg_ddiem_relational_ontology_graph_csv_file_name));
    LOGGER.info(" '%s', -------------- src_clinical_log_dataset_csv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),src_clinical_log_dataset_csv_file_name));
    LOGGER.info(" '%s', -------------- dest_dir_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),dest_dir_file_name));
    LOGGER.info(" '%s', -------------- OMIM_mimTitles_dataset_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),OMIM_mimTitles_dataset_tsv_file_name));
    LOGGER.info(" '%s', -------------- ChEBI_drug_names_dataset_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),ChEBI_drug_names_dataset_tsv_file_name));
    LOGGER.info(" '%s', -------------- gene_info_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),gene_info_tsv_file_name));
    LOGGER.info(" '%s', -------------- iembase_mapping_csv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),iembase_mapping_csv_file_name));
    LOGGER.info(" '%s', -------------- gene_id__2__uniprotkb_id_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),gene_id__2__uniprotkb_id_tsv_file_name));
    LOGGER.info(" '%s', -------------- uniprotkb_id__2__ko_id_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),uniprotkb_id__2__ko_id_tsv_file_name));
    LOGGER.info(" '%s', -------------- uniprotkb_id__2__ec_number_tsv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),uniprotkb_id__2__ec_number_tsv_file_name));
    LOGGER.info(" '%s', -------------- PubChem_CID_csv_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),PubChem_CID_csv_file_name));
    LOGGER.info(" '%s', -------------- count_of_workers is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),count_of_workers));
    process_list=[];
    queue_list=[];#this array will contain objects of multiprocessing.Queue (which is a near clone of queue.Queue)
    worker_list=[];
    
    try:
        for i in range(count_of_workers):
            #Instantiates the thread
            #(i) dos not make a sequence, so we use (i,)
            worker_id2='%s__%s__%d'%('BORG_DDIEM__prepare_clinical_logs_for_rdf_part1',worker_id,i);
            LOGGER.info(">>>>>>>>>>worker_tag:'%s'"%(worker_id2));
            
            worker_number=i;
            w=BORG_DDIEM__prepare_clinical_logs_for_rdf_part1(
                hostname,ipAddress,pid
                ,task_id
                ,task_formulation_timestamp
                ,worker_id2
                ,worker_number
                ,working_dir_file_name
                ,borg_ddiem_relational_ontology_graph_csv_file_name
                ,src_clinical_log_dataset_csv_file_name
                ,"%s"%(dest_dir_file_name)
                ,OMIM_mimTitles_dataset_tsv_file_name
                ,drugbank_drug_names_dataset_tsv_file_name
                ,ChEBI_drug_names_dataset_tsv_file_name
                ,gene_info_tsv_file_name
                ,iembase_mapping_csv_file_name
                ,gene_id__2__uniprotkb_id_tsv_file_name
                ,uniprotkb_id__2__ko_id_tsv_file_name
                ,uniprotkb_id__2__ec_number_tsv_file_name
                ,PubChem_CID_csv_file_name
            );
            """
            t=threading.Thread(
                target=run_BORG_DDIEM__prepare_clinical_logs_for_rdf_part1
                ,args=(
                    d
                    ,worker_id2
                )
            );
            thread_list.append(t);
            worker_list.append(d);
            """
            q=multiprocessing.Queue();
            p=multiprocessing.Process(
                target=run_BORG_DDIEM__prepare_clinical_logs_for_rdf_part1
                ,args=(
                    w
                    ,q
                    ,worker_id2
                )
            );
            process_list.append(p);
            queue_list.append(q);
            worker_list.append(w);
            
        for process in process_list:
            process.start();
                
        #block the current process till join() returns
        #for process in process_list:
        for i,process in enumerate(process_list):
            cont=True;
            while(cont):
                #LOGGER.info("============Looping, i is:%d, process_list[%d].isAlive() is:'%s'"%(i,i,process_list[i].isAlive()));
                process.join(60);#wait for 60 seconds.
                if(process.is_alive()):
                    #timout occurred on process
                    cont=True;
                    #LOGGER.info("timeout occurred on process:'%s'."%(worker_list[i].worker_id));
                    #worker_list[i].stop();
                    #worker_list[i].some_function();
                else:
                    cont=False;
                    #LOGGER.info("execution completes for process:'%s'."%(worker_list[i].consumer_tag));
        for i,worker in enumerate(worker_list):
            pass;
            """
            """;
            #processing_outcome__dict=worker_list[i]._processing_outcome__dict;
            #processing_outcome__dict=worker_list[i].get_processing_outcome();
            processing_outcome__dict=queue_list[i].get();
            #LOGGER.info("[=]%s, %s"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),json.dumps(processing_outcome__dict,indent=4)));
            LOGGER.info("processing_outcome__dict is:'%s'"%(json.dumps(processing_outcome__dict,indent=4)));
            worker_list[i]=None;
            worker=None;
            
    except KeyboardInterrupt:
        for i,worker in enumerate(worker_list):
            pass;
            """
            """;
            #cleanup
            #worker.cleanup();
            if(worker_list[i]!=None):
                worker_list[i].stop();
                processing_outcome__dict=worker_list[i]._processing_outcome__dict;
                worker_list[i]=None;
                worker=None;
        worker_list=None;
        queue_list=None;
        process_list=None;
    """
    except Exception as error:
        LOGGER.error("An error has been detected. Reason:'%s'"%(error));
        worker_list=None;
        thread_list=None;
    """
    worker_list=None;
    queue_list=None;
    process_list=None;

