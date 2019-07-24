import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { DiseaseService } from '../disease.service';

@Component({
  selector: 'app-disease-list',
  templateUrl: './disease-list.component.html',
  styleUrls: ['./disease-list.component.css'],
  providers:  [ DiseaseService ]
})
export class DiseaseListComponent implements OnInit {

  diseaseList: any = [];
  selectedDisease : any;

  constructor(private service: DiseaseService) { }

  ngOnInit() {
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })

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
