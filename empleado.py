__author__ = 'Laura'


class Empleado():
    """Esta clase representa el empleado de un departamento"""

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """Metodo constructor de empleado

        En este metodo se define un objeto de tipo Empleado con sus atributos

        :param nombre: nombre del empleado
        :param apellidos: apellidos del empleado
        :param dni: documento de identidad del empleado
        :param direccion: direccion del empleado
        :param edad: edad del empleado
        :param email: correo electronico del empleado
        :param salario: salario anual del empleado
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """Metodo get del salario

        Este metodo toma el valor del salario anual del empleado

        :return: salario anual del empleado
        :rtype: float
        """
        return self.salario

    def get_dni(self):
        """Metodo get del dni

        Este metodo toma el valor del dni del empleado

        :return: dni del empleado
        :rtype: str
        """
        return self.dni

    def get_nombre_apellidos(self):
        """Metodo get del nombre y apellidos

        Este metodo toma el nombre completo del empleado que consta de su nombre y sus apellidos

        :return: nombre y apelldos del empleado
        :rtype: str
        """
        return self.nombre + ' ' + self.apellidos

    def get_edad(self):
        """Metodo get de la edad

        Este metodo toma el valor de la edad del empleado

        :return: edad del empleado
        :rtype: int
        """
        return self.edad

    def get_email(self):
        """Metodo get del email

        Este metodo toma el valor del correo electronico del empleado

        :return: email del empleado
        :rtype: str
        """
        return self.email

    def get_direccion(self):
        """Metodo get de la direccion

        Este metodo toma el valor de la direccion del empleado

        :return: direccion del empleado
        :rtype: str
        """
        return self.direccion

    def get_salario_mensual(self):
        """Metodo get del salario mensual

        Este metodo toma el valor del salario mensual del empleado a partir de su
        salario anual dividiendolo entre 12

        :return: salario mensual del empleado
        :rtype: float
        """
        return self.get_salario() / 12.0



