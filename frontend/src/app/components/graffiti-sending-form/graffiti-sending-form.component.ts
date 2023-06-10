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
  private image: File | any;
  public sendGraffitiForm: FormGroup | any;

  ngOnInit(): void {
    this.sendGraffitiForm = this.fb.group({
      address: [null, Validators.required],
      longitude: ['', [Validators.maxLength(14), coordinatesValidator()]],
      latitude: ['', [Validators.maxLength(14), coordinatesValidator()]],
      zip: ['', [Validators.minLength(6), Validators.maxLength(6), indexValidator()]],
      comment: [null, Validators.required]
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

  onSubmit() {
    const graffitiForm: GraffitiForm = new GraffitiForm(this.sendGraffitiForm.controls.address.value,
      this.sendGraffitiForm.controls.zip.value, this.sendGraffitiForm.controls.latitude.value,
      this.sendGraffitiForm.controls.longitude.value, this.sendGraffitiForm.controls.comment.value);

    this.graffitiService.sendGraffitiForm(graffitiForm, this.image).subscribe(
      (data) => {
        this.sendGraffitiForm.reset();
      },
      (error) => {
        console.log(error);
      }
    )
  }

}
