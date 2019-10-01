# Transforms ddiem collapased csv to rdf 
from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC, ClosedNamespace, RDFS
from rdflib.term import URIRef

import csv
import json
import hashlib
import uuid
import re

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

if __name__ == '__main__':

    DDIEM = ClosedNamespace(
        uri=URIRef("http://ddiem.phenomebrowser.net/"),
        terms=[
            #Classes
            "Disease", "Drug", "TheraputicProcedure", "Phenotype", "Evidence",
            "Gene", "ProtienOrEnzyme", "Provenance", "TheraputicProcedureType",

            #Properties
            "ecNumber", "uniprotId", "url", "failedToContributeToCondition"
        ]
    )

    OBO = ClosedNamespace(
        uri=URIRef("http://purl.obolibrary.org/obo/"),
        terms=[
            #participates-in
            "RO_0000056",
            #treats
            "RO_0002606",
            #negatively regulates
            "RO_0002212",
            #has evidence
            "RO_0002558",
            #has phenotype
            "RO_0002200",
            #gene product of 
            "RO_0002204",
            #disease has basis in dysfunction of 
            "RO_0004020",
            #contributes to condition
            "RO_0003304",
            #has participant
            "RO_0000057"
        ]
    )

    DDIEM_SOURCE_FILE = "../../raw_data/2019-09-29/BORG_DDIEM__clinical_logs.2019-09-29.1713hrs.collapsed.clinical_logs_for_rdf_part1.csv"
    DRUG_BANK_FILE = "../../raw_data/2019-09-29/BORG_DDIEM__clinical_logs.2019-09-29.1713hrs.collapsed.clinical_logs_for_rdf_part1.drugbank_drug_names.json"
    CHEBI_FILE = "../../raw_data/2019-09-29/BORG_DDIEM__clinical_logs.2019-09-29.1713hrs.collapsed.clinical_logs_for_rdf_part1.ChEBI_drug_names.json"
    WHOCC_FILE = "../../raw_data/2019-09-01/WHOCC/BORG_DDIEM__clinical_logs.2019-09-01.1348hrs.collapsed.clinical_logs_for_rdf_part1.WHOCC_drug_names.json"

    drug_bank = {}
    with open(DRUG_BANK_FILE, "r", encoding="utf-8") as json_file:
        drug_bank = json.load(json_file)

    def find_drug(drug_bank, drug_id): 
        return (drug for key, drug in drug_bank.items() if key == drug_id)

    chebi_drug_bank = {}
    with open(CHEBI_FILE, "r", encoding="utf-8") as json_file:
        chebi_drug_bank = json.load(json_file)

    def find_chebi_drug(drug_bank, drug_id): 
        return (drug_name for key, drug in drug_bank.items() if key == drug_id for drug_name in drug if drug_name['source'] == "ChEBI" or drug_name['source'] == "UniProt")

    who_drug_bank = {}
    with open(WHOCC_FILE, "r", encoding="utf-8") as json_file:
        who_drug_bank = json.load(json_file)

    def find_drug_name(drug_id):
        global drug_bank, chebi_drug_bank, who_drug_bank
        if drug_id.startswith("CHEBI"):
            drug = next(find_chebi_drug(chebi_drug_bank, drug_id.replace(":", "_")), None)
            return drug['name'] if drug else ''
        elif drug_id.startswith("DB"):
            drug = next(find_drug(drug_bank, drug_id), None)
            return drug['drug_name'] if drug else ''
        else :
            drug = next(find_drug(who_drug_bank, drug_id), None)
            return drug['name'] if drug else ''

    store = Graph()

    # Bind a few prefix, namespace pairs for pretty output
    store.bind("dc", DC)
    store.bind("foaf", FOAF)
    store.bind("ddiem", DDIEM)
    store.bind("obo", OBO)

    disease_dict = {}
    gene_dict = {}
    protien_dict = {}
    procedure_dict = {}
    drug_dict = {}
    drug_container_dict = {}
    pheno_dict = {}
    procedure_type_dict = {}

    def drug(drug_id):
        global drug_dict
        if encrypt_string(drug_id) not in drug_dict :
            drug_res = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
            drug_res.set(RDF.type, DDIEM.Drug)
            drug_res.set(DC.identifier, Literal(drug_id))
            drug_res.add(DDIEM.url, Literal("https://www.drugbank.ca/drugs/" + drug_id)) if drug_id.startswith("DB") else None
            drug_res.add(DDIEM.url, Literal("https://www.ebi.ac.uk/chebi/searchId.do?chebiId=" + drug_id)) if drug_id.startswith("CHEBI") else None
            drug_res.add(DDIEM.url, Literal("https://www.whocc.no/atc_ddd_index/?code=" + drug_id)) if not drug_id.startswith("CHEBI") and not drug_id.startswith("DB") else None
            name = find_drug_name(drug_id)
            if name:
                drug_res.set(RDFS.label, Literal(name))
            drug_dict[encrypt_string(drug_id)] = drug_res
            return drug_res
        else :
            return drug_dict[encrypt_string(drug_id)]

    def drug_by_name(drug_name):
        global drug_dict
        if encrypt_string(drug_name) not in drug_dict :
            drug_res = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
            drug_res.set(RDF.type, DDIEM.Drug)
            drug_res.set(RDFS.label, Literal(drug_name))
            drug_dict[encrypt_string(drug_name)] = drug_res
            return drug_res
        else :
            return drug_dict[encrypt_string(drug_name)]


    with open(DDIEM_SOURCE_FILE, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 1:
                print("Column names are :" + ", ".join(row))
            elif line_count > 1:
                disease_id_col = row[1].replace('#', '').replace('*', '').replace('%', '').strip()
                drug_comb_col = (row[24].strip() if row[24] else '') + (row[25].strip() if row[25] else '') + (row[26].strip() if row[26] else '') + (row[28].strip() if row[28] else '') + (row[29].strip() if row[29] else '') + (row[30].strip() if row[30] else '')
                drug_name = row[17]
                use_drug_name = False
                if not drug_comb_col.strip() and drug_name.strip():
                    drug_comb_col = drug_name
                    use_drug_name = True

                disease = None
                if disease_id_col not in disease_dict :
                    disease = store.resource(str(DDIEM.uri) +  disease_id_col)
                    disease.set(RDF.type, DDIEM.Disease)
                    disease.set(RDFS.label, Literal(row[5]))
                    disease.set(RDFS.comment, Literal(row[9]))
                    disease.add(DC.identifier, Literal("https://www.omim.org/entry/" + disease_id_col))
                    disease_dict[disease_id_col] = disease
                else :
                    disease = disease_dict[disease_id_col]


                protein_enzyme_col=12
                protein_enzyme = None
                if encrypt_string(row[protein_enzyme_col]) not in protien_dict :
                    protein_enzyme = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                    protein_enzyme.set(RDF.type, DDIEM.ProtienOrEnzyme)
                    protein_enzyme.set(RDFS.label, Literal(row[protein_enzyme_col]))

                    for ecNumber in row[15].split(","):
                        protein_enzyme.add(DDIEM.ecNumber, Literal(ecNumber.strip())) if ecNumber.strip() else None

                    for uniprotId in row[16].split(","):
                        protein_enzyme.add(DDIEM.uniprotId, Literal(uniprotId.strip())) if uniprotId.strip() else None

                    protien_dict[encrypt_string(row[protein_enzyme_col])] = protein_enzyme
                else :
                    protein_enzyme = protien_dict[encrypt_string(row[protein_enzyme_col])]

                gene_col=11
                for geneCode in row[gene_col].split(","):
                    if not geneCode.strip():
                        continue

                    if geneCode not in gene_dict :
                        gene = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                        gene.set(RDF.type, DDIEM.Gene)
                        gene.set(RDFS.label, Literal(geneCode))
                        gene.add(DC.identifier, Literal("https://ghr.nlm.nih.gov/gene/" + geneCode))
                        disease.set(OBO.RO_0004020, gene)
                        gene_dict[geneCode] = gene
                    else :
                        disease.add(OBO.RO_0004020, gene_dict[geneCode])

                    if gene_dict[geneCode] not in store.objects(protein_enzyme, OBO.RO_0002204):
                        protein_enzyme.add(OBO.RO_0002204, gene_dict[geneCode])

                if not drug_comb_col.strip() or drug_comb_col.strip() == "No treatment is available in DDIEM":
                    print("disease dont have treatment :" + disease_id_col)
                    line_count += 1
                    continue

                procedure_type_col=34
                procedure_type = None
                if row[procedure_type_col] and encrypt_string(row[procedure_type_col]) not in procedure_type_dict :
                    procedure_type = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                    procedure_type.set(RDF.type, DDIEM.TheraputicProcedureType)
                    procedure_type.set(RDFS.label, Literal(row[procedure_type_col]))
                    procedure_type_dict[encrypt_string(row[procedure_type_col])] = procedure_type
                elif row[procedure_type_col]:
                    procedure_type = procedure_type_dict[encrypt_string(row[procedure_type_col])]

                procedure_id = disease_id_col + ":" + drug_comb_col
                if encrypt_string(procedure_id) not in procedure_dict :
                    procedure = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                    procedure.set(RDF.type, DDIEM.TheraputicProcedure)
                    procedure.set(RDFS.comment, Literal(row[18]))
                    procedure.set(OBO.RO_0002606, disease)
                    if procedure_type:
                        procedure.set(RDFS.subClassOf, procedure_type) 
                    procedure_dict[encrypt_string(procedure_id)] = procedure
                
                for evidenceStr in row[31].split(','):
                    evidenceStr = evidenceStr.strip().replace(" ", "")
                    if evidenceStr:
                        evidence = store.resource(str(DDIEM.uri) + evidenceStr)
                        evidence.set(RDF.type, DDIEM.Evidence)
                        evidence.set(DC.identifier, Literal(evidenceStr))
                        evidence.set(DDIEM.url, Literal("http://purl.obolibrary.org/obo/" + evidenceStr.replace(":", "_")))
                        if evidence and evidence not in store.objects(procedure_dict[encrypt_string(procedure_id)], OBO.RO_0002558) :
                            procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0002558, evidence)

                for referenceStr in row[39].split(","):
                    referenceLiteral = Literal(referenceStr.strip()) if referenceStr.strip() else None
                    if referenceLiteral and referenceLiteral not in store.objects(procedure_dict[encrypt_string(procedure_id)], DC.provenance) :
                        procedure_dict[encrypt_string(procedure_id)].add(DC.provenance, referenceLiteral)
                
                #drug ored columns
                drug_container = None
                ored_drug_comb_col =(row[23].strip() if row[23] else '') + (row[24].strip() if row[24] else '') + (row[25].strip() if row[25] else '')
                if ored_drug_comb_col.strip() and encrypt_string(ored_drug_comb_col.strip()) in drug_container_dict :
                    drug_container =  drug_container_dict[ encrypt_string(ored_drug_comb_col.strip())]
                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)
                else :
                    drug_container = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                    drug_container.add(RDF.type, RDF.Alt)
                    drug_container_dict[ encrypt_string(ored_drug_comb_col.strip())] = drug_container
                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)

                for drug_col in row[23:26]:
                    if not drug_col.strip() : 
                        continue
                    
                    for item in drug_col.split(','):
                        drug_res = drug(drug_id=item.strip())
                        drug_res.add(OBO.RO_0000056, procedure_dict[encrypt_string(procedure_id)])
                        drug_container.add(RDF.li, drug_res) 
                
                #drug and columns
                for drug_col in row[27:30]:
                    if not drug_col.strip():
                        continue

                    for item in drug_col.split(','):
                        if encrypt_string(item.strip()) in drug_container_dict :
                            drug_container =  drug_container_dict[ encrypt_string(item.strip())]
                            procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)
                        else :
                            drug_container = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                            drug_container.add(RDF.type, RDF.Alt)
                            drug_res = drug(item.strip())
                            drug_res.add(OBO.RO_0000056, procedure_dict[encrypt_string(procedure_id)])
                            drug_container.add(RDF.li, drug_res)
                            drug_container_dict[encrypt_string(item.strip())] = drug_container
                            procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)

                if use_drug_name:
                    if encrypt_string(drug_name.strip()) in drug_container_dict :
                        drug_container =  drug_container_dict[ encrypt_string(drug_name.strip())]
                        procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)
                    else :
                        drug_container = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                        drug_container.add(RDF.type, RDF.Alt)
                        drug_res = drug_by_name(drug_name.strip())
                        drug_res.add(OBO.RO_0000056, procedure_dict[encrypt_string(procedure_id)])
                        drug_container.add(RDF.li, drug_res)
                        drug_container_dict[encrypt_string(drug_name.strip())] = drug_container
                        procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0000057, drug_container)

                phenotype_col_id=36
                phenotype = None
                if row[phenotype_col_id].strip():
                    if encrypt_string(row[phenotype_col_id]) not in pheno_dict :
                        phenotype = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                        phenotype.set(RDF.type, DDIEM.Phenotype)
                        phenotype.set(RDFS.label, Literal(row[phenotype_col_id]))
                        phenotype.set(RDFS.comment, Literal(row[38]))
                        phenotype.add(DC.identifier, Literal(row[37]))
                        pheno_dict[encrypt_string(row[phenotype_col_id])] = phenotype
                        phenotype.add(DDIEM.url, Literal("http://purl.obolibrary.org/obo/" + row[37].replace(":", "_").replace("*", "")))
                    else :
                        phenotype = pheno_dict[encrypt_string(row[phenotype_col_id])]

                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0002212, phenotype)

                #mutation or genetype elements
                if row[32].strip():
                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0003304, Literal(row[32].strip()))
                if row[33].strip():
                    procedure_dict[encrypt_string(procedure_id)].add(DDIEM.failedToContributeToCondition, Literal(row[33].strip()))
        
            line_count += 1
        print("Processed " + str(line_count) + " lines.")

    # Serialize the file to rdf/xml representation
    store.serialize("../../raw_data/2019-09-29/ddiem.rdf", format="pretty-xml", max_depth=3)
