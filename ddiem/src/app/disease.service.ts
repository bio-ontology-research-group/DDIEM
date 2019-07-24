import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';

@Injectable()
export class DiseaseService {

  constructor(private http: HttpClient) { }

  listDiseases() {
    let options = {
      headers:  new HttpHeaders({
        'Accept': 'application/json'
      })
    };

    return this.http.get('/api/disease', options);
  }

  getDiseases(iri: any) {
    let options = {
      headers:  new HttpHeaders({
        'Accept': 'application/json'
      })
    };

    return this.http.get('/api/disease/' + iri, options);
  }
}
