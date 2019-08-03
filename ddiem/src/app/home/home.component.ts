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
    this.service.listDiseases().subscribe(data => {
      this.diseaseList = data;
    })

  }

  onDiseaseSelect(disease){
    this.router.navigate(['/disease', encodeURIComponent(disease.OMIM_entry.value)]);
  }

}
