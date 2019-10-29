import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DiseaseListComponent } from './disease-list/disease-list.component';
import { DiseaseComponent } from './disease/disease.component';
import { SparqlComponent } from './sparql/sparql.component';
import { AboutComponent } from './about/about.component';

const routes: Routes = [
  {path: '',component: HomeComponent},  
  {path: 'about',component: AboutComponent},  
  {path: 'disease-list',component: DiseaseListComponent},
  {path: 'disease-list-by-resource/:iri/:type',component: DiseaseListComponent},
  {path: 'disease/:iri',component: DiseaseComponent},
  {path: 'isparql',component: SparqlComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
