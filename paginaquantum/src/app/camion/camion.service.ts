import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Camion } from './camion';
import { CamionDetail } from './camion-detail';

const API_URL = 'http://192.168.132.86:5000';
const Camiones = '/camion/1';
const Camioness = '/salvo/';


@Injectable()
export class CamionService {


  constructor(private http: HttpClient) { }
  getCamiones(): Observable<Camion[]> {
        return this.http.get<Camion[]>(API_URL + Camiones);
    }



        getCamion(CamionId): Observable<Camion> {
        return this.http.get<Camion>(API_URL + Camioness +CamionId);
    }
}
