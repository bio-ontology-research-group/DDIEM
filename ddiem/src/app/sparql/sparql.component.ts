import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-sparql',
  templateUrl: './sparql.component.html',
  styleUrls: ['./sparql.component.css']
})
export class SparqlComponent implements OnInit {

  formats = [
    {name: 'HTML',  format:'text/html'},
    {name: 'XML',  format:'application/sparql-results+xml'},
    {name: 'JSON',  format:'application/sparql-results+json'},
    {name: 'Javascript',  format:'application/javascript'},
    {name: 'Turtle',  format:'text/turtle'},
    {name: 'RDF/XML',  format:'application/rdf+xml'},
    {name: 'N-Triples',  format:'text/plain'},
    {name: 'CSV',  format:'text/csv'},
    {name: 'TSV',  format:'text/tab-separated-values'}
  ];

  format: any = {name: 'HTML',  format:'text/html'};
  @ViewChild("htmlForm")
  htmlForm: ElementRef;
  @ViewChild("sparqlEle")
  sparqlEle: ElementRef;

  constructor() { }

  ngOnInit() {
    this.diseaseList();
  }

  submit(){
    this.htmlForm.nativeElement.submit();
  }

  clear(){
    this.sparqlEle.nativeElement.value = '';
  }

  diseaseList() {
    var query = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
SELECT ?disease ?label
FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
WHERE {
  ?disease rdf:type ddiem:Disease . 
  ?disease rdfs:label ?label
} ORDER BY 1 LIMIT 10`;
    this.sparqlEle.nativeElement.value = query;
  }

  diseaseByName() {
    var query = `SELECT DISTINCT  ?OMIM_ID ?disease_name ?phenotype_improved_by_treatment__object
        FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
        WHERE {
            ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_entry .
            ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_ID .
            ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_disease_name> ?disease_name .
            ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_row_id> ?clinical_outcome_log_id .
            ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_phenotype_improved_by_treatment__bag> ?phenotypes_improved_by_treatment .
            ?phenotypes_improved_by_treatment rdf:rest* ?phenotype_improved_by_treatment .
            ?phenotype_improved_by_treatment ?phenotype_improved_by_treatment__predicate ?phenotype_improved_by_treatment__object .
            FILTER (?disease_name="HYPERPHENYLALANINEMIA, BH4-DEFICIENT, C; HPABH4C"^^xsd:string)
            FILTER (?phenotype_improved_by_treatment__predicate != rdf:type)
      } ORDER BY 1 2 3 LIMIT 10`;
      this.sparqlEle.nativeElement.value = query;
  }
	
  treatmentImprovedPhenotypes() {
    var query = `SELECT DISTINCT ?BORG_DDIEM__clinical_logs__version ?clinical_outcome_log_id ?OMIM_ID ?disease_name ?phenotype_improved_by_treatment__object ?RO_0002302
      FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
      WHERE {
          ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/BORG_DDIEM__clinical_logs__version> ?BORG_DDIEM__clinical_logs__version .
          ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_entry .
          ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_ID .
          ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_disease_name> ?disease_name .
          ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_row_id> ?clinical_outcome_log_id .
          ?x <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_phenotype_improved_by_treatment__bag> ?phenotypes_improved_by_treatment .
          ?phenotypes_improved_by_treatment rdf:rest* ?phenotype_improved_by_treatment .
          ?phenotype_improved_by_treatment ?phenotype_improved_by_treatment__predicate ?phenotype_improved_by_treatment__object .
          ?x <http://purl.obolibrary.org/obo/RO_0002302> ?RO_0002302 .
          ?RO_0002302 ?RO_0002302__predicate ?RO_0002302__object .
          FILTER (?disease_name="HYPERPHENYLALANINEMIA, BH4-DEFICIENT, C; HPABH4C"^^xsd:string && ?phenotype_improved_by_treatment__object = "Abnormality of neurotransmitter metabolism"^^xsd:string)
          FILTER (?phenotype_improved_by_treatment__predicate != rdf:type)
      } ORDER BY 1 2 3 4 LIMIT 10`;
      this.sparqlEle.nativeElement.value = query;
  }


  drugByRegimen() {
    var query = `SELECT DISTINCT ?oo ?p ?drug_entry__uri# ?drug_entry_property_name ?drug_entry_property_value
      WHERE {
          ?regimen__consistsOf__uri ?p ?drug_entry__uri .
          ?drug_entry__uri ?drug_entry_property_name ?drug_entry_property_value 
          {
              SELECT DISTINCT ?regimen__consistsOf__uri ?oo
              FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
              WHERE {
                <http://www.cbrc.kaust.edu.sa/ddiem/regimen/042db1ac0f7eb035c3d2d6db45b6b76e355d0cefb577ead3c46acbe96e6b8db2> ?p ?regimen__consistsOf__uri .
                ?regimen__consistsOf__uri ?op ?oo .
                #?drug_entry ?drug_entry__predicate ?drug_entry__object . 
                FILTER (?oo=<http://www.cbrc.kaust.edu.sa/ddiem/terms/DrugNonAlternative>) .
              }
          }
          FILTER (?p=<http://www.cbrc.kaust.edu.sa/ddiem/terms/nonoptional>) .
        } ORDER BY 1 2 3`;
    this.sparqlEle.nativeElement.value = query;
  }

}
