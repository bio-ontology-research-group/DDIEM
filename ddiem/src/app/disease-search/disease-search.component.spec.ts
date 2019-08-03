import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DiseaseSearchComponent } from './disease-search.component';

describe('DieaseSearchComponent', () => {
  let component: DiseaseSearchComponent;
  let fixture: ComponentFixture<DiseaseSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DiseaseSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DiseaseSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
