import csv
import sys

sys.setrecursionlimit(15000)  # Aumenta o limite de recursão para 1500


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None, data=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.data = data

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)


def insere(raiz, nodo):
    """Insere um nó em uma árvore binária de pesquisa."""
    # O nó deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # O nó deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # O nó deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)


def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nó corrente.
    print(raiz.chave),

    # Visita filho da direita.
    em_ordem(raiz.direita)


def busca(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor que a da raiz.
    return busca(raiz.esquerda, chave)