import { Component, OnInit, Input, Output, EventEmitter, SimpleChange } from '@angular/core';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { Router } from '@angular/router';

@Component({
  selector: 'app-disease-search',
  templateUrl: './disease-search.component.html',
  styleUrls: ['./disease-search.component.css']
})
export class DiseaseSearchComponent implements OnInit {

  @Input() diseaseList: any = [];
  @Output() selectedDisease = new EventEmitter<any>();

  formatter: any;
  
  search = (text$: Observable<string>) =>
        text$.pipe(
          debounceTime(200),
          distinctUntilChanged(),
          map(term => term.length < 2 ? []
            : this.diseaseList.filter(v => v.disease_name.value.toLowerCase().indexOf(term.toLowerCase()) > -1).slice(0, 10))
        )

  constructor(private router: Router) { }

  ngOnInit() {
  }

  ngOnChanges(change: SimpleChange) {
    if(change.currentValue && change.currentValue.diseaseList) {
      this.formatter = (x: {disease_name: { value: string}}) => x.disease_name.value;
    }
  }

  onDiseaseSelect(event){
    this.selectedDisease.emit(event.item);
  }

  
}
