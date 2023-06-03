import { Component, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { MapInfoWindow, MapMarker } from '@angular/google-maps';
import { GraffitiService } from 'src/app/services/graffiti.service';
import { environment } from 'src/environments/environment';
import { Graffiti } from 'src/app/entities/graffiti.model';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent {
  apiLoaded: Observable<boolean>;
  graffities: Graffiti[] = [];
  url: string = 'https://maps.googleapis.com/maps/api/js?key=' + environment.googleMapsApiKey;

  @ViewChild(MapInfoWindow, {static: false}) infoWindow: MapInfoWindow | any;

  lat: number = 49.808571116626005;
  lng: number = 73.10329162306904;

  markerOptions: google.maps.MarkerOptions = {draggable: false};
  markerPositions: google.maps.LatLngLiteral[] = [{lat: this.lat, lng: this.lng}];

  constructor(private httpClient: HttpClient, private graffitiService: GraffitiService) {
    this.apiLoaded = httpClient.jsonp(this.url, 'callback')
        .pipe(
          map(() => true),
          catchError(() => of(false)),
        );
  }

  ngOnInit() {
    this.graffitiService.getGraffities()
    .subscribe((data: Graffiti[]) =>{
      this.graffities = data;
    })
  }

  options: google.maps.MapOptions = {
    center: {lat: this.lat, lng: this.lng},
    zoom: 12
  };

  openInfoWindow(marker: MapMarker) {
    this.infoWindow.open(marker);
  }
}
