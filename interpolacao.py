import math
import csv
# busca por interpolação
# com recursão

# Se x estiver presente em arr[0..n-1], então
# retorna o índice dele, senão retorna -1.
def interpolationSearch(arr, lo, hi, x):

    # Como a matriz está ordenada, um elemento presente
    # na matriz deve estar no intervalo definido pelo canto
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        # Sondando a posição mantendo
        # distribuição uniforme em mente.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))

        # Condição de alvo encontrado
        if arr[pos] == x:
            return pos

        # Se x for maior, x está na submatriz direita
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)

        # Se x for menor, x está na submatriz esquerda
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1