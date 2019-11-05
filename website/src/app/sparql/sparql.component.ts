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
FROM <http://ddiem.phenomebrowser.net>
WHERE {
  ?disease rdf:type ddiem:Disease . 
  ?disease rdfs:label ?label
} ORDER BY 1 LIMIT 10`;
    this.sparqlEle.nativeElement.value = query;
  }

  diseaseByName() {
    var query = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX obo: <http://purl.obolibrary.org/obo/>

  SELECT ?identifier ?label ?gene ?comment
  FROM <http://ddiem.phenomebrowser.net>
  WHERE {
    ?disease rdf:type ddiem:Disease;
              rdfs:label ?label;
              obo:RO_0004020 ?gene;
              dc:identifier ?identifier;
              rdfs:comment ?comment .
    FILTER (?label="MUSCULAR DYSTROPHY-DYSTROGLYCANOPATHY (CONGENITAL WITH BRAIN AND EYE ANOMALIES), TYPE A, 9; MDDGA9")
  }`;
      this.sparqlEle.nativeElement.value = query;
  }
	
  proceduresByDisease() {
    var query = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    
    SELECT ?procedure ?comment ?evidenceCode ?typeName ?phenotypeCorrected ?provenance
    FROM <http://ddiem.phenomebrowser.net>
    WHERE {
    <http://ddiem.phenomebrowser.net/210200> rdf:type ddiem:Disease .
    ?procedure obo:RO_0002606 <http://ddiem.phenomebrowser.net/210200>;
                rdf:type ddiem:TheraputicProcedure;
                obo:RO_0002558 ?evidenceCode;
                obo:RO_0002212 ?phenotype;
                dc:provenance ?provenance;
                rdfs:comment ?comment .
    OPTIONAL {
      ?procedure rdfs:subClassOf ?type .
      ?type rdfs:label ?typeName .
    } . 
    ?phenotype rdfs:label ?phenotypeCorrected .
    }`;
    this.sparqlEle.nativeElement.value = query;
  }


  drugParticipatedInProcedure() {
    var query = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    
    SELECT ?drugName ?drugId
    FROM <http://ddiem.phenomebrowser.net>
    WHERE {
      ddiem:3204771e-9e7e-49dd-9c30-15c2c6c95f11 rdf:type ddiem:TheraputicProcedure;
      obo:RO_0000057 ?drugContainer .
      ?drugContainer (rdf:_1|rdf:_2|rdf:_3) ?drug .
      ?drug rdfs:label ?drugName;
            dc:identifier ?drugId .
    }`;
    this.sparqlEle.nativeElement.value = query;
  }

}
