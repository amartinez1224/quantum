import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule, Routes} from '@angular/router';

import {CamionListComponent} from '../camion/camion-list/camion-list.component';
import {CamionDetailComponent} from '../camion/camion-detail/camion-detail.component';
import { HelloComponent } from '../hello.component';
import {CamionMaloComponent} from '../camion/camion-malo/camion-malo.component';

const routes: Routes = [
  {
     path: 'camiones',
     component: CamionListComponent
   },
   {
     path: 'salvo',
     children: [
       {
         path: ':id',
         component: CamionDetailComponent
       }
     ]
  },
  {
      path: 'home',
      component: HelloComponent
  },
  {
      path: 'sospechoso',
      component: CamionMaloComponent
  }
 ];

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'})
    ],
    exports: [RouterModule],
    declarations: []
})
export class AppRoutingModule {

}
