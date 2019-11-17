import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CamionListComponent } from './camion-list.component';

describe('CamionListComponent', () => {
  let component: CamionListComponent;
  let fixture: ComponentFixture<CamionListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CamionListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CamionListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
