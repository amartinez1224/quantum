import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CamionListComponent } from './camion-list/camion-list.component';
import { CamionService } from './camion.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CamionDetailComponent } from './camion-detail/camion-detail.component';
import { RouterModule, Routes } from '@angular/router';

@NgModule({
  declarations: [CamionListComponent, CamionDetailComponent],
  imports: [
    CommonModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule
  ],
  exports: [CamionListComponent],
  providers:[CamionService]
})
export class CamionModule { }
