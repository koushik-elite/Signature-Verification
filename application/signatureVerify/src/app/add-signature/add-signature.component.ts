import { Component, OnInit, AfterViewInit, ElementRef } from '@angular/core';
import { FileUploader } from 'ng2-file-upload';
import { ApplicationService } from '../services/application.service';
import { environment } from '../../environments/environment';

// const URL = 'http://127.0.0.1:5000/upload/original';
// const URL = 'https://evening-anchorage-3159.herokuapp.com/api/';

@Component({
  selector: 'app-add-signature',
  templateUrl: './add-signature.component.html',
  styleUrls: ['./add-signature.component.css']
})
export class AddSignatureComponent implements OnInit, AfterViewInit {

  public uploader: FileUploader = new FileUploader({ url: environment.url + 'upload/original' });
  public success = false;
  public fileadded = false;
  public customer_id = 0

  constructor(appservice: ApplicationService) {
    // this.uploader.onAfterAddingFile = (file) => { file.withCredentials = false; };

    this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
      //things to do on completion
      this.customer_id = response
      // let owner_ids = appservice.owner_ids.getValue()
      // owner_ids.push(response)
      // appservice.owner_ids.next(owner_ids);
      this.success = true;
      this.fileadded = false;
      this.uploader.queue = [];
      console.log(response)
    };
  }

  ngOnInit() {
  }

  showThumb(image, el: ElementRef) {
    let reader = new FileReader();
    reader.onloadend = function (e) {
      el.nativeElement.src = reader.result;
    };
    if (image) {
      return reader.readAsDataURL(image);
    }
  }

  onFileItemRemove(item) {
    item.remove();
    this.success = false;
    this.fileadded = false;
    // this.uploader.queue = [];
  }

  ngAfterViewInit() {
    this.uploader.onAfterAddingFile = (item => {
      item.withCredentials = false;
      this.fileadded = true;
    });
  }

}
