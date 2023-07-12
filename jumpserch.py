import math
import csv
def jumpSearch(arr, x, n):

    # Encontrando o tamanho do bloco a ser pulado
    step = math.sqrt(n)

    # Encontrando o bloco onde o elemento está
    # presente (se estiver presente)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Fazendo uma busca linear por x em
    # bloco começando com prev.
    while arr[int(prev)] < x:
        prev += 1

        # Se chegarmos ao próximo bloco ou ao final
        # da matriz, o elemento não está presente.
        if prev == min(step, n):
            return -1

    # Se o elemento for encontrado
    if arr[int(prev)] == x:
        return prev

    return -1

# Este código é contribuído por "Sharad_Bhardwaj".