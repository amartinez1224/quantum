import { Component, OnInit } from '@angular/core';
import { CamionDetail } from "../camion-detail";
import { CamionService } from "../camion.service";

@Component({
  selector: 'app-camion-malo',
  templateUrl: './camion-malo.component.html',
  styleUrls: ['./camion-malo.component.css']
})
export class CamionMaloComponent implements OnInit {

  constructor(private camionService: CamionService) { }

sosp: CamionDetail;

  ngOnInit() {
    this.camionService.getSosp().subscribe(sosp => this.sosp = sosp);
    }
  }

}
