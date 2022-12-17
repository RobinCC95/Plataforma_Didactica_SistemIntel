import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { ProblemaEnum } from 'src/app/enums/problema.enum';
import { GrafoService } from 'src/app/grafo/grafo.service';
import { ParametrosEjercicioDTO } from 'src/app/modelos/parametros.ejercicio.dto';
import { Router } from '@angular/router';
import {
  FormArray,
  FormBuilder,
  FormControl,
  FormGroup,
  Validators
} from '@angular/forms'

@Component({
  selector: 'app-busqueda-grafo',
  templateUrl: './busqueda-grafo.component.html',
  styleUrls: ['./busqueda-grafo.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class BusquedaGrafoComponent implements OnInit {

  constructor(private grafoService : GrafoService, private fb: FormBuilder, private router: Router) { }

  ngOnInit(): void {
  }

  miFormulario: FormGroup = this.fb.group({
    solucion: this.fb.control('', [
      Validators.required,
      Validators.minLength(3),
      Validators.maxLength(15),
    ]),
    algoritmo: this.fb.control('', [
      Validators.required
    ]),
    datoUno: this.fb.control('', [
    ]),
    datoDos: this.fb.control('', [
    ]),
    tecnologias: this.fb.array([]),
  });

  tecnologia: FormControl = this.fb.control('', [
  ]);

  proyectos : any[] = []

  get tecnologias(): FormArray {
    return this.miFormulario.get('tecnologias') as FormArray;
  }

  validar() {
    return this.miFormulario.invalid && this.miFormulario.touched;
  }

  agregarTecnologia() {
    if (this.tecnologia.invalid) {
      return;
    }

    this.tecnologias.push(this.fb.control(this.tecnologia.value));
    this.tecnologia.reset();
  }

  agregarProyecto(){
    if (this.miFormulario.invalid) {
      return;
    }
    let param : ParametrosEjercicioDTO = new ParametrosEjercicioDTO()
    param.problema = this.miFormulario.get('solucion')!.value
    param.algoritmo = this.miFormulario.get('algoritmo')!.value
    param.requerimientos = {}
    switch(param.problema){
      case ProblemaEnum.PUZZLE:
        param.requerimientos['lista'] = this.tecnologias
        break;
      case ProblemaEnum.RUMANIA:
        param.requerimientos['ubicacion_inicial'] = this.miFormulario.get('datoUno')!.value
        param.requerimientos['ubicacion_final'] = this.miFormulario.get('datoDos')!.value
        break;
      case ProblemaEnum.REINAS:
        param.requerimientos['tamano_n'] = this.miFormulario.get('datoUno')!.value
        break;
    }
    this.grafoService.analizarGrafo(param).subscribe(data => {
      console.log(data);
    })
    this.miFormulario.reset()
    this.tecnologias.clear()
    this.router.navigate(['/grafo-analizar']);

  }

}
