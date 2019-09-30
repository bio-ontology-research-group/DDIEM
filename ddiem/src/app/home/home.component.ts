import { Component, OnInit } from '@angular/core';
import { DiseaseService } from '../disease.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers:  [ DiseaseService ]
})
export class HomeComponent implements OnInit {

  diseaseList: any = [];

  constructor(private router: Router,
              private service: DiseaseService) { }

  ngOnInit() {
    this.service.listDiseasesAndDrugs().subscribe(data => {
      this.diseaseList = data;
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

}
