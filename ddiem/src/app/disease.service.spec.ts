import { TestBed } from '@angular/core/testing';

import { DiseaseService } from './disease.service';

describe('DiseaseService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DiseaseService = TestBed.get(DiseaseService);
    expect(service).toBeTruthy();
  });
});
