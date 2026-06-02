from meu_grafo_lista_adj_nao_dir import MeuGrafo

print("INICIANDO OS CASOS DE TESTES")

# ==========================================
# CASO DE TESTE 1: Árvore Direcionada
# ==========================================
g1 = MeuGrafo()
g1.adiciona_vertice("A")
g1.adiciona_vertice("B")
g1.adiciona_vertice("C")
g1.adiciona_vertice("D")
g1.adiciona_vertice("E")

g1.adiciona_aresta("a1", "A", "B")
g1.adiciona_aresta("a2", "A", "C")
g1.adiciona_aresta("a3", "B", "D")
g1.adiciona_aresta("a4", "B", "E")

print("--- CASO 1: Árvore Direcionada ---")
print("\nPossui ciclo? (Esperado: False) = ", g1.ha_ciclo())
print("É árvore? (Esperado: ['C', 'D', 'E']) = ", g1.eh_arvore())
print("É bipartido? (Esperado: True) = ", g1.eh_bipartido())
print("Menor Caminho A até E (Esperado: ['A', 'B', 'E']) = ", g1.menor_caminho("A", "E"))
print()

# ==========================================
# CASO DE TESTE 2: Quadrado Direcionado
# ==========================================
g2 = MeuGrafo()
g2.adiciona_vertice("A")
g2.adiciona_vertice("B")
g2.adiciona_vertice("C")
g2.adiciona_vertice("D")

g2.adiciona_aresta("e1", "A", "B")
g2.adiciona_aresta("e2", "B", "D")
g2.adiciona_aresta("e3", "A", "C")
g2.adiciona_aresta("e4", "C", "D")

print("--- CASO 2: Quadrado Direcionado ---")
print("\nPossui ciclo? (Esperado: False) = ", g2.ha_ciclo())
print("É árvore? (Esperado: False) = ", g2.eh_arvore())
print("É bipartido? (Esperado: True) = ", g2.eh_bipartido())
print("Menor Caminho A até D (Esperado: ['A', 'B', 'D'] ou ['A', 'C', 'D']) = ", g2.menor_caminho("A", "D"))
print()


# ==========================================
# CASO DE TESTE 3: Triângulo com Vértice Isolado
# ==========================================
g3 = MeuGrafo()
g3.adiciona_vertice("A")
g3.adiciona_vertice("B")
g3.adiciona_vertice("C")
g3.adiciona_vertice("F")

g3.adiciona_aresta("t1", "A", "B")
g3.adiciona_aresta("t2", "B", "C")
g3.adiciona_aresta("t3", "C", "A")

print("--- CASO 3: Triângulo com Vértice Isolado ---")
print("\nPossui ciclo? (Esperado: True) = ", g3.ha_ciclo())
print("É árvore? (Esperado: False) = ", g3.eh_arvore())
print("É bipartido? (Esperado: False) = ", g3.eh_bipartido())
print("Menor Caminho A até F (Esperado: None) = ", g3.menor_caminho("A", "F"))