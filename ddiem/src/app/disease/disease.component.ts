import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import { DiseaseService } from '../disease.service';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { _ } from 'underscore';

@Component({
  selector: 'app-disease',
  templateUrl: './disease.component.html',
  styleUrls: ['./disease.component.css']
})
export class DiseaseComponent implements OnInit {
  disease : any = {};
  datasets : any = [];
  context : any = {};
  diseaseList: any = [];
  regimenTypes: any = new Set();
  selectedDisease : any;
  iri: any;

  constructor(private router: Router,
              private route: ActivatedRoute,
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
    this.router.navigate(['/disease', encodeURIComponent(disease.OMIM_entry.value)]);
  }

  initDisease(iri) {
    this.service.getDiseases(iri).subscribe(data => { 
      this.disease = data ? data["@graph"] : null;
      this.context = data ? data["@context"] : null;
      this.datasets = this.findDatasets();
      var drugCompositionIdSet = new Set();

      for (var i=0; i < this.datasets.length; i++) {
        if (this.datasets[i]['ddiem:has_regimen_mechanism_of_action__bag'] && this.datasets[i]['ddiem:has_regimen_mechanism_of_action__bag'][0]){
          var bag = this.find(this.datasets[i]['ddiem:has_regimen_mechanism_of_action__bag'][0]['@id']);
          bag && bag['rdf:_1'] ? this.regimenTypes.add(bag['rdf:_1'][0]['@value']) : null;
        }

        if (!this.datasets[i]['obo:RO_0002302']) {
          continue;
        }

        var drugCompId = this.datasets[i]['obo:RO_0002302'][0]['@id'];
        if (drugCompositionIdSet.has(drugCompId)) {
          continue;
        } 

        drugCompositionIdSet.add(drugCompId);
        this.service.getTreatmentDrug(drugCompId).subscribe(drugData => {
          var drugs = drugData ? drugData["@graph"] : null;
          if (drugs) {
            var drugObjs = _.filter(drugs, drug => drug['ddiem:has_name']);
            _.each(this.datasets, ds => { 
              if (!ds['obo:RO_0002302']) {
                return;
              }

              var id = _.findWhere(drugs, {'@id': ds['obo:RO_0002302'][0]['@id']});
              if (id) {
                ds.drugs = drugObjs;
              }
            });
          }         
        });
      }
      console.log(this.disease);
    });
  }

  find(id) {
    return _.findWhere(this.disease, {'@id': id});
  }

  //Finds Disease object
  d(){
    return this.find(this.iri);
  }

  gene() {
    return this.find(this.datasets[0]['obo:RO_0004020'][0]['@id']);
  }

  ec_number() {
    if (this.gene()['obo:RO_0002205']) {
      var ecIri = _.find(this.gene()['obo:RO_0002205'], (obj) => {
        if (!obj['@id']) {
          return false;
        }
        return obj['@id'].startsWith("ec:");
      });
      return ecIri ? ecIri['@id'].substr(ecIri['@id'].lastIndexOf(':') + 1) : '';
    }
  }

  findDatasets(){
    return _.filter(this.disease, (item) => {
      if (item['ddiem:has_omim_id'] && !item['ddiem:has_disease_name'] 
            && item['ddiem:has_omim_id'][0]['@id'] === this.iri) {
        return true;
      } else { 
        return false;
      }
    });
  }

  phenotype(ds) {
    if (ds['ddiem:has_phenotype_improved_by_treatment__bag']) {
      var phenotype = this.find(ds['ddiem:has_phenotype_improved_by_treatment__bag'][0]['@id']);
      return phenotype['rdf:_1'] ? phenotype['rdf:_1'][0]['@value'] : '';
    } 
    return '';
  }

  phenotypeUrl(ds) {
    if (ds['ddiem:has_phenotype_ID__collection']) {
      var phenotype = this.find(ds['ddiem:has_phenotype_ID__collection'][0]['@id']);
      var compactUri = phenotype['rdf:first'] ? phenotype['rdf:first'][0]['@id'] : '';
      if (compactUri.startsWith('obo:')) {
        return this.context.obo + compactUri.substr(compactUri.lastIndexOf(':') + 1);;
      }
    } 
    return '';
  }

  referenceDisplay(ds) {
    var ref = this.reference(ds);
    if (ref && ref.startsWith('pubmed:')) {
      return ref;
    } else if (ref) {
      return 'Clinical trials';
    }
    return '';
  }

  reference(ds) {
    if (ds['ddiem:treatment_manuscript_reference__collection']) {
      return this.find(ds['ddiem:treatment_manuscript_reference__collection'][0]['@id'])['rdf:first'][0]['@id'];
    }
    return null;
  }

  openPubmedRef(url: string){
    if (url.startsWith("pubmed:")) {
      url = this.context.pubmed + url.substr(url.lastIndexOf(':') + 1);
    }
    this.openInNewTab(url);
  }

  openInNewTab(url: string){
    window.open(url, "_blank");
  }
}
