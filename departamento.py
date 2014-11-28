__author__ = 'Laura'


class Departamento():
    """Esta clase representa el departamento de una empresa"""

    def __init__(self, nombre_depto, id_depto):
        """Metodo constructor de departamento

        En este metodo se define un objeto de tipo Departamento con sus atributos

        :param nombre_depto: nombre del departamento
        :type nombre_depto: str
        :param id_depto: numero de identificacion del departamento
        :type id_depto: str
        :param empleados: lista de empleados vacia
        :type empleados: list
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self, empleado):
        """Metodo aniadir empleado

        Este metodo se usa para aniadir un nuevo empleado a la lista de empleados del departamento

        :param empleado: empleado que se va a aniadir a la lista de empleados del departamento
        :type empleado: empleado
        """
        self.empleados.append(empleado)

    def get_salario_total(self):
        """Metodo get del salario total

        Este metodo toma la suma del salario total de todos los empleados del departamento

        :param total: variable que guarda la suma de todos los salarios de los empleados del departamento
        :return: total
        :rtype: float
        """
        total = 0
        for empleado in self.empleados:
            total = total + empleado.get_salario()
        return total

    def get_nombre_dpto(self):
        """Metodo get nombre del departamento

        Este metodo toma el nombre del departamento

        :return: nombre del departamento
        :rtype: str
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """Metodo get salario mensual total

        Este metodo calcula el salario total mensual de todos los empleados del departamento

        :return: salario mensual total de todos los empleados del departamento
        :rtype: float
        """
        return self.get_salario_total() / 12.0
