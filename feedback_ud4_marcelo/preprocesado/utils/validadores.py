# Importamos el repositorio de cartografía de ciudad,
# que nos permite validar provincias, municipios, códigos postales, calles y números
from feedback_ud4_marcelo.municipios.datos.repositorioCartoCiudad import RepositorioCartoCiudad as repCC

class Validador:
    """
    ------------------------------------------------------------------
        CLASE PARA VALIDAR DISTINTOS ATRIUBTOS DE UN PACIENTE.
    ------------------------------------------------------------------

    Incluye validaciones de teléfono, dirección y parámetros clínicos.
    """

    @staticmethod
    def validar_telefono(tlf: str) -> bool:
        """
        Valida que un teléfono cumpla las reglas básicas:
        - Debe ser numérico.
        - Debe empezar por 9, 6 o 7 (prefijos válidos en España).
        - Debe tener exactamente 9 dígitos.
        """
        if not tlf.isdigit():
            print("El teléfono debe ser totalmente numérico")
            return False
        elif not tlf.startswith(("9", "6", "7")):
            print("El número de teléfono no es válido")
            return False
        elif not tlf.__len__() == 9:
            print("El número de teléfono debe constar de 9 dígitos")
            return False
        else:
            return True

    @staticmethod
    def validar_direccion(direccion: dict) -> bool:
        """
        Valida que una dirección exista en el repositorio de cartografía.
        Comprueba provincia, municipio, código postal, calle y número.
        """
        if repCC.get_provincia(direccion.get("provincia")) is None:
            return False
        if repCC.get_municipio(direccion.get("provincia"), direccion.get("ciudad")) is None:
            return False
        if repCC.get_cp(direccion.get("ciudad"), direccion.get("cp")) is None:
            return False
        if repCC.get_calle(direccion.get("ciudad"), direccion.get("calle")) is None:
            return False
        if repCC.get_numero(direccion.get("calle"), direccion.get("numero")) is None:
            return False
        return True

    # --- VALIDACIONES CLÍNICAS ---
    @staticmethod
    def validar_hematies(valor: float, genero: str) -> bool:
        """
        Valida el número de hematíes según género.
        Hombres: 4.5–5.9 millones/µL
        Mujeres: 4.0–5.2 millones/µL
        """
        if genero == "H":
            return Validador.validar_rango(valor, 4.5, 5.9)
        else:
            return Validador.validar_rango(valor, 4.0, 5.2)

    @staticmethod
    def validar_hemoglobina(valor: float, genero: str) -> bool:
        """
        Valida la hemoglobina según género.
        Hombres: 13.5–17.5 g/dL
        Mujeres: 12–16 g/dL
        """
        if genero == "H":
            return Validador.validar_rango(valor, 13.5, 17.5)
        else:
            return Validador.validar_rango(valor, 12, 16)

    @staticmethod
    def validar_hematocrito(valor: float, genero: str) -> bool:
        """
        Valida el hematocrito según género.
        Hombres: 41–53 %
        Mujeres: 36–46 %
        """
        if genero == "H":
            return Validador.validar_rango(valor, 41, 53)
        else:
            return Validador.validar_rango(valor, 36, 46)

    @staticmethod
    def validar_leucocitos(valor: float) -> bool:
        """
        Valida el número de leucocitos.
        Rango normal: 4500–11500 /µL
        """
        return Validador.validar_rango(valor, 4500, 11500)

    @staticmethod
    def validar_vsg(valor: int, genero: str) -> bool:
        """
        Valida la velocidad de sedimentación globular (VSG).
        Hombres: 0–10 mm/h
        Mujeres: 0–20 mm/h
        """
        if genero == "H":
            return Validador.validar_rango(valor, 0, 10)
        else:
            return Validador.validar_rango(valor, 0, 20)

    @staticmethod
    def validar_hdl(valor: int) -> bool:
        """
        Valida el colesterol HDL.
        Rango normal: 42–90 mg/dL
        """
        return Validador.validar_rango(valor, 42, 90)

    @staticmethod
    def validar_ldl(valor: int) -> bool:
        """
        Valida el colesterol LDL (ojo: en tu código estaba escrito como 'vdl', aquí lo corrijo).
        Rango normal: 0–160 mg/dL
        """
        return Validador.validar_rango(valor, 0, 160)

    @staticmethod
    def validar_colesterol(valor: int) -> bool:
        """
        Valida el colesterol total.
        Rango normal: 120–200 mg/dL
        """
        return Validador.validar_rango(valor, 120, 200)

    @staticmethod
    def validar_trigliceridos(valor: int, genero: str) -> bool:
        """
        Valida los triglicéridos según género.
        Hombres: 30–280 mg/dL
        Mujeres: 30–220 mg/dL
        """
        if genero == "H":
            return Validador.validar_rango(valor, 30, 280)
        else:
            return Validador.validar_rango(valor, 30, 220)

    # --- MÉTODO AUXILIAR ---
    @staticmethod
    def validar_rango(valor, minimo, maximo) -> bool:
        """
        Comprueba si un valor está dentro de un rango [minimo, maximo].
        Devuelve True si está dentro, False si no.
        """
        return minimo <= valor <= maximo
