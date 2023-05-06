import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-graffiti-sending-form',
  templateUrl: './graffiti-sending-form.component.html',
  styleUrls: ['./graffiti-sending-form.component.css']
})
export class GraffitiSendingFormComponent {
  sendGraffitiForm = this.fb.group({
    address: [''],
    longitude: [''],
    latitude: [''],
    zip: [''],
    comment: [''],
    photo: ['']
  })

  constructor(private fb: FormBuilder) { }

}
