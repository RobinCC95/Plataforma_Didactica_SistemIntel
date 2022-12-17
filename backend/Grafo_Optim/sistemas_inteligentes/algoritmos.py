from search import *
from notebook import psource, heatmap, gaussian_kernel, show_map, final_path_colors, display_visual, plot_NQueens
import warnings
warnings.filterwarnings("ignore")
import time

class Algoritmos_busqueda_solucion:

    def __init__(self):
        self.problema = None
        

    def romania_map_problem(self, pos_ini, pos_fin, grafo_mapa):
        psource(GraphProblem)
        self.graficar_grafo_map(grafo_mapa)
        self.problema = GraphProblem(pos_ini, pos_fin, grafo_mapa)

    def ocho_puzzle_problem(self,lista):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.problema =  EightPuzzle(lista)

    def n_reinas_problem(self, n):
        psource(NQueensProblem)
        self.problema = NQueensProblem(n)

    def primero_en_anchura(self):
        nodo_class_sol = breadth_first_tree_search(self.problema)
        return nodo_class_sol.solution()
        # print(nodo_class_sol.solution())
    # def primero_en_profundidad(self):
    #     """saca la primera solucion recorriendo en profundidad, cuidado mucha carga de 
    #     procesamiento

    #     Returns:
    #         _type_: _description_
    #     """
    #     nodo_class_sol = depth_first_tree_search(self.romania_problem)
    #     # print(nodo_class_sol.solution())
    #     return nodo_class_sol.solution()

    def primero_en_profundidad_gra(self):
        nodo_class_sol =  depth_first_graph_search(self.problema)
        return nodo_class_sol.solution()
        
    def coste_uniforme(self):
        nodo_class_sol =  uniform_cost_search(self.problema)
        return nodo_class_sol.solution()
    
    def busqueda_num_pasos(self,num_pasos=50):
        nodo_class_sol =  depth_limited_search(self.problema, num_pasos)
        return nodo_class_sol.solution()

    def a_asterisco_h(self):
        """Una búsqueda* es la mejor búsqueda en el primer gráfico con f(n) = g(n)+h(n).
     Debe especificar la función h cuando llame a astar_search, o
     más en su subclase Problema.

        Returns:
            lista nodos solucion
        """
        nodo_class_sol =  astar_search(self.problema)
        return nodo_class_sol.solution()

    # def distancia_linea_recta(self, pos_nodo):
    #     return (self.romania_problem.h(pos_nodo))
    def recursiva_find(self):
        nodo_class_sol =  recursive_best_first_search(self.problema)
        return nodo_class_sol.solution()

    def datos_defecto(self):
        romania_map = UndirectedGraph(dict(
            Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
            Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
            Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
            Drobeta=dict(Mehadia=75),
            Eforie=dict(Hirsova=86),
            Fagaras=dict(Sibiu=99),
            Hirsova=dict(Urziceni=98),
            Iasi=dict(Vaslui=92, Neamt=87),
            Lugoj=dict(Timisoara=111, Mehadia=70),
            Oradea=dict(Zerind=71, Sibiu=151),
            Pitesti=dict(Rimnicu=97),
            Rimnicu=dict(Sibiu=80),
            Urziceni=dict(Vaslui=142)))

        romania_map.locations = dict(
            Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
            Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
            Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
            Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
            Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
            Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
            Vaslui=(509, 444), Zerind=(108, 531))
        return romania_map

    def graficar_grafo_map(self, romania_map):
        # node colors, node positions and node label positions
        node_colors = {node: 'white' for node in romania_map.locations.keys()}
        node_positions = romania_map.locations
        node_label_pos = { k:[v[0],v[1]-10]  for k,v in romania_map.locations.items() }
        edge_weights = {(k, k2) : v2 for k, v in romania_map.graph_dict.items() for k2, v2 in v.items()}

        romania_graph_data = {  'graph_dict' : romania_map.graph_dict,
                                'node_colors': node_colors,
                                'node_positions': node_positions,
                                'node_label_positions': node_label_pos,
                                'edge_weights': edge_weights
                            }
        show_map(romania_graph_data)