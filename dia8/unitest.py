import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self): #necesario que empiece por test
        palabra = "buen día"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DÍA") #Compara el resultado de la función con el esperado

if __name__ == '__main__':
    unittest.main()
    