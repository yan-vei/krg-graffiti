import { Component } from '@angular/core';

@Component({
  selector: 'app-about-us',
  templateUrl: './about-us.component.html',
  styleUrls: ['./about-us.component.css']
})
export class AboutUsComponent {

  public copyToClipboard(line: string) {
    navigator.clipboard.writeText(line);

    alert("Скопирован e-mail: " + line);
  }

}
