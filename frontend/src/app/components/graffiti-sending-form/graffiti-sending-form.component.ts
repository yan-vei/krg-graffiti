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
      address: ['', Validators.required],
      longitude: ['', [Validators.maxLength(14), coordinatesValidator()]],
      latitude: ['', [Validators.maxLength(14), coordinatesValidator()]],
      zip: ['', [Validators.minLength(6), Validators.maxLength(6), indexValidator()]],
      comment: ['', Validators.required]
    })
  }

  constructor(private fb: FormBuilder, private graffitiService: GraffitiService) {
  }

  setFile(event: any) {
    const file = event.target.files[0];
    this.image = file;
  }


  get formFilled() {
    return (Boolean(this.image) && this.sendGraffitiForm.valid);
  }

}
