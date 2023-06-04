import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { AboutUsComponent } from './components/about-us/about-us.component';
import { GraffitiSendingFormComponent } from './components/graffiti-sending-form/graffiti-sending-form.component';

const routes: Routes = [
    { path: 'map', component: LandingPageComponent},
    { path: 'about', component: AboutUsComponent},
    { path: 'send-graffiti', component: GraffitiSendingFormComponent},
    { path: '', redirectTo: '/map', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
