import { Component, OnInit } from '@angular/core';
import { DiseaseService } from '../disease.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  stats: any = [];

  constructor(private service: DiseaseService) { }

  ngOnInit() {
    this.service.getDiseaseStats().subscribe(data => {
      this.stats = data;
    })
  }

  openInNewTab(url: string){
    window.open(url, "_blank");
  }
}
