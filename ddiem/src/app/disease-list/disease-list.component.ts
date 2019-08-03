import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { DiseaseService } from '../disease.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-disease-list',
  templateUrl: './disease-list.component.html',
  styleUrls: ['./disease-list.component.css'],
  providers:  [ DiseaseService ]
})
export class DiseaseListComponent implements OnInit {

  diseaseList: any = [];

  constructor(private router: Router,
              private service: DiseaseService) { }

  ngOnInit() {
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })

  }

  onDiseaseSelect(disease){
    this.router.navigate(['/disease', encodeURIComponent(disease.OMIM_entry.value)]);
  }

  onDiseaseSelectNewTab(disease) {
    console.log(encodeURIComponent(disease.OMIM_entry.value), disease.OMIM_entry.value);
    this.router.navigate([]).then(result => {  window.open('/disease/' + encodeURIComponent(encodeURIComponent(disease.OMIM_entry.value)), '_blank'); });
  }

}
