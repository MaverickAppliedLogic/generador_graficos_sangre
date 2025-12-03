# Importamos las utilidades de validación y normalización
from feedback_ud4_marcelo.preprocesado.utils.validadores import Validador as vP
from feedback_ud4_marcelo.preprocesado.utils.normalizadores import NormalizadorDatos as nP

class DataPreprocessor:
    """
    --------------------------------------------------------------------
        CLASE ENCARGADA DEL PREPROCESAMIENTO DE LOS DATOS DE ENTRADA
    --------------------------------------------------------------------
    Combina validación (Validador) y normalización (NormalizadorDatos).
    Todos los métodos son estáticos, no requiere instanciación.
    """

    @staticmethod
    def name_preprocessing(nombre: str, apellidos: str) -> str:
        """
        Preprocesa el nombre completo.
        Usa el normalizador para devolver 'Apellidos, Nombre'.
        """
        return nP.normalizar_nombre(nombre, apellidos)

    @staticmethod
    def genero_preprocessing(genero: str) -> str:
        """
        Preprocesa el género.
        Usa el normalizador para devolver 'H' o 'M'.
        """
        return nP.normalizar_genero(genero)

    @staticmethod
    def direccion_preprocessing(direccion: dict) -> str:
        """
        Preprocesa la dirección.
        - Valida la dirección contra el repositorio de cartografía.
        - Si no es válida, devuelve 'error'.
        - Si es válida, devuelve la dirección como string.
        """
        if not vP.validar_direccion(direccion):
            print("Dirección no válida.")
            return "error"
        else:
            print("Dirección válida")
            return str(direccion)

    @staticmethod
    def telefono_preprocessing(tlf: str) -> int:
        """
        Preprocesa el teléfono.
        - Si es válido, lo convierte a entero.
        - Si no es válido, devuelve -1.
        """
        if vP.validar_telefono(tlf):
            return int(tlf)
        else:
            return -1

    # --- PREPROCESAMIENTO DE PARÁMETROS CLÍNICOS ---
    @staticmethod
    def hematies_preprocessing(valor: float, genero: str) -> float:
        """
        Preprocesa el número de hematíes.
        - Valida el valor según género.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original (no lo ajusta).
        """
        if not vP.validar_hematies(valor, genero):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def hemoglobina_preprocessing(valor: float, genero: str) -> float:
        """
        Preprocesa la hemoglobina.
        - Valida el valor según género.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_hemoglobina(valor, genero):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def hematocrito_preprocessing(valor: float, genero: str) -> float:
        """
        Preprocesa el hematocrito.
        - Valida el valor según género.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_hematocrito(valor, genero):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def leucocitos_preprocessing(valor: float) -> float:
        """
        Preprocesa los leucocitos.
        - Valida el valor.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_leucocitos(valor):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def vsg_preprocessing(valor: int, genero: str) -> int:
        """
        Preprocesa la velocidad de sedimentación globular (VSG).
        - Valida el valor según género.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_vsg(valor, genero):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def hdl_preprocessing(valor: int) -> int:
        """
        Preprocesa el colesterol HDL.
        - Valida el valor.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_hdl(valor):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def ldl_preprocessing(valor: int) -> int:
        """
        Preprocesa el colesterol LDL.
        - Valida el valor.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_ldl(valor):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def colesterol_preprocessing(valor: int) -> int:
        """
        Preprocesa el colesterol total.
        - Valida el valor.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_colesterol(valor):
            print("!! VALOR ANÓMALO")
        return valor

    @staticmethod
    def trigliceridos_preprocessing(valor: int, genero: str) -> int:
        """
        Preprocesa los triglicéridos.
        - Valida el valor según género.
        - Si es anómalo, imprime aviso.
        - Devuelve el valor original.
        """
        if not vP.validar_trigliceridos(valor, genero):
            print("!! VALOR ANÓMALO")
        return valor
