from datetime import datetime
from dateutil.relativedelta import relativedelta
class Empleados:
    """Clase que contiene datos de empleados y retorna mediante un string.
        :param nombre: nombre del empleado,
        :param apellido: apellido del empleado,
        :param fecha_nacimiento: fecha de nacimiento del empleado,
        :param nro_dni: numero de dni del empleado
        :type: args : string
    """
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:str, nro_dni:str ):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_dni = nro_dni
    def obtener_edad(self) -> str:
        """Obtiene la edad del empleado a partir de la fecha de nacimiento
            :return: edad del empleado
            :rtype: int
        """
        return relativedelta(datetime.now(), datetime.strptime(self.fecha_nacimiento, '%d/%m/%Y')).years
    def presentarse(self) -> str:
        """Presenta al empleado con sus datos
            :return: texto con infromacion del empleado
            :rtype: str
        """
        return f'Hola, soy {self.nombre} {self.apellido}. Nací el {self.fecha_nacimiento} y ni DNI es {self.nro_dni}'
    def __str__(self) -> str:
        return f'''
            Nombre : {self.nombre}
            Apellido : {self.apellido}
            Fecha de nacimiento : {self.fecha_nacimiento}
            Numero de dni : {self.nro_dni}
            '''
if __name__ == "__main__":
    empleado = Empleados("ricardo","lujan","20/11/1990","11111111")
    print(empleado.presentarse())
    print(empleado)
    print(empleado.obtener_edad())
