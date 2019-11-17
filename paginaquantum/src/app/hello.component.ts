import { Component, Input } from '@angular/core';

@Component({
  selector: 'hello',
  template: `<div class="container-fluid">
              <div class="row">
              <img src="../assets/logo.jpg" class="img-fluid" alt="Responsive image">
              </div>
              </div>`,
  styles: [`h1 { font-family: Lato; }`]
})
export class HelloComponent  {
  @Input() name: string;
}
