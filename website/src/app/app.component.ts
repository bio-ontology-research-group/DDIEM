import { Component, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  encapsulation: ViewEncapsulation.None,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ddiem';
  date = '';

  options = {
    headers:  new HttpHeaders({
      'Accept': 'application/json'
    })
  };

  constructor(private modalService: NgbModal,
    private http: HttpClient) {
      this.http.get('/api/ddiem/modified', this.options)
        .subscribe(data => {
          this.date = data && data[0] ? data[0].date.value : ''
        })
  }

  openInNewTab(url: string){
    window.open(url, "_blank");
  }

  openDisclaimer(content) { 
    this.modalService.open(content, {size: 'lg'}); 
  }
  
}
