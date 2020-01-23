# Pra segunda questão decidi utilizar o algoritmo de Khan
class Vertex:
    def __init__(self, n):
        self.n = n
        self.vertices = []
        self.grau_de_entrada = 0


class Grafo:
    def __init__(self):
        self.grafo = {}
        self.tamanho = 0


    def add_aresta(self, u, v):
        self.grafo[u].vertices.append(v)


    def add_vertice(self, vertice):
        vertice = Vertex(vertice)
        self.grafo[vertice.n] = vertice
        self.tamanho += 1

    def topological_sort(self) -> list:
        # Primeiro verifico o grau de entrada de cada vértice
        for i in self.grafo:
            for j in self.grafo[i].vertices:
                self.grafo[j].grau_de_entrada += 1


        fila = []

        # Dentro da fila eu coloco primeiro os vértices que possuem grau de entrada igual a zero
        for i in range(self.tamanho):
            if self.grafo[i].grau_de_entrada == 0:
                fila.append(i)

        resultado = []

        # Após isso eu vou montando a a lista resultado com os vértices que estão na fila e possuem grau de entrada
        # igual a zero
        while fila:
            u = fila.pop(0)
            resultado.append(u)


            for i in self.grafo[u].vertices:
                self.grafo[i].grau_de_entrada -= 1

                if self.grafo[i].grau_de_entrada == 0:
                    fila.append(i)


        # Apenas formatação da saída
        for i in resultado:
            if i == resultado[-1]:
                print(i)
                break
            print(i, end=', ')

        return resultado


if __name__ == '__main__':
    g = Grafo()
    g.add_vertice(0)
    g.add_vertice(1)
    g.add_vertice(2)
    g.add_vertice(3)
    g.add_vertice(4)
    g.add_vertice(5)
    g.add_vertice(6)
    g.add_vertice(7)
    
    g.add_aresta(0, 3)
    g.add_aresta(1, 2)
    g.add_aresta(4, 6)
    g.add_aresta(3, 5)
    g.add_aresta(2, 6)
    g.add_aresta(4, 6)
    g.add_aresta(5, 7)
    g.add_aresta(5, 6)
    g.add_aresta(6, 7)

    print("A ordem de carregamento de todos os módulos do sistema é")
    g.topological_sort()
