from feedback_ud4_marcelo.menu_obtencion_datos import obtener_datos
from feedback_ud4_marcelo.pacientes import gestorPacientes as gP
from pandas import DataFrame as dF
from feedback_ud4_marcelo.graphics import modeladorGraficos as mG
from feedback_ud4_marcelo.pacientes.gestorPacientes import pacientes
from feedback_ud4_marcelo.pacientes.model.pacienteModel import Paciente
from feedback_ud4_marcelo.preprocesado.utils.normalizadores import NormalizadorDatos as nD

"""
-------------------------------------------------------------------------------------------
                                    CLASE EJECUTABLE
------------------------------------------------------------------------------------------- 
1. Lanza un menu interactivo para la obtención de datos de 30 pacientes.
2. Los datos obtenidos se duplican y se mantienen en dos listas distintas, 
    los datos de una de las listas son normalizados mientras que el otro grupo se mantiene
    exactamente como se obtuvieron.  
3. Muestra los gráficos correspondientes de cada una de la lista de datos.
"""

if __name__ == "__main__":

    for i in range(30):
        paciente = obtener_datos()
        gP.agregar_paciente(paciente)
        print("Registrando pacientes. " + str(i) + "/30")

    datos = dF(gP.recuperar_pacientes())

    for i in range(len(pacientes)):
        gP.actualizar_paciente(nD.normalizar_paciente(pacientes[i]), i)
    datos_normalizados = dF(gP.recuperar_pacientes())

    print("Sin normalizar")
    print(datos)

    print("Normalizados")
    print(datos_normalizados)

    mG.generar_graficos(datos, datos_normalizados)

