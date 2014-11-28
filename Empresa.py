__author__ = 'Laura'


class Empresa:
    """Esta clase representa la empresa"""

    def __init__(self, nombre_empresa, cif, razon_social):
        """Metodo constructor de empresa

        En este metodo se define un objeto de tipo Empresa con sus atributos

        :param nombre_empresa: nombre de la empresa
        :type nombre_empresa: str
        :param cif: codigo de identificacion fiscal de la empresa
        :type cif: str
        :param razon_social: denominacion por la que se conoce colectivamente a una empresa
        :type razon_social: str
        :param departamentos: lista de departamentos vacia de la empresa
        :type departamentos: list
        """

        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.departamentos = []