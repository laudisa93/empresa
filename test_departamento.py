from unittest import TestCase

from mockito import *

from empleado import *
from departamento import *


__author__ = 'Laura'


class TestDepartamento(TestCase):
    """Clase TestDepartamento para testear los metodos de la clase Departamento del proyecto"""

    def test_get_salario_total(self):
        """Metodo test get salario total

        Este metodo testea el correcto funcionamiento del metodo get_salario_total de la clase Departamento
        creando tres objetos empleados mediante mocks y verificando el valor del salario total

        :return: assertEqual
        :rtype: bool
        :raise assertEqual: si los valores de los salarios no coinciden
        """
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)

        when(emp1).get_salario().thenReturn(1000)
        when(emp2).get_salario().thenReturn(1500)
        when(emp3).get_salario().thenReturn(2000)

        dpto = Departamento("Empresa", 123)

        dpto.aniadir_empleado(emp1)
        dpto.aniadir_empleado(emp2)
        dpto.aniadir_empleado(emp3)

        total = dpto.get_salario_total()
        print("Test Salario total")
        print("Salario total: ", total)

        self.assertEqual(total, 4500)

    def test_get_salario_total_mensual(self):
        """Metodo test para testear el correcto funcionamiento del metodo get_salario_total_mensual

        Este metodo testea el correcto funcionamiento del metodo get_salario_total_mensual de la clase Departamento
        creando tres objetos empleados mediante mocks y verificando el valor del salario total mensual

        :return: assertEqual
        :rtype: bool
        :raise assertEqual: si los valores de los salarios no coinciden
        """

        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)

        when(emp1).get_salario().thenReturn(12000)
        when(emp2).get_salario().thenReturn(24000)
        when(emp3).get_salario().thenReturn(36000)

        emp1.get_salario_mensual()

        dpto = Departamento("Empresa", 123)

        dpto.aniadir_empleado(emp1)
        dpto.aniadir_empleado(emp2)
        dpto.aniadir_empleado(emp3)

        total_mensual = dpto.get_salario_total_mensual()

        print("Test Salario Mensual total")
        print("Salario total mensual: ", total_mensual)

        self.assertEqual(total_mensual, 6000)
