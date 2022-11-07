import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SistemasInteligentesComponent } from './sistemas-inteligentes.component';

describe('SistemasInteligentesComponent', () => {
  let component: SistemasInteligentesComponent;
  let fixture: ComponentFixture<SistemasInteligentesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SistemasInteligentesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SistemasInteligentesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
