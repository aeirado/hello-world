'''Quick Sort Algorithm'''

from random import randint

def quick_sort_recursive(array):
    '''
    No quick quick_sort_recursive pega-se um número qualquer da lista e reserva para comparar com os outros -> assim cria-se uma variável temp com esse número. 
    Na fase de comparação divide-se a list
    - lesser_than = todos os números menores que temp
    - greater_than = todos os números maiores que temp
    Depois combina-se essas 2 listas com temp entre elas na lista original e supõe-se que tudo está ordenado.
    Repete-se recursivamente esse processo para as listas lesser_than e greater_than.
    Qual o caso base?
    Quando a lista dividida for igual ou menor que 1 não há mais o que ordenar, então, retorna-se ela.
    '''

    if len(array) <= 1:
        return array
    
    temp = array.pop(0)
    lesser_than = []
    greater_than = []
    for i in range(len(array)):
        if temp >= array[i]:
            lesser_than.append(array[i])
        else:
            greater_than.append(array[i])
    
    return quick_sort_recursive(lesser_than) +
    [temp] + quick_sort_recursive(greater_than)


if __name__ == '__main__':
    A = []
    for i in range(40):
        A.append(randint(-100, 100))
    
    print(A)
    result = quick_sort_recursive(A)
    print(result)
