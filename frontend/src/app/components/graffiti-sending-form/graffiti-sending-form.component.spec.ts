import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GraffitiSendingFormComponent } from './graffiti-sending-form.component';

describe('GraffitiSendingFormComponent', () => {
  let component: GraffitiSendingFormComponent;
  let fixture: ComponentFixture<GraffitiSendingFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GraffitiSendingFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GraffitiSendingFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
