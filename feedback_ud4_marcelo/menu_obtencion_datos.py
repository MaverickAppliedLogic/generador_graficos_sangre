from feedback_ud4_marcelo.pacientes.model.pacienteModel import Paciente
from feedback_ud4_marcelo.preprocesado.data_preprocessor import DataPreprocessor as DtP

def obtener_datos() -> Paciente:
    """
    ---------------------------------------------------------------------------------------
                FUNCION INTERACTIVA PARA CAPTURAR LOS DATOS DE UN PAICENTE
    ---------------------------------------------------------------------------------------
    Aplica preprocesamiento y validación a cada campo antes de construir el objeto Paciente.
    """

    print("INSERTAR PACIENTES: ")
    print("-----------------------")

    # --- Datos personales ---
    nombre = DtP.name_preprocessing(input("Nombre: "), input("Apellidos: "))# Devuleve formato 'Apellidos, Nombre'
    genero = DtP.genero_preprocessing(input("Género (H/M): "))
    print(genero)
    direccion = obtener_direccion()
    telefono = -1
    while telefono == -1:
        telefono = DtP.telefono_preprocessing(input("Teléfono: "))# Teléfono: se repite la petición hasta que sea válido


    # --- Parámetros del hemograma ---
    # Cada valor se valida con el preprocesador, que imprime aviso si es anómalo
    hematies = DtP.hematies_preprocessing(float(input("Hematíes (millones/mm3): ")), genero)
    hemoglobina = DtP.hemoglobina_preprocessing(float(input("Hemoglobina (g/dl): ")), genero)
    hematocrito = DtP.hematocrito_preprocessing(float(input("Hematocrito (%): ")), genero)
    leucocitos = DtP.leucocitos_preprocessing(int(input("Leucocitos (WBC, mL): ")))
    vsg = DtP.vsg_preprocessing(int(input("VSG (mm/h): ")), genero)
    hdl = DtP.hdl_preprocessing(int(input("HDL (mg/dl): ")))
    ldl = DtP.ldl_preprocessing(int(input("LDL (mg/dl): ")))
    colesterol = DtP.colesterol_preprocessing(hdl + ldl)# Colesterol total calculado como HDL + LDL y validado
    trigliceridos = DtP.trigliceridos_preprocessing(int(input("Triglicéridos (mg/dl): ")), genero)

    print("\nDatos capturados correctamente.")

    # Se construye y devuelve el objeto Paciente con todos los datos capturados
    return Paciente(
        nombre_completo=nombre,
        genero=genero,
        direccion=str(direccion),
        tlf=telefono,
        hematies=hematies,
        hemoglobina=hemoglobina,
        hematocrito=hematocrito,
        leucocitos=leucocitos,
        vsg=vsg,
        hdl=hdl,
        ldl=ldl,
        colesterol=colesterol,
        trigliceridos=trigliceridos
    )


def obtener_direccion() -> dict:
    """
    ----------------------------------------------------------------
        FUNCION AUXILIAR PARA CAPTURAR LA DIRECCION DE UN PACIENTE
    ----------------------------------------------------------------
    Devuelve un diccionario con los campos básicos de localización.
    """
    return {
        "calle": input("Calle: "),
        "numero": input("Número: "),
        "cp": input("Código postal: "),
        "ciudad": input("Ciudad: "),
        "provincia": input("Provincia: "),
        "pais": input("País: ")
    }
