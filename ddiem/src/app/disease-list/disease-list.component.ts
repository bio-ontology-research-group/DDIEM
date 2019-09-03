import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { DiseaseService } from '../disease.service';
import { Router } from '@angular/router';
import { TitleCasePipe } from '@angular/common';

@Component({
  selector: 'app-disease-list',
  templateUrl: './disease-list.component.html',
  styleUrls: ['./disease-list.component.css'],
  providers:  [ DiseaseService ]
})
export class DiseaseListComponent implements OnInit {

  diseaseList: any = [];

  constructor(private router: Router,
              private titlecasePipe:TitleCasePipe,
              private service: DiseaseService) { }

  ngOnInit() {
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })

  }

  onDiseaseSelect(disease){
    console.log(disease.disease)
    this.router.navigate(['/disease', encodeURIComponent(disease.disease.value)]);
  }

  onDiseaseSelectNewTab(disease) {
    console.log(disease.disease)
    this.router.navigate([]).then(result => {  window.open('/disease/' + encodeURIComponent(encodeURIComponent(disease.disease.value)), '_blank'); });
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }

}
