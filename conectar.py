from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

camiones = [{
  "id": 1,
  "marca": "Chevrolet",
  "placa":"tgr-123"
}, {
  "id": 2,
  "marca": "JAC",
  "placa":"hdu-857"
},
{
  "id": 3,
  "marca": "Mercedez",
  "placa":"jud-098"
},
{
  "id": 4,
  "marca": "No idetificado",
  "placa":"slo-947"
},
{
  "id": 5,
  "marca": "Wrong",
  "placa":"pwu-267"
}]

class Camiones(Resource):
    def get(self, id):
        for u in camiones:
            if u["id"]==id:
                return u, 200
        return "El salvoconducto no se encontro", 404



@app.after_request
def add_security_headers(resp):
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

api.add_resource(Camiones,"/camion/<int:id>")
app.run(debug=True)
