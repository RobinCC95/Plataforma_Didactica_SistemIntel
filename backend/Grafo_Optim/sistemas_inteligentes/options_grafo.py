from shutil import get_archive_formats
import time
from sistemas_inteligentes import graph_mapper

from sistemas_inteligentes.algoritmos import *
# from analisis import algorithms


class Options_Grafo:
    def __init__(self, tipo_problem, tipo_algoritmo, requerimientos) -> None:
        self.problem = Algoritmos_busqueda_solucion()
        self.tipo_problem = tipo_problem
        self.tipo_algoritmo = tipo_algoritmo
        self.requerimientos = requerimientos
        self.grafo_transform = None        
        self.options()
    
    def options(self):
        # self.problem.n_reinas_problem(8)
        # mg.ocho_puzzle_problem()
        # lista_sol = self.problem.coste_uniforme()
         #mat = graph_mapper.graph_to_adjacencies_mat(self.grafo)
         #TODO: quitar la linea siguiente y descomentar el else
        # self.grafo_transform = lista_sol

        self.tipoProblema(self.tipo_problem, self.requerimientos)
        self.grafo_transform = self.tipoSolucion(self.tipo_algoritmo)

    def tipoProblema(self, tipo_problema, requerimientos):
        if (tipo_problema == 'REINAS'):
            self.problem.n_reinas_problem(requerimientos.tamano_n)
        elif (tipo_problema == 'PUZZLE'):
            self.problem.ocho_puzzle_problem(requerimientos.lista)
        elif (tipo_problema == 'RUMANIA'):
            self.problem.romania_map_problem(requerimientos.ubicacion_inicial,
            requerimientos.ubicacion_final, self.problem.datos_defecto)
        else:
            raise Exception("No se reconoce el tipo de PROBLEMA")
            

    def tipoSolucion(self, tipo_solucion):
        grafo = None
        if(tipo_solucion == 'PRIMERO ANCHURA'):
            grafo = self.problem.primero_en_anchura()
        elif(tipo_solucion == 'PRIMERO PROFUNDIDAD'):
            grafo = self.problem.primero_en_profundidad_gra()
        elif(tipo_solucion == 'COSTE UNIFORME'):
            grafo = self.problem.coste_uniforme()
        elif(tipo_solucion == 'NUMERO PASOS'):
            grafo = self.problem.busqueda_num_pasos()
        elif(tipo_solucion == 'A ASTERISCO'):
            grafo = self.problem.a_asterisco_h()
        elif(tipo_solucion == 'RECURSIVA'):
            grafo = self.problem.recursiva_find()
        else:
            raise Exception("No se reconoce el tipo de SOLUCION")
        
        return grafo


    def get_grafo_transform(self):
        if self.grafo_transform is None:
            raise Exception("No se ha procesado el grafo")
        else:            
            return self.grafo_transform

    def set_grafo_transform(self):
        """Funcion encargada de las transformaciones y escoger las clases de busquedas
        """
        pass



