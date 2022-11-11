import os, sys
import unittest
sys.path.append('')
import functions.functions as f

# Imports para configurar docs_from_tests

from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'functions'), 'functions')

class MyTest(unittest.TestCase):
    def test_suma(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')


        self.assertEqual(f.sumar(1, 1), 2)

        self.assertNotEqual(f.sumar(1, 1), 1)

        with self.assertRaises(TypeError): 
            f.sumar(1,'a')



        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia suma.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)



    def test_resta(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')


        
        self.assertEqual(f.restar(20, 10), 10)

        self.assertNotEqual(f.restar(10, 10), -10)

        with self.assertRaises(TypeError):
            f.restar(1,'b')


        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia resta.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)



    def test_divicion(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')


        self.assertEqual(f.dividir(20, 10), 2)

        with self.assertRaises(ZeroDivisionError):
            f.dividir(1,0)

        with self.assertRaises(TypeError):
            f.dividir(1,'c')


        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia divicion.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)




    def test_multiplicacion(self):

        # Inicio de la secuencia
        initialise_call_hierarchy('start')


        self.assertEqual(f.multiplicar(20, 10), 200)

        self.assertNotEqual(f.multiplicar(1000, 10), 10)

        with self.assertRaises(TypeError):
            f.multiplicar(10,20,30)




        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()

        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia divicion.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)






if __name__ == '__main__':
    unittest.main()
