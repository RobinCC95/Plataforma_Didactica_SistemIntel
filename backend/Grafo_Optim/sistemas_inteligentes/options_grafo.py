from shutil import get_archive_formats
import time
from sistemas_inteligentes import graph_mapper

from analisis import algorithms


class Options_Grafo:
    def __init__(self, grafo, option) -> None:
        self.grafo = grafo
        self.option = option
        self.grafo_transform = None        
        self.options()
    
    def options(self):
        option = self.option
         #mat = graph_mapper.graph_to_adjacencies_mat(self.grafo)
         #TODO: quitar la linea siguiente y descomentar el else
        self.grafo_transform = "grafo transformado"
        if option == "find_profundidad":
            pass
        elif option == "find_anchura":
            pass
        elif option == "a-estrella":
            pass
        elif option == "poda-a-b":
            pass
        else:
            pass
            #raise Exception("opcion no reconocida")

    def get_grafo_transform(self):
        if self.grafo_transform is None:
            raise Exception("No se ha procesado el grafo")
        else:            
            return self.grafo_transform

    def set_grafo_transform(self):
        """Funcion encargada de las transformaciones y escoger las clases de busquedas
        """
        pass



