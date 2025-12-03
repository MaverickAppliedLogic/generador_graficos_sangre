from feedback_ud4_marcelo.pacientes.model.pacienteModel import Paciente
'''
------------------------------------------------------------------------------
        MÓDULO ENCARGADO DE GUARDAR Y GESTIONAR PACIENTES EN MEMORIA
------------------------------------------------------------------------------

Guarda los pacientes en una lista y ofrece distintos métodos para trabajar con ella.
'''
pacientes= []

def agregar_paciente(paciente: Paciente):
    pacientes.append(paciente)

def actualizar_paciente(paciente: Paciente, index: int):
    pacientes[index] = paciente

def recuperar_pacientes()-> list[Paciente]:
    return pacientes