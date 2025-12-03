
from dataclasses import dataclass

@dataclass
class Paciente:
    nombre_completo: str
    genero: str
    direccion: str
    tlf: int
    hematies: float
    hemoglobina: float
    hematocrito: float
    leucocitos: float
    vsg: int
    hdl: int
    ldl: int
    colesterol: int
    trigliceridos: int


