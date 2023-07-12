import csv

def binarySearch(A, left, right, x):
    """Algoritmo de busca binária para retornar a posição da chave `x` na sublista A[left…right]"""
    # Condição base (o espaço de busca está esgotado)
    if left > right:
        return -1

    # encontra o valor médio no espaço de busca e compara com a chave
    mid = (left + right) // 2

    # Condição base (uma chave é encontrada)
    if x == A[mid]:
        return mid

    # descarta todos os elementos no espaço de busca correto, incluindo o elemento do meio
    elif x < A[mid]:
        return binarySearch(A, left, mid - 1, x)

    # descarta todos os elementos no espaço de busca à esquerda, incluindo o elemento do meio
    else:
        return binarySearch(A, mid + 1, right, x)


def exponentialSearch(A, x):
    """Retorna a posição da chave `x` em uma determinada lista `A` de comprimento `n`"""
    # caso básico
    if not A:
        return -1

    bound = 1

    # encontra o intervalo no qual a chave `x` residiria
    while bound < len(A) and A[bound] < x:
        bound *= 2  # calcula a próxima potência de 2

    # chama busca binária em A[bound/2 … min(bound, n-1)]
    return binarySearch(A, bound // 2, min(bound, len(A) - 1), x)