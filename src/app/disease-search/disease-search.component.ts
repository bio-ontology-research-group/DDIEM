import { Component, OnInit, Input, Output, EventEmitter, SimpleChange } from '@angular/core';
import { Observable } from 'rxjs';
import {debounceTime, distinctUntilChanged, map} from 'rxjs/operators';
import { Router } from '@angular/router';
import { TitleCasePipe } from '@angular/common';

@Component({
  selector: 'app-disease-search',
  templateUrl: './disease-search.component.html',
  styleUrls: ['./disease-search.component.css']
})
export class DiseaseSearchComponent implements OnInit {

  @Input() diseaseList: any = [];
  @Output() selectedDisease = new EventEmitter<any>();

  disease = null;

  formatter: any;
  
  search = (text$: Observable<string>) =>
        text$.pipe(
          debounceTime(200),
          distinctUntilChanged(),
          map(term => term.length < 2 ? []
            : this.diseaseList.filter(v => v.label.value.toLowerCase().indexOf(term.toLowerCase()) > -1).slice(0, 10))
        )

  constructor(private router: Router,
              private titlecasePipe:TitleCasePipe) { }

  ngOnInit() {
    this.formatter = (x: {label: { value: string}}) => x.label ? this.toTitleCase(x.label.value) : null;
  }

  ngOnChanges(change: SimpleChange) {
    if(change.currentValue && change.currentValue.diseaseList) {
      // this.formatter = (x: {label: { value: string}}) => x.label.value;
    }
  }

  onDiseaseSelect(event){
    this.selectedDisease.emit(event.item);
  }

  toTitleCase(text){
    return this.titlecasePipe.transform(text);
  }
  
}
