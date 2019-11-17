import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule, Routes} from '@angular/router';

import {CamionListComponent} from '../camion/camion-list/camion-list.component';
import {CamionDetailComponent} from '../camion/camion-detail/camion-detail.component';

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
