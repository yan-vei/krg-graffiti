import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent {
  apiLoaded: Observable<boolean>;

  constructor(httpClient: HttpClient) {

    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js?key=AIzaSyBKoxdP_26r9N69xoQmTd2ItzkmkS_ez7w', 'callback')
        .pipe(
          map(() => true),
          catchError(() => of(false)),
        );
  }
  lat: number = 49.808571116626005;
  lng: number = 73.10329162306904;

  options: google.maps.MapOptions = {
    center: {lat: this.lat, lng: this.lng},
    zoom: 12
  };
}
