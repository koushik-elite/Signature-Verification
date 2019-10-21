import { Component, OnInit } from '@angular/core';
import { ApplicationService } from './services/application.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'signatureVerify';

  constructor(private appservice: ApplicationService) {
  }

  ngOnInit() {
    this.loadAllCustomerId()
  }

  loadAllCustomerId() {
    this.appservice.getAllCustomerId()
      .subscribe(
        data => {
          this.appservice.owner_ids.next(data.split(","));
        }
      );
  }
}
