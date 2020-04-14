#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"));
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and len(
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2


class MainHandler(webapp2.RequestHandler):

    def post(self):
        cif = str (self.request.get("cif"));
        cifC = str (self.request.get("cif-cliente"));
        nombre = str (self.request.get("nombre"));
        nombreC = str (self.request.get("nombre-cliente"));
        direccion = str (self.request.get("direccion"));
        direccionC = str (self.request.get("direccion-cliente"));
        poblacion = str (self.request.get("poblacion"));
        poblacionC = str (self.request.get("poblacion-cliente"));
        provincia = str (self.request.get("provincia"));
        provinciaC = str (self.request.get("provincia-cliente"));
        cpostal = str (self.request.get("cpostal"));
        cpostalC = str (self.request.get("cpostal-cliente"));
        pais = str (self.request.get("pais"));
        paisC = str (self.request.get("pais-cliente"));
        contacto = str (self.request.get("contacto"));
        contactoC = str (self.request.get("contacto-cliente"));
        email = str (self.request.get("email"));
        emailC = str (self.request.get("email-cliente"));
        telf = str (self.request.get("telf"));
        telfC = str (self.request.get("telf-cliente"));

        if len(cif.strip()) > 0 and len(nombre.strip()) > 0 and len(direccion.strip()) > 0 and len(poblacion.strip()) > 0 and len( provincia.strip()) > 0 and len( cpostal.strip()) > 0 and len( pais.strip()) > 0 and len( contacto.strip()) > 0 and len( email.strip()) > 8 and len( telf.strip()) > 0 and len( cifC.strip()) > 0 and len( nombreC.strip()) > 0 and len( direccionC.strip()) > 0 and len( poblacionC.strip()) > 0 and len( provinciaC.strip()) > 0 and len( cpostalC.strip()) > 0 and len( paisC.strip()) > 0 and len( contactoC.strip()) > 0 and len( emailC.strip()) > 0 and len( telfC.strip()) > 8:
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("detalleFactura.html"))
        else:
            self.response.write("Datos no validos")

app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
