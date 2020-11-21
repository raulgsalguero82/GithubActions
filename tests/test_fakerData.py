import unittest
import datetime
from Comunidad.Persona import Persona
from Comunidad.Base import Base, Session
from faker import Faker


class Test_fakerData(unittest.TestCase):
    


    def setUp(self):
        self.data_factory = Faker()
        self.data = [] 
        self.personas = []
        for i in range(0,10):
            self.data.append((self.data_factory.name(), self.data_factory.random_number()))
            self.personas.append(Persona(nombre = self.data[-1][0], edad = self.data[-1][-1]))

    def test_constructor(self):
        for persona, dat in zip(self.personas, self.data):
            self.assertEqual(persona.dar_nombre(), dat[0])
            self.assertEqual(persona.dar_edad(), dat[-1])

    def test_anio_nacimiento(self):
       for persona, dat in zip(self.personas, self.data):
                self.assertEqual(persona.calcular_anio_nacimiento(True), datetime.datetime.now().year - dat[-1])

    def test_asignacion(self):
        original_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba = Persona(nombre = original_data[0], edad = original_data[-1])
        new_data = (self.data_factory.name(), self.data_factory.random_number())
        while new_data[0] == original_data[0] or new_data[-1] == original_data[-1]:
            new_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba.asignar_nombre(new_data[0])
        persona_prueba.asignar_edad(new_data[-1])    
        self.assertFalse(persona_prueba.dar_nombre()==original_data[0])
        self.assertFalse(persona_prueba.dar_edad()==original_data[-1])
        self.assertTrue(persona_prueba.dar_nombre()==new_data[0])
        self.assertTrue(persona_prueba.dar_edad()==new_data[-1])

    def test_objetos_iguales(self):
        persona_nueva = self.personas[-1]
        self.assertIsNot(persona_nueva, self.personas[0])
        self.assertIs(persona_nueva, self.personas[-1])

    def test_elemento_en_conjunto(self):
        original_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba = Persona(nombre = original_data[0], edad = original_data[-1])
        self.assertIn(self.personas[0], self.personas)
        self.assertNotIn(persona_prueba, self.personas)

    def test_instancia_clase(self):
        self.assertIsInstance(self.personas[0], Persona)
        self.assertNotIsInstance(self.personas, Persona)

    def test_almacenar(self):
        self.personas[0].almacenar()

        session = Session()
        persona = session.query(Persona).filter(Persona.nombre == self.data[0][0] and Persona.edad == self.data[0][1]).first()

        self.assertEqual(persona.dar_nombre(),self.data[0][0])
        self.assertEqual(persona.dar_edad(),self.data[0][-1])

    def test_recuperar(self):
        session = Session()
        session.add(self.personas[0])
        session.commit()
        session.close()

        persona = Persona("",0)
        persona.recuperar(self.data[0][0], self.data[0][-1])

        self.assertEqual(persona.dar_nombre(),self.data[0][0])
        self.assertEqual(persona.dar_edad(),self.data[0][-1])



if __name__ == '__main__':
    unittest.main()
