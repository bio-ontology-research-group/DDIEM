import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { DiseaseService } from '../disease.service';

@Component({
  selector: 'app-disease',
  templateUrl: './disease.component.html',
  styleUrls: ['./disease.component.css']
})
export class DiseaseComponent implements OnInit {
  disease : any = {};


  constructor(private route: ActivatedRoute,
              private diseaseService: DiseaseService) {
    this.route.params.subscribe( params => {
      this.diseaseService.getDiseases(params.iri).subscribe(data => this.disease = data);
    });
  }

  ngOnInit() {
  }

}
