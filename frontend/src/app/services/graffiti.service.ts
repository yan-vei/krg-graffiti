import { HttpClient} from "@angular/common/http";
import { Injectable} from '@angular/core';
import { Observable } from 'rxjs';
import { Graffiti } from "../entities/graffiti.model";
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class GraffitiService {
  constructor(private http: HttpClient) {}

  getGraffities() : Observable<Graffiti[]> {
    let url: string = environment.apiUrl + '/images';
    return this.http.get<Graffiti[]>(url);
  }
}


