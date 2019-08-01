import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
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
  selectedDisease : any;

  constructor(private route: ActivatedRoute,
              private service: DiseaseService) {
    this.route.params.subscribe( params => {
      this.service.getDiseases(params.iri).subscribe(data => { 
        this.disease = data ? data["@graph"] : null;
        this.context = data ? data["@context"] : null;
        this.datasets = this.findDatasets();
        var drugCompositionIdSet = new Set();

        for (var i=0; i < this.datasets.length; i++) {
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
    });
  }

  ngOnInit() {
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })
  }

  onDiseaseSelect(event){
    console.log(event);
  }

  find(id) {
    return _.findWhere(this.disease, {'@id': id});
  }

  gene() {
    return this.find(this.disease[0]['obo:RO_0004020'][0]['@id']);
  }

  ec_number() {
    if (this.gene()['obo:RO_0002205'] && this.gene()['obo:RO_0002205'][0]['@id']){ 
      var ecNumber = this.find(this.gene()['obo:RO_0002205'][0]['@id']);
      return ecNumber &&  ecNumber['ddiem:has_ec_number'] ? ecNumber['ddiem:has_ec_number'][0]['@value'] : '';
    }
  }

  findDatasets(){
    return _.filter(this.disease, (item) => {
      if (item['ddiem:has_omim_id'] && !item['ddiem:has_disease_name'] 
            && item['ddiem:has_omim_id'][0]['@id'] === this.disease[0]['@id']) {
        return true;
      } else { 
        return false;
      }
    });
  }

  phenotype(ds) {
    if (ds['ddiem:has_phenotype_improved_by_treatment__bag']) {
      return this.find(ds['ddiem:has_phenotype_improved_by_treatment__bag'][0]['@id'])['rdf:_1'][0]['@value'];
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

  search = (text$: Observable<string>) =>
    text$.pipe(
      debounceTime(200),
      distinctUntilChanged(),
      map(term => term.length < 2 ? []
        : this.diseaseList.filter(v => v.disease_name.value.toLowerCase().indexOf(term.toLowerCase()) > -1).slice(0, 10))
    )

  formatter = (x: {disease_name: { value: string}}) => x.disease_name.value;
}
