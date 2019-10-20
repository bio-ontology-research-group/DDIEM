import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import { DiseaseService } from '../disease.service';
import { _ } from 'underscore';
import { TitleCasePipe } from '@angular/common';

@Component({
  selector: 'app-disease',
  templateUrl: './disease.component.html',
  styleUrls: ['./disease.component.css']
})
export class DiseaseComponent implements OnInit {
  disease : any = {};
  phenotypes : any = [];
  drugs : any = [];
  procedures : any = [];
  proceduressData: any;
  genes : any = [];
  protienEffected : any = {};
  context : any = {};
  diseaseList: any = [];
  regimenTypes: any = new Set();
  selectedDisease : any;
  isMutationExists = false;
  iri: any;
  expasyUrl = "https://enzyme.expasy.org/EC/";
  uniprotUrl = "https://www.uniprot.org/uniprot/";

  constructor(private router: Router,
              private route: ActivatedRoute,
              private titlecasePipe:TitleCasePipe,
              private service: DiseaseService) {
    this.route.params.subscribe( params => {
      this.initDisease(params.iri);
      console.log(params.iri, decodeURIComponent(params.iri));
      this.iri = decodeURIComponent(params.iri);
    });
  }

  ngOnInit() {
    this.service.listDiseasesAndDrugs().subscribe(data => {
      this.diseaseList = data;
    })
  }

  onDiseaseSelect(diseaseOrDrug){
    console.log(diseaseOrDrug.resource)
    if (diseaseOrDrug.type.value === 'http://ddiem.phenomebrowser.net/Disease') {
      this.router.navigate(['/disease', encodeURIComponent(diseaseOrDrug.resource.value)]);
    } else {
      this.router.navigate(['/disease-list-by-drug', encodeURIComponent(diseaseOrDrug.resource.value)]);
    }
  }

  initDisease(iri) {
    this.service.getDiseases(iri).subscribe(data => { 
      this.disease = data ? data["@graph"] : null;
      this.context = data ? data["@context"] : null;
    
      this.service.getDiseaseProcedures(iri).subscribe(proceduressData => {
        this.proceduressData = proceduressData ? proceduressData["@graph"] : null;     
        this.procedures = _.filter(this.proceduressData, (obj) => obj['@type'].includes("ddiem:TheraputicProcedure"));
        console.log(this.procedures);
      });

      this.service.getDiseasePhenotypes(iri).subscribe(phenotypesData => {
        this.phenotypes = phenotypesData ? phenotypesData["@graph"] : null;   
        console.log(this.phenotypes);
      });

      this.service.getDiseaseDrugs(iri).subscribe(drugsData => {
        this.drugs = drugsData ? drugsData["@graph"] : null;    
        console.log(this.drugs);
      });
      
      this.genes = _.map(this.d()['obo:RO_0004020'], (gene) => this.find(gene['@id']));
      this.protienEffected = _.find(this.disease, (obj) => obj['obo:RO_0002204'] && _.findWhere(obj['obo:RO_0002204'], (value) => value['@id'] === this.genes[0]['@id']));
      this.isMutationExists = _.filter(this.disease, (obj) => obj['obo:RO_0003304'] || obj['ddiem:failedToContributeToCondition']).length > 0
      console.log(this.disease, this.genes, this.protienEffected);
    });
  }

  find(id:string) {
    return _.findWhere(this.disease, {'@id': id});
  }

  findProcedureData(id:string) {
    return _.findWhere(this.proceduressData, {'@id': id});
  }

  //Finds Disease object
  d(){
    if (this.iri.startsWith(this.context.ddiem)) {
      return this.find("ddiem:" + this.iri.substr(this.iri.lastIndexOf('/') + 1));
    } 
    return null;
  }

  ecNumberUri(number){ 
    return this.expasyUrl + number;
  }

  uniprotUri(number){ 
    return this.uniprotUrl + number;
  }

  findAltList(drugAltIri){
    var drugAlt = _.findWhere(this.drugs, {'@id': drugAltIri})
    if (drugAlt) {
      var drugs = _.map(
        _.filter(
          _.keys(drugAlt), (key) => key.includes('rdf:_')), (key) => {
            return _.findWhere(this.drugs, {'@id': drugAlt[key][0]['@id']})
          });
      return drugs;
    }
    return [];
  }

  phenotypeRes(iri) {
    return _.findWhere(this.phenotypes, {'@id': iri});
  }

  phenotypeUrl(iri) {
    if (this.phenotypeRes(iri)['ddiem:url']) {
      return "http://aber-owl.net/ontology/HP/#/Browse/" + encodeURIComponent("<" + this.phenotypeRes(iri)['ddiem:url'][0]['@value'] + ">");
    } 
    return '';
  }

  referenceDisplay(url) {
    if (url.startsWith(this.context.PMID) || url.startsWith(this.context.PMIDs)) {
      return "PMID:" + url.substr(url.lastIndexOf('/') + 1)
    } else if (url.startsWith(this.context.PMCID)) {
      return "PMCID:" + url.substr(url.lastIndexOf('/') + 1)
    } else if (url.startsWith(this.context.ClinicalTrials) 
        || url.startsWith(this.context.ClinicalTrial) 
        || url.startsWith(this.context.ClinicalTrialswww)) {
      return "Clinical trial ID:" + url.substr(url.lastIndexOf('/') + 1)
    } else {
      return 'Clinical trial';
    }
  }

  evidenceName(name) {
    return name.substr(name.indexOf(':') + 1);
  }

  evidenceUrl(iri) {
    if (iri && this.findProcedureData(iri)['ddiem:url']) {
      return "http://aber-owl.net/ontology/ECO/#/Browse/" + encodeURIComponent("<" + this.findProcedureData(iri)['ddiem:url'][0]['@value'] + ">");
    } 
    return '';
  }

  openInNewTab(url: string){
    console.log(url);
    window.open(url, "_blank");
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }
}