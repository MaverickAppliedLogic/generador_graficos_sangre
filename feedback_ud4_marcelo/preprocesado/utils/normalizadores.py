from feedback_ud4_marcelo.pacientes.model.pacienteModel import Paciente


class NormalizadorDatos:
    """
    -------------------------------------------------------------------
            CLASE PARA NORMALIZAR LOS DATOS DE UN PACIENTE
    -------------------------------------------------------------------
    Todos los métodos son estáticos, no hace falta instanciar la clase.
    """

    @staticmethod
    def normalizar_paciente(paciente: Paciente) -> Paciente:
        """
        Normaliza todos los atributos clínicos de un objeto Paciente.
        Devuelve el mismo objeto con los valores ajustados al rango normal.
        """
        paciente.hematies = NormalizadorDatos.normalizar_hematies(paciente.hematies, paciente.genero)
        paciente.hemoglobina = NormalizadorDatos.normalizar_hemoglobina(paciente.hemoglobina, paciente.genero)
        paciente.hematocrito = NormalizadorDatos.normalizar_hematocrito(paciente.hematocrito, paciente.genero)
        paciente.leucocitos = NormalizadorDatos.normalizar_leucocitos(paciente.leucocitos)
        paciente.vsg = NormalizadorDatos.normalizar_vsg(paciente.vsg, paciente.genero)
        paciente.hdl = NormalizadorDatos.normalizar_hdl(paciente.hdl)
        paciente.ldl = NormalizadorDatos.normalizar_ldl(paciente.ldl)
        paciente.colesterol = NormalizadorDatos.normalizar_colesterol(paciente.colesterol)
        paciente.trigliceridos = NormalizadorDatos.normalizar_trigliceridos(paciente.trigliceridos, paciente.genero)
        return paciente

    @staticmethod
    def normalizar_nombre(nombre: str, apellidos: str) -> str:
        """
        Devuelve el nombre completo en formato estándar: 'Apellidos, Nombre'.
        """
        nombre_completo = apellidos + ", " + nombre
        return nombre_completo

    @staticmethod
    def normalizar_genero(genero: str) -> str:
        """
        Normaliza el género a 'H' o 'M'.
        Acepta variantes como 'hombre', 'mujer', 'h', 'm'.
        Si no reconoce el valor, devuelve 'H' por defecto.
        """
        g = genero.strip().lower()
        if g in ["h", "hombre"]:
            return "H"
        elif g in ["m", "mujer"]:
            return "M"
        return "H"  # valor por defecto


    # --- MÉTODOS DE NORMALIZACIÓN ESPECÍFICOS ---

    @staticmethod
    def normalizar_hematies(valor: float, genero: str) -> float:
        """
        Normaliza el número de hematíes según el género.
        Hombres: 4.5–5.9 millones/µL
        Mujeres: 4.0–5.2 millones/µL
        """
        minimo, maximo = (4.5, 5.9) if genero == "H" else (4.0, 5.2)
        return NormalizadorDatos.ajustar_rango(valor, minimo, maximo)

    @staticmethod
    def normalizar_hemoglobina(valor: float, genero: str) -> float:
        """
        Normaliza la hemoglobina según el género.
        Hombres: 13.5–17.5 g/dL
        Mujeres: 12–16 g/dL
        """
        minimo, maximo = (13.5, 17.5) if genero == "H" else (12, 16)
        return NormalizadorDatos.ajustar_rango(valor, minimo, maximo)

    @staticmethod
    def normalizar_hematocrito(valor: float, genero: str) -> float:
        """
        Normaliza el hematocrito según el género.
        Hombres: 41–53 %
        Mujeres: 36–46 %
        """
        minimo, maximo = (41, 53) if genero == "H" else (36, 46)
        return NormalizadorDatos.ajustar_rango(valor, minimo, maximo)

    @staticmethod
    def normalizar_leucocitos(valor: float) -> float:
        """
        Normaliza el número de leucocitos.
        Rango normal: 4500–11500 /µL
        """
        return NormalizadorDatos.ajustar_rango(valor, 4500, 11500)

    @staticmethod
    def normalizar_vsg(valor: int, genero: str) -> int:
        """
        Normaliza la velocidad de sedimentación globular (VSG).
        Hombres: 0–10 mm/h
        Mujeres: 0–20 mm/h
        """
        minimo, maximo = (0, 10) if genero == "H" else (0, 20)
        return NormalizadorDatos.ajustar_rango(valor, minimo, maximo)

    @staticmethod
    def normalizar_hdl(valor: int) -> int:
        """
        Normaliza el colesterol HDL.
        Rango normal: 42–90 mg/dL
        """
        return NormalizadorDatos.ajustar_rango(valor, 42, 90)

    @staticmethod
    def normalizar_ldl(valor: int) -> int:
        """
        Normaliza el colesterol LDL.
        Rango normal: 0–160 mg/dL
        """
        return NormalizadorDatos.ajustar_rango(valor, 0, 160)

    @staticmethod
    def normalizar_colesterol(valor: int) -> int:
        """
        Normaliza el colesterol total.
        Rango normal: 120–200 mg/dL
        """
        return NormalizadorDatos.ajustar_rango(valor, 120, 200)

    @staticmethod
    def normalizar_trigliceridos(valor: int, genero: str) -> int:
        """
        Normaliza los triglicéridos según el género.
        Hombres: 30–280 mg/dL
        Mujeres: 30–220 mg/dL
        """
        minimo, maximo = (30, 280) if genero == "H" else (30, 220)
        return NormalizadorDatos.ajustar_rango(valor, minimo, maximo)

    @staticmethod
    def ajustar_rango(valor, minimo, maximo):
        """
        Ajusta un valor dentro de un rango dado.
        - Si el valor < mínimo → devuelve el mínimo.
        - Si el valor > máximo → devuelve el máximo.
        - Si está dentro → lo deja igual.
        """
        return max(min(valor, maximo), minimo)