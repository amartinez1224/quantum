import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CamionMaloComponent } from './camion-malo.component';

describe('CamionMaloComponent', () => {
  let component: CamionMaloComponent;
  let fixture: ComponentFixture<CamionMaloComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CamionMaloComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CamionMaloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
