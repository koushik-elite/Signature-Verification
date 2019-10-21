import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';

const URL = 'http://127.0.0.1:5000/';

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {
  

  public owner_ids = new BehaviorSubject(['']);

  constructor(private http: HttpClient) { }

  getAllCustomerId() {
    return this.http.get<String>(URL + "allcustomerid");
  }
}
