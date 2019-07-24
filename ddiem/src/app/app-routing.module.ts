import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DiseaseListComponent } from './disease-list/disease-list.component';
import { DiseaseComponent } from './disease/disease.component';

const routes: Routes = [
  {path: 'home',component: HomeComponent},  
  {path: 'disease-list',component: DiseaseListComponent},
  {path: 'disease/:iri',component: DiseaseComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
