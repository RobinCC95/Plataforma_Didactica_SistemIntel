import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JuegoGrafoComponent } from './juego-grafo.component';

describe('JuegoGrafoComponent', () => {
  let component: JuegoGrafoComponent;
  let fixture: ComponentFixture<JuegoGrafoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ JuegoGrafoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(JuegoGrafoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
