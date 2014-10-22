from unittest import TestCase
from empleado import *
from departamento import *
from mockito import *

__author__ = 'Laura'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        emp1 = mock(Empleado)  # emp1 con salario 1000
        emp2 = mock(Empleado)  # emp2 con salario 1500
        emp3 = mock(Empleado)  # emp3 con salario 2000

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
        emp1 = mock(Empleado)  # emp1 con salario 1000
        emp2 = mock(Empleado)  # emp2 con salario 1500
        emp3 = mock(Empleado)  # emp3 con salario 2000

        when(emp1).get_salario().thenReturn(12000)
        when(emp2).get_salario().thenReturn(24000)
        when(emp3).get_salario().thenReturn(36000)

        emp1.get_salario_mensual();

        dpto = Departamento("Empresa", 123)

        dpto.aniadir_empleado(emp1)
        dpto.aniadir_empleado(emp2)
        dpto.aniadir_empleado(emp3)

        total_mensual = dpto.get_salario_total_mensual()

        print("Test Salario Mensual total")
        print("Salario total mensual: ", total_mensual)

        self.assertEqual(total_mensual,6000)
