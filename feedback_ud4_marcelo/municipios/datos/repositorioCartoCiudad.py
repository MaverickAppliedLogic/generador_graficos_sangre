from typing import Optional
from feedback_ud4_marcelo.services.cartoCiudadService import CartoCiudadService

class RepositorioCartoCiudad:

    @staticmethod
    def get_provincia(nombre: str) -> Optional[str]:
        datos = CartoCiudadService.get("Provincia", {"nombre": nombre})
        return datos.get("resultado", [{}])[0].get("nombre") if datos.get("resultado") else None

    @staticmethod
    def get_municipio(provincia: str, nombre: str) -> Optional[str]:
        datos = CartoCiudadService.get("Municipio", {"provincia": provincia, "nombre": nombre})
        return datos.get("resultado", [{}])[0].get("nombre") if datos.get("resultado") else None

    @staticmethod
    def get_cp(municipio: str, codigo: str) -> Optional[str]:
        datos = CartoCiudadService.get("CodigoPostal", {"municipio": municipio, "codigoPostal": codigo})
        return datos.get("resultado", [{}])[0].get("codigoPostal") if datos.get("resultado") else None

    @staticmethod
    def get_calle(municipio: str, nombre: str) -> Optional[str]:
        datos = CartoCiudadService.get("Via", {"municipio": municipio, "nombre": nombre})
        return datos.get("resultado", [{}])[0].get("idVia") if datos.get("resultado") else None

    @staticmethod
    def get_numero(calle: str, numero: str) -> Optional[str]:
        datos = CartoCiudadService.get("Portal", {"idVia": calle, "numero": numero})
        return datos.get("resultado", [{}])[0].get("numero") if datos.get("resultado") else None
