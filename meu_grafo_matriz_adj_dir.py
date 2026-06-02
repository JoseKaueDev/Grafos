from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def alcancabilidade(self):   
        
        numero_vertices = len(self.vertices)
        matriz_retorno = [[0] * numero_vertices for _ in range(numero_vertices)]

        def dfs(origem , atual):
            matriz_retorno[origem][atual] = 1

            for vizinho in range(numero_vertices):
                if len(self.matriz[atual][vizinho]) > 0:
                    if matriz_retorno[origem][vizinho] == 0:
                        dfs(origem , vizinho)
        for i in range(numero_vertices):
            dfs(i , i)

        return matriz_retorno
