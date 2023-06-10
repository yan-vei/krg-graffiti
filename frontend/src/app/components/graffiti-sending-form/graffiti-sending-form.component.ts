import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { GraffitiForm } from 'src/app/entities/graffiti-form.model';
import { coordinatesValidator, indexValidator } from 'src/app/utils/custom-validators';
import { GraffitiService } from 'src/app/services/graffiti.service';

@Component({
  selector: 'app-graffiti-sending-form',
  templateUrl: './graffiti-sending-form.component.html',
  styleUrls: ['./graffiti-sending-form.component.css']
})
export class GraffitiSendingFormComponent {
  private image: File | null = null;
  public sendGraffitiForm: FormGroup | any;

  ngOnInit(): void {
    this.sendGraffitiForm = this.fb.group({
      address: [''],
      longitude: [''],
      latitude: [''],
      zip: ['', Validators.minLength(5)],
      comment: ['',]
    })
  }

  constructor(private fb: FormBuilder, private graffitiService: GraffitiService) {
  }

  setFile(event: any) {
    const file = event.target.files[0];
    this.image = file;
  }


  get buttonDisabled() {
    return (!Boolean(this.image) && !this.sendGraffitiForm.valid);
  }

}
