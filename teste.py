from meu_grafo_lista_adj_nao_dir import MeuGrafo


G_Paraiba = MeuGrafo()
G_Paraiba.adiciona_vertice("J")
G_Paraiba.adiciona_vertice("C")
G_Paraiba.adiciona_vertice("E")
G_Paraiba.adiciona_vertice("P")
G_Paraiba.adiciona_vertice("M")
G_Paraiba.adiciona_vertice("T")
G_Paraiba.adiciona_vertice("Z")
#arestas
G_Paraiba.adiciona_aresta("a1","J","C")
G_Paraiba.adiciona_aresta("a2","C","E")
G_Paraiba.adiciona_aresta("a3","C","E")
G_Paraiba.adiciona_aresta("a4","C","P")
G_Paraiba.adiciona_aresta("a5","C","P")
G_Paraiba.adiciona_aresta("a6","C","M")
G_Paraiba.adiciona_aresta("a7","C","T")
G_Paraiba.adiciona_aresta("a8","M","T")
G_Paraiba.adiciona_aresta("a9","T","Z")
print() 

print("Vertices não adjacentes:")
print(G_Paraiba.vertices_nao_adjacentes())

print("Verifica se tem laco:",G_Paraiba.ha_laco()) 

print("Grau do Vertice C: " , G_Paraiba.grau("C"))
print("Grau do Vertice T: " , G_Paraiba.grau("T"))
print("Grau do Vertice M: " , G_Paraiba.grau("M"))

print("Verifica se tem arestas paralelas:", G_Paraiba.ha_paralelas())

print(G_Paraiba.arestas_sobre_vertice("C"))

print("Grafo eh completo:", G_Paraiba.eh_completo())

print("ah_ciclo = ",G_Paraiba.ha_ciclo())

print("verificar se he arvore = ", G_Paraiba.eh_arvore())

print("Verificar se eh bi partido = ", G_Paraiba.eh_bipartido())





