import requests

class CartoCiudadService:

    def buscar_direccion(provincia: str, ciudad: str, cp: str, calle: str, numero: str)->bool:

        xml_body = f"""<?xml version="1.0" encoding="UTF-8"?>
        <wps:Execute service="WPS" version="1.0.0"
         xmlns:wps="http://www.opengis.net/wps/1.0.0"
         xmlns:ows="http://www.opengis.net/ows/1.1"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.opengis.net/wps/1.0.0
         http://schemas.opengis.net/wps/1.0.0/wpsExecute_request.xsd">
          <ows:Identifier>org.cnig.cartociudad.wps.GeocodeAddress</ows:Identifier>
          <wps:DataInputs>
            <wps:Input>
              <ows:Identifier>province</ows:Identifier>
              <wps:Data><wps:LiteralData>{provincia}</wps:LiteralData></wps:Data>
            </wps:Input>
            <wps:Input>
              <ows:Identifier>city</ows:Identifier>
              <wps:Data><wps:LiteralData>{ciudad}</wps:LiteralData></wps:Data>
            </wps:Input>
            <wps:Input>
              <ows:Identifier>road_type</ows:Identifier>
              <wps:Data><wps:LiteralData>Calle</wps:LiteralData></wps:Data>
            </wps:Input>
            <wps:Input>
              <ows:Identifier>road_name</ows:Identifier>
              <wps:Data><wps:LiteralData>{calle}</wps:LiteralData></wps:Data>
            </wps:Input>
            <wps:Input>
              <ows:Identifier>road_number</ows:Identifier>
              <wps:Data><wps:LiteralData>{numero}</wps:LiteralData></wps:Data>
            </wps:Input>
            <wps:Input>
              <ows:Identifier>max_results</ows:Identifier>
              <wps:Data><wps:LiteralData>5</wps:LiteralData></wps:Data>
            </wps:Input>
          </wps:DataInputs>
        </wps:Execute>
        """

        response = requests.post("https://www.cartociudad.es/wps", data=xml_body, headers={"Content-Type": "application/xml"})
        print(response.text)
