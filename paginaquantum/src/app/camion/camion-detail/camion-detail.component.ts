import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import {Camion} from '../camion';
import {CamionDetail} from '../camion-detail';
import { CamionService } from '../camion.service';


@Component({
  selector: 'app-camion-detail',
  templateUrl: './camion-detail.component.html',
  styleUrls: ['./camion-detail.component.css']
})
export class CamionDetailComponent implements OnInit {

  constructor(private camionService: CamionService, private route: ActivatedRoute) { }

  camionDetail: Camion;

  camion_id: number;

  loader: any;

  getCamionDetail(): void {
      this.camionService.getCamion(this.camion_id).subscribe(camionDetail => {this.camionDetail = camionDetail});
    }
/*
  ngOnInit() {
    this.camion_id = +this.route.snapshot.paramMap.get('id');
    this.camionDetail = new CamionDetail();
    this.getCamionDetail();
  }
*/

onLoad(params) {
  this.camion_id = parseInt(params['id']);
  this.camionDetail = new CamionDetail();
  this.getCamionDetail();
}
ngOnInit() {
  this.loader = this.route.params.subscribe((params: Params) => this.onLoad(params));
}

ngOnDestroy() {
  this.loader.unsubscribe();
}

}
