import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { DiseaseComponent } from './disease/disease.component';
import { DiseaseListComponent } from './disease-list/disease-list.component';
import { FormsModule } from '@angular/forms';
import { DiseaseService } from './disease.service';
import { HttpClientModule } from '@angular/common/http';
import { EllipsisPipe } from '../pipes/EllipsisPipe';
import { SparqlComponent } from './sparql/sparql.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DiseaseListComponent,
    DiseaseComponent,
    SparqlComponent,
    EllipsisPipe
  ],
  imports: [
    NgbModule,
    FormsModule,
    HttpClientModule,
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    AppRoutingModule
  ],
  providers: [DiseaseService],
  bootstrap: [AppComponent]
})
export class AppModule { }
