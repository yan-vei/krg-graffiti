import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { GraffitiForm } from 'src/app/entities/graffiti-form.model';
import { GraffitiService } from 'src/app/services/graffiti.service';

@Component({
  selector: 'app-graffiti-sending-form',
  templateUrl: './graffiti-sending-form.component.html',
  styleUrls: ['./graffiti-sending-form.component.css']
})
export class GraffitiSendingFormComponent {
  private image: File | null = null;

  sendGraffitiForm = this.fb.group({
    address: ['', Validators.maxLength(150)],
    longitude: ['', Validators.maxLength(12)],
    latitude: ['', Validators.maxLength(12)],
    zip: ['', [Validators.maxLength(6), Validators.minLength(6)]],
    comment: ['', Validators.required]
  })

  constructor(private fb: FormBuilder, private graffitiService: GraffitiService) {
  }

  setFile(event: any) {
    const file = event.target.files[0];
    this.image = file;
  }

  get graffitiImage() {
    return this.image;
  }

}
