#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


class MainHandler(webapp2.RequestHandler):

    def post(self):
        km = float(self.request.get("km", -1))
        time = float(self.request.get("time", -1))
        cons = float(self.request.get("consumption", -1))
        if km < 0 or time < 0 or cons < 0:
            self.response.write("Datos no validos")

        self.response.write(
            "Velocidad media (km/hora): " + str(round(km / time, 2)) + "<br>Consumo total: " + str(
                round(cons * km / 100, 2)))


app = webapp2.WSGIApplication([
    ('/car', MainHandler)
], debug=True)
