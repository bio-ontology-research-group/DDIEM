# Transforms ddiem collapased csv to rdf 
from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC, ClosedNamespace, RDFS, DCTERMS
from rdflib.term import URIRef

import csv
import json
import hashlib
import uuid
import re
import datetime

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

if __name__ == '__main__':

    DDIEM = ClosedNamespace(
        uri=URIRef("http://ddiem.phenomebrowser.net/"),
        terms=[
            #Classes
            "Disease", "Drug", "Phenotype", "Evidence", "DDIEM",
            "Gene", "ProtienOrEnzyme", "Provenance",

            #Properties
            "ecNumber", "uniprotId", "keggEntryId", "url", "failedToContributeToCondition", "iembaseAccessionNumber", "iembaseUrl"
        ]
    )

    OBO = ClosedNamespace(
        uri=URIRef("http://purl.obolibrary.org/obo/"),
        terms=[
            #participates-in
            "RO_0000056",
            #treats
            "RO_0002599",
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
            "RO_0000057",
            #therapeutic procedure
            "OGMS_0000112",
            #combination therapeutic procedure
            "DDIEM_0000023",
            #part of
            "BFO_0000050"
        ]
    )

    VOID = ClosedNamespace(uri=URIRef("http://rdfs.org/ns/void#"), terms=['Dataset','sparqlEndpoint','feature'])
     

    DDIEM_SOURCE_FILE = "../../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.0958hrs.collapsed.clinical_logs_for_rdf_part1.csv"
    DRUG_BANK_FILE = "../../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.0958hrs.collapsed.clinical_logs_for_rdf_part1.drugbank_drug_names.json"
    CHEBI_FILE = "../../raw_data/2020-01-16/BORG_DDIEM__clinical_logs.2020-01-16.0958hrs.collapsed.clinical_logs_for_rdf_part1.ChEBI_drug_names.json"
    WHOCC_FILE = "../../raw_data/2020-01-12/WHOCC/BORG_DDIEM__clinical_logs.2020-01-13.0859hrs.collapsed.clinical_logs_for_rdf_part1.WHOCC_drug_names.json"

    drug_bank = {}
    with open(DRUG_BANK_FILE, "r", encoding="utf-8") as json_file:
        drug_bank = json.load(json_file)

    def find_drug(drug_bank, drug_id): 
        return (drug for key, drug in drug_bank.items() if key == drug_id)

    chebi_drug_bank = {}
    with open(CHEBI_FILE, "r", encoding="utf-8") as json_file:
        chebi_drug_bank = json.load(json_file)

    def find_chebi_drug(drug_bank, drug_id): 
        return (drug_name for key, drug in drug_bank.items() if key == drug_id for drug_name in drug if len(drug) == 1 or drug_name['source'] == "ChEBI" or drug_name['source'] == "UniProt")

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

    def add_ored_drugs(row, procedure, pubchem_cid_or, pubchem_cid_or_name):
        for drug_col in row[24:27]:
            if not drug_col.strip() : 
                continue
            
            drug_col = drug_col.replace('(','').replace(')','')
            for item in drug_col.split(','):
                drug_res = drug(drug_id=item.strip())
                drug_res.add(OBO.RO_0000056, procedure)
                procedure.add(OBO.RO_0000057, drug_res)

        if pubchem_cid_or:
            names = pubchem_cid_or_name.split(',')
            count = 0
            print("or:", pubchem_cid_or, "|", pubchem_cid_or_name)
            for item in pubchem_cid_or.split(','):
                drug_res = pubchem_drug(drug_id=item.strip(), drug_name=names[count])
                drug_res.add(OBO.RO_0000056, procedure)
                procedure.add(OBO.RO_0000057, drug_res)
                count += 1

    store = Graph()

    # Bind a few prefix, namespace pairs for pretty output
    store.bind("dc", DC)
    store.bind("foaf", FOAF)
    store.bind("ddiem", DDIEM)
    store.bind("obo", OBO)
    store.bind("dcterms", DCTERMS)
    store.bind("void", VOID)

    description = '''DDIEM - Drug database for inborn errors of metabolism is a database on therapeutic strategies
     for inborn errors of metabolism. These strategies are classified by mechanism and outcome in DDIEM Ontology. 
     DDIEM uses this ontology to categprise the experimental treatments that have been proposed or applied. It 
     includes descriptions of the phenotypes addressed by the treatment and drugs participating in treatment and procedures.'''

    dataset = store.resource(str(DDIEM.DDIEM))
    dataset.add(RDF.type, VOID.Dataset)
    dataset.add(FOAF.homepage, store.resource('http://ddiem.phenomebrowser.net/'))
    dataset.add(FOAF.page,  store.resource('https://github.com/bio-ontology-research-group/DDIEM'))
    dataset.add(DCTERMS.title, Literal('DDIEM - Drug Database for Inborn Error of Metabolism'))
    dataset.add(DCTERMS.description, Literal(description))

    kaust = store.resource('https://www.kaust.edu.sa')
    kaust.add(RDF.type, FOAF.Organization)
    kaust.add(RDFS.label, Literal('King Abdullah University of Science and Technology'))

    uoc = store.resource('https://www.pdn.cam.ac.uk')
    uoc.add(RDF.type, FOAF.Organization)
    uoc.add(RDFS.label, Literal('University of Cambridge'))

    dataset.add(DCTERMS.contributor, kaust)
    dataset.add(DCTERMS.contributor, uoc)

    robert = store.resource("https://www.kaust.edu.sa/RobertHoehndorf")
    robert.add(RDF.type, FOAF.Person)
    robert.add(RDFS.label, Literal('Robert Hoehndorf'))
    robert.add(FOAF.mbox, store.resource('mailto:robert.hoehndorf@kaust.edu.sa'))
    dataset.add(DCTERMS.creator, robert)

    marwa = store.resource("https://www.kaust.edu.sa/MarwaAbdelhakim")
    marwa.add(RDF.type, FOAF.Person)
    marwa.add(RDFS.label, Literal('Marwa Abdelhakim'))
    marwa.add(FOAF.mbox, store.resource('mailto:marwa.abdelhakim@kaust.edu.sa'))
    dataset.add(DCTERMS.creator, marwa)

    allan = store.resource("https://www.kaust.edu.sa/AllanKamau")
    allan.add(RDF.type, FOAF.Person)
    allan.add(RDFS.label, Literal('Allan Kamau'))
    allan.add(FOAF.mbox, store.resource('mailto:allan.kamau@kaust.edu.sa'))
    dataset.add(DCTERMS.creator, allan)

    ali = store.resource("https://www.kaust.edu.sa/AliRazaSyed")
    ali.add(RDF.type, FOAF.Person)
    ali.add(RDFS.label, Literal('Ali Raza Syed'))
    ali.add(FOAF.mbox, store.resource('mailto:ali.syed@kaust.edu.sa'))
    dataset.add(DCTERMS.creator, ali)

    senay = store.resource("https://www.kaust.edu.sa/SenayKafkas")
    senay.add(RDF.type, FOAF.Person)
    senay.add(RDFS.label, Literal('Senay Kafkas'))
    senay.add(FOAF.mbox, store.resource('mailto:senay.kafkas@kaust.edu.sa'))
    dataset.add(DCTERMS.creator, senay)

    paul = store.resource("https://www.pdn.cam.ac.uk/PaulSchofield")
    paul.add(RDF.type, FOAF.Person)
    paul.add(RDFS.label, Literal('Dr Paul Schofield'))
    paul.add(FOAF.mbox, store.resource('mailto:pns12@cam.ac.uk'))
    dataset.add(DCTERMS.creator, paul)

    eunice = store.resource("https://www.pdn.cam.ac.uk/EuniceMcMurray")
    eunice.add(RDF.type, FOAF.Person)
    eunice.add(RDFS.label, Literal('Eunice McMurray'))
    eunice.add(FOAF.mbox, store.resource('mailto:eym24@cam.ac.uk'))

    dataset.add(DCTERMS.modified, Literal(str(datetime.date.today())))
    dataset.add(VOID.sparqlEndpoint, store.resource('http://ddiem.phenomebrowser.net/sparql'))
    dataset.add(DCTERMS.license, store.resource('https://creativecommons.org/licenses/by/4.0/'))
    dataset.add(VOID.feature, store.resource('http://www.w3.org/ns/formats/RDF_XML'))

    # Serialize the file to rdf/xml representation
    store.serialize("../../../../data/VOID.{date}.rdf".format(date=str(datetime.date.today())), format="pretty-xml", max_depth=3)

    store.load("../../../../data/ddiem.owl")

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

    def pubchem_drug(drug_id, drug_name):
        global drug_dict
        if encrypt_string(drug_id) not in drug_dict :
            drug_res = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
            drug_res.set(RDF.type, DDIEM.Drug)
            drug_res.set(DC.identifier, Literal(drug_id))
            drug_res.set(RDFS.label, Literal(drug_name))
            drug_number = drug_id.split(":")[1] if drug_id.find(":") > -1 else None
            drug_res.add(DDIEM.url, Literal("https://pubchem.ncbi.nlm.nih.gov/compound/" + drug_number)) if drug_id.startswith("CID:") else None
            drug_dict[encrypt_string(drug_id)] = drug_res
            return drug_res
        else :
            return drug_dict[encrypt_string(drug_id)]

    with open(DDIEM_SOURCE_FILE, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        use_drug_name = False
        for row in csv_reader:
            if line_count == 1:
                print("Column names are :" + ", ".join(row))
            elif line_count > 1:
                disease_id_col = row[1].replace('#', '').replace('*', '').replace('%', '').strip()
                if not disease_id_col:
                    print("Empty disease id column:" + disease_id_col)
                    line_count += 1
                    continue
                
                na_drug_index_col = row[60].strip()
                pubchem_cid_or = row[47].strip()
                pubchem_cid_or_name = row[48].strip()
                pubchem_sid_or = row[49].strip()
                pubchem_cid_and = row[53].strip()
                pubchem_cid_and_name = row[54].strip()
                pubchem_sid_and = row[55].strip()
                drug_comb_col = (row[24].strip() if row[24] else '') + (row[25].strip() if row[25] else '') + (row[26].strip() if row[26] else '') 
                drug_comb_col += (row[28].strip() if row[28] else '') + (row[29].strip() if row[29] else '') + (row[30].strip() if row[30] else '')
                drug_comb_col += (pubchem_cid_or if pubchem_cid_or else '') + (pubchem_cid_and if pubchem_cid_and else '')
                # + (pubchem_sid_and if pubchem_sid_and else '') + (pubchem_sid_or if pubchem_sid_or else '')

                # print("iembase number:" + row[42]) if ',' in row[42] else None
                # print("drug_comb_col:" + drug_comb_col)
                if drug_comb_col.strip():
                    use_drug_name = False
                
                drug_name = row[19]
                if (not drug_comb_col.strip() or drug_comb_col.strip() == 'NA') and drug_name.strip():
                    drug_comb_col = drug_name
                    use_drug_name = True

                disease = None
                if disease_id_col not in disease_dict :
                    disease = store.resource(str(DDIEM.uri) +  disease_id_col)
                    disease.set(RDF.type, DDIEM.Disease)
                    disease.set(RDFS.label, Literal(row[5]))
                    disease.set(RDFS.comment, Literal(row[9]))

                    iembase_id_col = row[43]
                    if iembase_id_col.strip():
                        disease.set(DDIEM.iembaseAccessionNumber, Literal(iembase_id_col))
                        disease.set(DDIEM.iembaseUrl, Literal('http://iembase.org/app/#!/disorder/' + iembase_id_col))
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

                    for ecNumber in row[46].split(","):
                        protein_enzyme.add(DDIEM.ecNumber, Literal(ecNumber.strip())) if ecNumber.strip() and not ('""' in ecNumber.strip()) else None

                    for uniprotId in row[44].split(","):
                        protein_enzyme.add(DDIEM.uniprotId, Literal(uniprotId.strip())) if uniprotId.strip() else None

                    for keggEntryId in row[45].split(","):
                        protein_enzyme.add(DDIEM.keggEntryId, Literal(keggEntryId.strip())) if keggEntryId.strip() else None

                    protien_dict[encrypt_string(row[protein_enzyme_col])] = protein_enzyme
                else :
                    protein_enzyme = protien_dict[encrypt_string(row[protein_enzyme_col])]

                gene_col=11
                gene_id_col=41
                gene_split_count=0
                gene_ids=row[gene_id_col].split(",")
                # print(row[gene_col], row[gene_id_col], row[41])
                for geneCode in row[gene_col].split(","):
                    if not geneCode.strip():
                        continue

                    if geneCode not in gene_dict :
                        gene = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                        gene.set(RDF.type, DDIEM.Gene)
                        gene.set(RDFS.label, Literal(geneCode))
                        gene.add(DC.identifier, Literal("https://www.ncbi.nlm.nih.gov/gene/" + gene_ids[gene_split_count] if gene_ids[gene_split_count] else "https://ghr.nlm.nih.gov/gene/" + geneCode))
                        disease.set(OBO.RO_0004020, gene)
                        gene_dict[geneCode] = gene
                    else :
                        disease.add(OBO.RO_0004020, gene_dict[geneCode])

                    if gene_dict[geneCode] not in store.objects(protein_enzyme, OBO.RO_0002204):
                        protein_enzyme.add(OBO.RO_0002204, gene_dict[geneCode])
                    
                    gene_split_count+=1

                
                if not drug_comb_col.strip() or drug_comb_col.strip().lower() == "No treatment is available in DDIEM".lower():
                    #print("disease dont have treatment :" + disease_id_col)
                    line_count += 1
                    continue

                drug_id_org_col=20
                procedure_instances=[]
                for id in row[drug_id_org_col].split("+"):
                    procedure_instances.append(id.strip())

                procedure_type_col=35
                procedure_type_list = []
                if row[procedure_type_col].strip():
                    for procedure_type in row[procedure_type_col].split("+"):
                        for procedure_type_class in store.subjects(RDFS.label, Literal(procedure_type.strip(), lang='en')):
                            procedure_type_list.append(procedure_type_class)

                procedure_id = disease_id_col + ":" + drug_comb_col
                if encrypt_string(procedure_id) not in procedure_dict :
                    procedure = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                    procedure.add(RDF.type, OBO.OGMS_0000112)
                    procedure.set(RDFS.comment, Literal(row[18]))
                    procedure.set(OBO.RO_0002599, disease)
                    procedure_dict[encrypt_string(procedure_id)] = procedure

                    if len(procedure_instances) > 1:
                        procedure.add(RDF.type, OBO.DDIEM_0000023)
                        count=0
                        for instance in procedure_instances:
                            instance = instance.replace('CHEBI:','CHEBI_')
                            procedure_ins = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                            procedure_ins.add(RDF.type, OBO.OGMS_0000112)
                            procedure.add(OBO.BFO_0000050, procedure_ins)
                            # print(disease_id_col, procedure_instances, procedure_type_list,(count + 1))
                            procedure_ins.add(RDF.type, procedure_type_list[(count + 1)]) if count < (len(procedure_type_list) + 1) else None
                            
                            if count == 0 and ((row[24].strip() if row[24] else '') + (row[25].strip() if row[25] else '') 
                            + (row[26].strip() if row[26] else '') + (pubchem_cid_or if pubchem_cid_or else '')): 
                                add_ored_drugs(row, procedure_ins, pubchem_cid_or, pubchem_cid_or_name)
                            else:
                                #drug and columns
                                for drug_col in row[28:31]:
                                    if not drug_col.strip():
                                        continue
                                    
                                    drug_col = drug_col.replace('(','').replace(')','')
                                    for item in drug_col.split(','):
                                        if instance.find(item.strip()) == -1 or item.strip() == 'NA':
                                            continue
                                        
                                        drug_res = drug(item.strip())  
                                        drug_res.add(OBO.RO_0000056, procedure_ins)
                                        procedure_ins.add(OBO.RO_0000057, drug_res)
                                        
                                if pubchem_cid_and:
                                    names = pubchem_cid_and_name.split(',')
                                    pubchem_count = 0
                                    print("and:", pubchem_cid_and, "|", pubchem_cid_and_name)
                                    for item in pubchem_cid_and.split(','):
                                        if instance.find(item.strip()) == -1 or item.strip() == 'NA':
                                            continue

                                        drug_res = pubchem_drug(item.strip(), names[pubchem_count]) 
                                        pubchem_count += 1
                                        drug_res.add(OBO.RO_0000056, procedure_ins)
                                        procedure_ins.add(OBO.RO_0000057, drug_res)
                                        
                                drug_names = drug_name.split('+')
                                for na_drug_idx in na_drug_index_col.split(','):
                                    if instance.find('NA') == -1:
                                        continue
                                    if not na_drug_idx or (na_drug_idx and int(na_drug_idx) > len(drug_names) ):
                                        continue
                                    if count != (int(na_drug_idx) - 1):
                                        continue

                                    # print(instance, disease_id_col, drug_names, na_drug_index_col, procedure_instances)
                                    name = drug_names[int(na_drug_idx) - 1] 
                                    drug_res = drug_by_name(name.strip()) 
                                    drug_res.add(OBO.RO_0000056, procedure_ins)
                                    procedure_ins.add(OBO.RO_0000057, drug_res)
                            
                            count += 1
                    else:
                        if len(procedure_type_list) > 0:
                            procedure.add(RDF.type, procedure_type_list[0])

                        if use_drug_name:
                            drug_res = drug_by_name(drug_name.strip())
                            drug_res.add(OBO.RO_0000056, procedure)
                            procedure.add(OBO.RO_0000057, drug_res)
                        else:
                            add_ored_drugs(row, procedure, pubchem_cid_or, pubchem_cid_or_name)
                        
                
                for evidenceStr in row[32].split(','):
                    evidenceStr = evidenceStr.strip().replace(" ", "")
                    if evidenceStr:
                        evidence = store.resource(str(DDIEM.uri) + evidenceStr)
                        evidence.set(RDF.type, DDIEM.Evidence)
                        evidence.set(DC.identifier, Literal(evidenceStr))
                        evidence.set(DDIEM.url, Literal("http://purl.obolibrary.org/obo/" + evidenceStr.replace(":", "_")))
                        if evidence and evidence not in store.objects(procedure_dict[encrypt_string(procedure_id)], OBO.RO_0002558) :
                            procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0002558, evidence)
        
                for referenceStr in row[40].split(","):
                    referenceStr = referenceStr[0:referenceStr.index('?')] if referenceStr.find('?') > -1 and 'scholar.google.com' not in referenceStr else referenceStr
                    referenceStr = referenceStr[0:referenceStr.rindex('/')] if referenceStr.rfind('/') > -1 and referenceStr.rfind('/') == len(referenceStr) - 1 else referenceStr
                    referenceLiteral = Literal(referenceStr.strip()) if referenceStr.strip() else None
                    if referenceLiteral and referenceLiteral not in store.objects(procedure_dict[encrypt_string(procedure_id)], DC.provenance) :
                        procedure_dict[encrypt_string(procedure_id)].add(DC.provenance, referenceLiteral)

                phenotype_col_id=37
                phenotype = None
                if row[phenotype_col_id].strip():
                    if encrypt_string(row[phenotype_col_id]) not in pheno_dict :
                        phenotype = store.resource(str(DDIEM.uri) + str(uuid.uuid4()))
                        phenotype.set(RDF.type, DDIEM.Phenotype)
                        phenotype.set(RDFS.label, Literal(row[phenotype_col_id]))
                        phenotype.set(RDFS.comment, Literal(row[39]))
                        if row[38].strip() and row[37].strip() != 'NA':
                            phenotype.add(DC.identifier, Literal(row[38]))
                            phenotype.add(DDIEM.url, Literal("http://purl.obolibrary.org/obo/" + row[38].replace(":", "_").replace("*", "")))
                        pheno_dict[encrypt_string(row[phenotype_col_id])] = phenotype
                    else :
                        phenotype = pheno_dict[encrypt_string(row[phenotype_col_id])]

                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0002212, phenotype)

                #mutation or genetype elements
                if row[33].strip():
                    procedure_dict[encrypt_string(procedure_id)].add(OBO.RO_0003304, Literal(row[33].strip()))
                if row[34].strip():
                    procedure_dict[encrypt_string(procedure_id)].add(DDIEM.failedToContributeToCondition, Literal(row[34].strip()))
        
            line_count += 1

        print("Processed " + str(line_count) + " lines.")

    # Serialize the file to rdf/xml representation
    store.serialize("../../../../data/ddiem-data.{data}.rdf".format(data=str(datetime.date.today())), format="pretty-xml", max_depth=3)
