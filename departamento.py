__author__ = 'Laura'


class Departamento():

    def __init__(self, nombre_depto, id_depto):
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def get_salario_total(self):
        total = 0
        for empleado in self.empleados:
            total = total + empleado.get_salario()
        print("Salario total: ", total)
        return total

