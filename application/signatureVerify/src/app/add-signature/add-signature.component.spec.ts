import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddSignatureComponent } from './add-signature.component';

describe('AddSignatureComponent', () => {
  let component: AddSignatureComponent;
  let fixture: ComponentFixture<AddSignatureComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddSignatureComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddSignatureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
