import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { HeaderComponent } from './template/header/header.component';
import { FooterComponent } from './template/footer/footer.component';
import { NotFoundComponent } from './template/not-found/not-found.component';
import { HttpClientModule } from '@angular/common/http';
import { UsuarioService } from './usuario.service';
import { BusquedaGrafoComponent } from './informacion/busqueda-grafo/busqueda-grafo.component';
import { JuegoGrafoComponent } from './informacion/juego-grafo/juego-grafo.component';
import { SistemasInteligentesComponent } from './informacion/sistemas-inteligentes/sistemas-inteligentes.component';
import { AyudaComponent } from './template/ayuda/ayuda.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginUserComponent,
    HeaderComponent,
    FooterComponent,
    NotFoundComponent,
    BusquedaGrafoComponent,
    JuegoGrafoComponent,
    SistemasInteligentesComponent,
    AyudaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  exports:[
    BusquedaGrafoComponent,
    JuegoGrafoComponent,
    SistemasInteligentesComponent,
    AyudaComponent
  ],
  providers: [UsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
