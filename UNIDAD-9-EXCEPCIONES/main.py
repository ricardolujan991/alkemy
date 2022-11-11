
def extrac_index(lista:list) -> str:
    """funcion para extraer un elemento de una lista ingresadno su indice

    Args:
        lista (list): lista de la cual se desea extraer la informacion

    Returns:
        str: se retorna la informacion que corresponde al indice ingresado
    """
    
    msj = 'ingrese el numero del indice que desea visualizar : '
    while True :
        try:
            index = int(input(msj))
            print(lista[index])
            break
        except:
            msj = 'El indice ingresado es incrrecto, por favor ingrese un indice valido : '
                          
if __name__ == '__main__':
    medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ]
    extrac_index(medios_transporte)
