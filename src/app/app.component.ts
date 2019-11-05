import { Component, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  encapsulation: ViewEncapsulation.None,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ddiem';

  constructor(private modalService: NgbModal) {}

  openInNewTab(url: string){
    window.open(url, "_blank");
  }

  openDisclaimer(content) { 
    this.modalService.open(content, {size: 'lg'}); 
  }
}
