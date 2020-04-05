import { Component, ViewEncapsulation, ViewChild } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  encapsulation: ViewEncapsulation.None,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ddiem';
  date = '';
  disclaimerKey = "disclaimer"

  @ViewChild('content') disclaimerTemp; 

  options = {
    headers:  new HttpHeaders({
      'Accept': 'application/json'
    })
  };

  constructor(private modalService: NgbModal,
    private http: HttpClient,
    private cookieSrv: CookieService) {
      this.http.get('/api/ddiem/modified', this.options)
        .subscribe(data => {
          this.date = data && data[0] ? data[0].date.value : ''
        })
  }

  ngOnInit() {
    if (!this.cookieSrv.get(this.disclaimerKey) || this.cookieSrv.get(this.disclaimerKey) == 'false') {
      this.cookieSrv.set(this.disclaimerKey, 'false')
      this.modalService.open(this.disclaimerTemp, {size: 'lg'}).result.then((result) => {
        this.cookieSrv.set(this.disclaimerKey, 'true')
      }, (reason) => {
        this.cookieSrv.set(this.disclaimerKey, 'true')
      });
    } 
  }

  openInNewTab(url: string){
    window.open(url, "_blank");
  }

  openDisclaimer(content) { 
    this.modalService.open(content, {size: 'lg'}); 
  }
  
}
