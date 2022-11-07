import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BusquedaGrafoComponent } from './busqueda-grafo.component';

describe('BusquedaGrafoComponent', () => {
  let component: BusquedaGrafoComponent;
  let fixture: ComponentFixture<BusquedaGrafoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BusquedaGrafoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BusquedaGrafoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
