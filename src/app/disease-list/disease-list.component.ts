import { Component, OnInit } from '@angular/core';
import { DiseaseService } from '../disease.service';
import { Router, ActivatedRoute } from '@angular/router';
import { TitleCasePipe } from '@angular/common';
import { _ } from 'underscore';

@Component({
  selector: 'app-disease-list',
  templateUrl: './disease-list.component.html',
  styleUrls: ['./disease-list.component.css'],
  providers:  [ DiseaseService ]
})
export class DiseaseListComponent implements OnInit {

  diseaseList: any = [];
  diseaseLinksList: any = [];
  drugIri: any;
  modeIri: any;

  constructor(private router: Router,
              private titlecasePipe:TitleCasePipe,
              private route: ActivatedRoute,
              private service: DiseaseService) { 
    
    this.route.params.subscribe( params => {
      this.drugIri = null;
      this.modeIri = null;
      if (params.iri && params.type) {
        if (decodeURIComponent(params.type) === 'http://ddiem.phenomebrowser.net/Drug') {
          this.drugIri = decodeURIComponent(params.iri);
          this.service.listDiseasesByDrug(params.iri).subscribe(data => { 
            this.diseaseLinksList = data;
          });
        } else {
          this.modeIri = decodeURIComponent(params.iri);
          this.service.listDiseasesByMode(params.iri).subscribe(data => { 
            this.diseaseLinksList = data;
          });
        }
      }
    });
  }

  ngOnInit() {
    this.service.listLookupResoruces().subscribe(data => {
      this.diseaseList = data;
      if (!this.drugIri && !this.modeIri) {
        this.diseaseLinksList = _.filter(data, (obj) => obj.type.value === 'http://ddiem.phenomebrowser.net/Disease');
      }
    })
  }

  onDiseaseSelect(lookupResource){
    console.log(lookupResource.resource)
    if (lookupResource.type.value === 'http://ddiem.phenomebrowser.net/Disease') {
      this.router.navigate(['/disease', encodeURIComponent(lookupResource.resource.value)]);
    } else {
      this.router.navigate(['/disease-list-by-resource', encodeURIComponent(lookupResource.resource.value), encodeURIComponent(lookupResource.type.value)]);
    }
  }

  onDiseaseSelectNewTab(lookupResource) {
    console.log(lookupResource.resource)
    this.router.navigate([]).then(result => {  window.open('/disease/' + encodeURIComponent(encodeURIComponent(lookupResource.resource.value)), '_blank'); });
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }

  openInNewTab(url: string){
    console.log(url);
    window.open(url, "_blank");
  }

}
