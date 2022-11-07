import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GrafoRoutingModule } from './grafo/grafo-routing.module';
import { GrafoModule } from './grafo/grafo.module';
import { LoginUserComponent } from './login-user/login-user.component';
import { NotFoundComponent } from './template/not-found/not-found.component';
import {BusquedaGrafoComponent} from './informacion/busqueda-grafo/busqueda-grafo.component'
import { JuegoGrafoComponent } from './informacion/juego-grafo/juego-grafo.component';
import { SistemasInteligentesComponent } from './informacion/sistemas-inteligentes/sistemas-inteligentes.component';
import { AyudaComponent } from './template/ayuda/ayuda.component';
const routes: Routes = [
  {
    path: 'user',
    component: LoginUserComponent
  },
  {
    path: 'informacion-busqueda',
    component:BusquedaGrafoComponent
  },
  {
    path: 'informacion-juego',
    component:JuegoGrafoComponent
  },
  {
    path: 'informacion-inteligente',
    component:SistemasInteligentesComponent
  },
  {
    path: 'ayuda',
    component:AyudaComponent
  },
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/user',
  },
  {
    path:'**',
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    GrafoModule,
    GrafoRoutingModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
