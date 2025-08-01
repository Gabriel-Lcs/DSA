def binary_search(lista, item): 
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            ultimo = meio - 1
        elif chute < item:
            primeiro = meio + 1
        
    return None

lista = [0, 1, 2, 3, 5, 6, 8, 9]

print(binary_search(lista, 9))
print(binary_search(lista, 10))


