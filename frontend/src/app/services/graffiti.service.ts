import { HttpClient} from "@angular/common/http";
import { Injectable} from '@angular/core';
import { Observable } from 'rxjs';
import { Graffiti } from "../entities/graffiti.model";
import { environment } from 'src/environments/environment';
import { GraffitiForm } from "../entities/graffiti-form.model";


@Injectable({
  providedIn: 'root'
})
export class GraffitiService {
  constructor(private http: HttpClient) {}

  getGraffities(): Observable<Graffiti[]> {
    let url: string = environment.apiUrl + '/images';
    return this.http.get<Graffiti[]>(url);
  }

  sendGraffitiForm(graffitiForm: GraffitiForm, image: File): Observable<Graffiti> {
    let url: string = environment.apiUrl + '/images';

    const formData = new FormData();
    formData.append('image', image);
    formData.append('graffitiForm', JSON.stringify(graffitiForm));

    return this.http.post<Graffiti>(url, formData)
  }
}


