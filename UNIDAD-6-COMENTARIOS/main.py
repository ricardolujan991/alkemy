def contar_caracteres(palabras):
    #se cuenta la cantidad de caracteres de cada palabra en la lista
    total_caracteres = []
    for palabra in palabras:
        total_caracteres.append(len(palabra))
    return total_caracteres

if __name__ == '__main__':
    lista_inicial = ['perro', 'elefante', 'dragón']
    print(contar_caracteres(lista_inicial))