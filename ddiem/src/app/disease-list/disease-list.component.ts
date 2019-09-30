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

  constructor(private router: Router,
              private titlecasePipe:TitleCasePipe,
              private route: ActivatedRoute,
              private service: DiseaseService) { 
    
    this.route.params.subscribe( params => {
      console.log("param:", params.iri)
      if (params.iri) {
        this.drugIri = decodeURIComponent(params.iri);
        this.service.listDiseasesByDrug(params.iri).subscribe(data => { 
          this.diseaseLinksList = data;
        });
      }
    });
  }

  ngOnInit() {
    console.log("drugIri:", this.drugIri)
    this.service.listDiseasesAndDrugs().subscribe(data => {
      this.diseaseList = data;
      if (!this.drugIri) {
        this.diseaseLinksList = _.filter(data, (obj) => obj.type.value === 'http://ddiem.phenomebrowser.net/Disease');
      }
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

  onDiseaseSelectNewTab(diseaseOrDrug) {
    console.log(diseaseOrDrug.resource)
    this.router.navigate([]).then(result => {  window.open('/disease/' + encodeURIComponent(encodeURIComponent(diseaseOrDrug.resource.value)), '_blank'); });
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }

  openInNewTab(url: string){
    console.log(url);
    window.open(url, "_blank");
  }

}
