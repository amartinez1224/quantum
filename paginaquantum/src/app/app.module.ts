import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {ReactiveFormsModule, FormsModule} from '@angular/forms';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

import {AppRoutingModule} from './app-routing/app-routing.module';
import {CamionModule} from './camion/camion.module';

import { AppComponent } from './app.component';
import { HelloComponent } from './hello.component';
import { HomeComponent } from './app/home/home.component';

@NgModule({
  imports:      [ BrowserModule, FormsModule,RouterModule,AppRoutingModule,CamionModule,HttpClientModule ],
  declarations: [ AppComponent, HelloComponent, HomeComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
