from meu_grafo_matriz_adj_dir import MeuGrafo

grafo_1 = MeuGrafo()

N = {"A", "B", "C"}

for n in sorted(N):
    grafo_1.adiciona_vertice(n)

grafo_1.adiciona_aresta("a1", "A", "B")
grafo_1.adiciona_aresta("a2", "B", "C")

print("Teste grafo_1 matriz de alcançabilidade: ")
for linha in grafo_1.alcancabilidade():
    print(linha)

# Esperado:
# [1, 1, 1]
# [0, 1, 1]
# [0, 0, 1]

#Teste 2 - Ciclo A → B → C → A

grafo_2 = MeuGrafo()

N = {"A", "B", "C"}

for n in sorted(N):
    grafo_2.adiciona_vertice(n)

grafo_2.adiciona_aresta("a1", "A", "B")
grafo_2.adiciona_aresta("a2", "B", "C")
grafo_2.adiciona_aresta("a3", "C", "A")

print("Teste grafo_2 matriz de alcançabilidade: ")
for linha in grafo_2.alcancabilidade():
    print(linha)

# Esperado:
# [1, 1, 1]
# [1, 1, 1]
# [1, 1, 1]

#Teste 3 - Grafo desconexo

grafo3 = MeuGrafo()

N = {"A", "B", "C", "D"}

for n in sorted(N):
    grafo3.adiciona_vertice(n)

grafo3.adiciona_aresta("a1", "A", "B")
grafo3.adiciona_aresta("a2", "C", "D")

print("Teste grafo_3 matriz de alcançabilidade: ")
for linha in grafo3.alcancabilidade():
    print(linha)

# Esperado:
# [1, 1, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 1]
# [0, 0, 0, 1]

#Teste 4 - Um vértice isolado

grafo4 = MeuGrafo()

N = {"A"}

for n in sorted(N):
    grafo4.adiciona_vertice(n)

print("Teste grafo_4 matriz de alcançabilidade: ")
for linha in grafo4.alcancabilidade():
    print(linha)

# Esperado:
# [1]
