import { Component, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { MapInfoWindow, MapMarker } from '@angular/google-maps';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent {
  apiLoaded: Observable<boolean>;
  @ViewChild(MapInfoWindow, {static: false}) infoWindow: MapInfoWindow | any;

  lat: number = 49.808571116626005;
  lng: number = 73.10329162306904;

  markerOptions: google.maps.MarkerOptions = {draggable: false};
  markerPositions: google.maps.LatLngLiteral[] = [{lat: this.lat, lng: this.lng}];

  constructor(httpClient: HttpClient) {

    this.apiLoaded = httpClient.jsonp('https://maps.googleapis.com/maps/api/js?key=AIzaSyBKoxdP_26r9N69xoQmTd2ItzkmkS_ez7w', 'callback')
        .pipe(
          map(() => true),
          catchError(() => of(false)),
        );
  }

  options: google.maps.MapOptions = {
    center: {lat: this.lat, lng: this.lng},
    zoom: 12
  };

  openInfoWindow(marker: MapMarker) {
    this.infoWindow.open(marker);
  }
}
