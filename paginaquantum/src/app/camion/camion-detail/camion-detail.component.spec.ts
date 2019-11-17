import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CamionDetailComponent } from './camion-detail.component';

describe('CamionDetailComponent', () => {
  let component: CamionDetailComponent;
  let fixture: ComponentFixture<CamionDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CamionDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CamionDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
