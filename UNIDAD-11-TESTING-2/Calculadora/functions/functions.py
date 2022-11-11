import logging
# Imports para configurar docs_from_tests



def sumar(num1:float, num2:float) -> float:
    """funcion para sumar dos numeros

    Args:
        num1 (float): primer numero que se desea sumar
        num2 (float): segundo numero que se desea sumar

    Returns:
        float: el resultado de la suma de los numero
    """    
    return num1 + num2

def restar(num1:float, num2:float) -> float:
    """funcion para sumar dos numeros

    Args:
        num1 (float): primer numero que se desea restar
        num2 (float): segundo numero que se desea restar

    Returns:
        float: el resultado de la resta de los numero
    """  
    return num1 - num2

def multiplicar(num1:float, num2:float) -> float:
    """funcion para sumar dos numeros

    Args:
        num1 (float): primer numero que se desea multiplicar
        num2 (float): segundo numero que se desea multiplicar

    Returns:
        float: el resultado de la multiplicacion 
    """  
    return num1 * num2

def dividir(num1:float, num2:float) -> float:
    """funcion para sumar dos numeros

    Args:
        num1 (float): dividendo
        num2 (float): divisor

    Returns:
        float: el resulado de la divicion 
    """  
    try :
        resultado =  num1 / num2
    except ZeroDivisionError:
        resultado = 0 
        logging.error('No se puede dividir por cero')
        raise ZeroDivisionError 
    return resultado


