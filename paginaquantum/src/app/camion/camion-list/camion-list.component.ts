import { Component } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { Camion } from "../camion";
import { CamionService } from "../camion.service";
import { Location } from '@angular/common';
import {Router} from '@angular/router';

@Component({
  selector: "app-camion-list",
  templateUrl: "./camion-list.component.html",
  styleUrls: ["./camion-list.component.css"]
})
export class CamionListComponent {
  camionForm: FormGroup;

  constructor(
    private camionService: CamionService,
    private formBuilder: FormBuilder,
    private router: Router
  ) {
    this.camionForm = this.formBuilder.group({
      idSalvo: ["", [Validators.required, Validators.minLength(1)]],
    });
  }

  createCamion(newCamion: Camion) {
    console.warn("Your order has been submitted", newCamion);
    this.router.navigateByUrl('/salvo/'+newCamion.idSalvo);
   this.camionForm.reset();
  }
}
