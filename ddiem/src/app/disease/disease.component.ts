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
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })
  }

  onDiseaseSelect(disease){
    this.router.navigate(['/disease', encodeURIComponent(disease.disease.value)]);
  }

  initDisease(iri) {
    this.service.getDiseases(iri).subscribe(data => { 
      this.disease = data ? data["@graph"] : null;
      this.context = data ? data["@context"] : null;
    
      this.service.getDiseasePhenotypes(iri).subscribe(phenotypesData => {
        this.phenotypes = phenotypesData ? phenotypesData["@graph"] : null;   
        console.log(this.phenotypes);
      });

      this.service.getDiseaseDrugs(iri).subscribe(drugsData => {
        this.drugs = drugsData ? drugsData["@graph"] : null;    
        console.log(this.drugs);
      });

      this.procedures = _.filter(this.disease, (obj) => obj['@type'].includes("ddiem:TheraputicProcedure"));
      this.isMutationExists = _.filter(this.disease, (obj) => obj['obo:RO_0003304'] || obj['ddiem:failedToContributeToCondition']).length > 0
      console.log(this.disease, this.procedures);
    });
  }

  find(id) {
    return _.findWhere(this.disease, {'@id': id});
  }

  //Finds Disease object
  d(){
    if (this.iri.startsWith(this.context.ddiem)) {
      return this.find("ddiem:" + this.iri.substr(this.iri.lastIndexOf('/') + 1));
    } 
    return null;
  }

  gene() {
    return this.find(this.d()['obo:RO_0004020'][0]['@id']);
  }

  protienEffected() {
    var geneId = this.gene()['@id'];
    return _.find(this.disease, (obj) => obj['obo:RO_0002204'] && obj['obo:RO_0002204'][0]['@id'] === geneId);
  }

  ecNumber() {
    var protien = this.protienEffected()
    if (protien) {
      if (protien['ddiem:ecNumber'][0]['@value'] !== "" && protien['ddiem:uniprotId'][0]['@value'] !== "")  {
        return protien['ddiem:ecNumber'][0]['@value'] + " / " + protien['ddiem:uniprotId'][0]['@value'];
      } else if (protien['ddiem:ecNumber'][0]['@value'] !== "") {
        return protien['ddiem:ecNumber'][0]['@value'];
      } else {
        return protien['ddiem:uniprotId'][0]['@value'];
      }
    }
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
    if (url.startsWith(this.context.pubmed)) {
      return "pubmed:" + url.substr(url.lastIndexOf('/') + 1)
    } else {
      return 'Clinical trials';
    }
  }

  evidenceName(name) {
    return name.substr(name.indexOf(':') + 1);
  }

  openInNewTab(url: string){
    window.open(url, "_blank");
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }
}
