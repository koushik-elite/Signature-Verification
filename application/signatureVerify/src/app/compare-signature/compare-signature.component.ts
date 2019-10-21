import { Component, OnInit, AfterViewInit, ElementRef } from '@angular/core';
import { FileUploader } from 'ng2-file-upload';
import { ApplicationService } from '../services/application.service';
import { environment } from '../../environments/environment';

// const URL = 'http://127.0.0.1:5000/upload/compare/1';
// const URL = 'https://evening-anchorage-3159.herokuapp.com/api/';

@Component({
  selector: 'app-compare-signature',
  templateUrl: './compare-signature.component.html',
  styleUrls: ['./compare-signature.component.css']
})
export class CompareSignatureComponent implements OnInit {

  public uploader: FileUploader = new FileUploader({ url: environment.url + 'upload/compare/1' });
  public success = false;
  public fileadded = false;
  public response_data;
  public selected_id;
  public owner_ids = [];
  public result = { 0: "Genuine", 1: "Forged" }

  constructor(public appservice: ApplicationService) {
    // this.uploader.onAfterAddingFile = (file) => { file.withCredentials = false; };

    this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
      //things to do on completion
      console.log(response);
      this.response_data = JSON.parse(response)
      this.success = true;
      this.fileadded = false;
      this.uploader.queue = [];
    };
  }

  ngOnInit() {
    this.loadAllCustomerId();
    const that = this;
    // this.owner_ids = this.appservice.owner_ids.getValue();
    this.uploader.onBuildItemForm = function (fileItem, form) { form.append('id', that.selected_id); return { fileItem, form } };
  }

  ngAfterViewInit() {
    this.uploader.onAfterAddingFile = (item => {
      item.withCredentials = false;
      this.fileadded = true;
    });
  }

  onFileItemRemove(item) {
    item.remove();
    this.success = false;
    this.fileadded = false;
    // this.uploader.queue = [];
  }

  loadAllCustomerId() {
    this.appservice.getAllCustomerId()
      .subscribe(
        data => {
          this.appservice.owner_ids.next(data["customer_id"]);
        }
      );
  }

}
