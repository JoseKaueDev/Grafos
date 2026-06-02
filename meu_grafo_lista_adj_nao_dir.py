from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

#lista adijacencia nao direcionado


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not V in [v.rotulo for v in self.vertices]:
            print("Erro, Vertice nao existe")
            raise VerticeInvalidoError()
        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                if self.arestas[a].v1.rotulo == V and self.arestas[a].v2.rotulo == V:
                    grau +=2
                else:
                    grau +=1
        return grau




    #teste para verificar se existe um ciclo

    def ha_ciclo(self):
        visitado = set()

        def dfs(v, vertice_pai):

            visitado.add(v.rotulo)

            for aresta in self.arestas.values():
                if aresta.v1 == v:
                    vizinho = aresta.v2
                elif aresta.v2 == v:
                    vizinho = aresta.v1
                else:
                    continue

                if vizinho.rotulo not in visitado:
                    if dfs(vizinho, v):
                        return True
                elif vizinho != vertice_pai:
                    return True

            return False
        
        for vertices in self.vertices:
            if vertices.rotulo not in visitado:
                if dfs(vertices, None):
                    return True
        return False
    
    #verificar se eh uma arvore 

    def eh_arvore(self):

        if self.ha_ciclo():
            return False
        if len(self.arestas) != (len(self.vertices) -1):
            return False
        
        folhas = []

        for v in self.vertices:
            if len(self.vertices) == 1:
                folhas.append(v.rotulo)
            elif self.grau(v.rotulo) == 1:
                folhas.append(v.rotulo)

        return folhas

    #verificar se é bipartido 

    def eh_bipartido(self):
        cores = {}   

        def dfs_colocar_cor(v , cor_atual):

            cores[v.rotulo] = cor_atual
            
            cor_oposto = 1 - cor_atual

            for aresta in self.arestas.values():
                if aresta.v1 == v:
                    vizinho = aresta.v2
                elif aresta.v2 == v:
                    vizinho = aresta.v1
                else:
                    continue

                if vizinho.rotulo not in cores:
                    if not dfs_colocar_cor(vizinho , cor_oposto):
                        return False
                elif cores[vizinho.rotulo] == cor_atual:
                    return False

            return True    

        for vertice in self.vertices:    #primeiro percorrer todos os vertices
            if vertice.rotulo not in cores:    #se o 
                if not dfs_colocar_cor(vertice, 0):
                    return False
                
        return True 
    


    def menor_caminho(self, vi, vf):

        for aresta in self.arestas.values():
            if aresta.peso < 0:
                return "Não é possível calcular: existem pesos negativos."

        dist = {}
        anterior = {}
        visitados = set()

        for v in self.vertices:
            dist[v.rotulo] = float('inf')
            anterior[v.rotulo] = None

        dist[vi] = 0

        while len(visitados) < len(self.vertices):

            atual = None
            menor_dist = float('inf')

            for vertice in self.vertices:
                r = vertice.rotulo

                if r not in visitados and dist[r] < menor_dist:
                    menor_dist = dist[r]
                    atual = r

            if atual is None:
                break

            visitados.add(atual)

            for aresta in self.arestas.values():

                if aresta.v1.rotulo == atual:

                    vizinho = aresta.v2.rotulo
                    nova_dist = dist[atual] + aresta.peso

                    if nova_dist < dist[vizinho]:
                        dist[vizinho] = nova_dist
                        anterior[vizinho] = atual

        if dist[vf] == float('inf'):
            return None

        caminho = []
        atual = vf

        while atual is not None:
            caminho.append(atual)
            atual = anterior[atual]

        caminho.reverse()

        return caminho, dist[vf]
    


    



                     





                


