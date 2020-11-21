import unittest
import datetime
from Comunidad.Persona import Persona
from Comunidad.Base import Base, Session


class Test_persona(unittest.TestCase):

    def test_prueba(self):
        self.assertEqual(1, 1)

    def setUp(self):
       self.persona1 = Persona(nombre='Alejandra', edad=25)
       self.persona2 = Persona(nombre='Diego', edad=22)
       self.persona3 = Persona(nombre='Alejandra', edad=25)
       self.persona4 = Persona(nombre='Diana', edad=25)
       self.grupo = [self.persona1, self.persona2, self.persona3]

    def test_constructor(self):
       self.assertEqual(self.persona1.dar_nombre(), 'Alejandra')
       self.assertEqual(self.persona1.dar_edad(), 25)

    def test_anio_nacimiento(self):
       self.assertEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25)
       self.assertNotEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25)
       self.assertEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25 + 1)
       self.assertNotEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25 + 1)

    def test_asignacion(self):
      self.persona2.asignar_edad(28)
      self.persona2.asignar_nombre("Felipe")
      self.assertFalse(self.persona2.dar_nombre()=='Diego')
      self.assertFalse(self.persona2.dar_edad()==22)
      self.assertTrue(self.persona2.dar_nombre()=='Felipe')
      self.assertTrue(self.persona2.dar_edad()==28)

    def test_objetos_iguales(self):
       persona_nueva = self.persona1
       self.assertIsNot(self.persona1, self.persona3)
       self.assertIs(self.persona1, persona_nueva)

    def test_alamacenar(self):
       self.persona1.almacenar()

       session = Session()
       persona = session.query(Persona).filter(Persona.nombre == 'Alejandra' and Persona.edad == 25).first()

       self.assertEqual(persona.dar_nombre(),'Alejandra')
       self.assertEqual(persona.dar_edad(),25)

    def test_recuperar(self):
       session = Session()
       session.add(self.persona2)
       session.commit()
       session.close()

       persona = Persona("",0)
       persona.recuperar("Diego", 22)

       self.assertEqual(persona.dar_nombre(),'Diego')
       self.assertEqual(persona.dar_edad(),22)


    def test_todos(self):
       session = Session()       
       session = Session()
       personas = session.query(Persona).all()
       session.close()       
       self.assertIsNotNone(personas)


if __name__ == '__main__':
    unittest.main()

