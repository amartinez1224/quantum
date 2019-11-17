from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector




app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
      app.run(host='192.168.132.86', port=5000,debug=True)


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

class Salvo(Resource):
    def get(self, numero):
        mydb = mysql.connector.connect(
          host="remotemysql.com",
          port="3306",
          user="qgbd0jGv86",
          passwd="ZTOqEZrvAU",
          database="qgbd0jGv86"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id, origen, destino, claseRecurso, descripcion, formaOtorgamiento, numero, volumen FROM salvoconducto WHERE numero = '"+numero+"'")
        myresult = mycursor.fetchall()
        return myresult, 200

class Arboles(Resource):
    def get(self, id):
        mydb = mysql.connector.connect(
          host="remotemysql.com",
          port="3306",
          user="qgbd0jGv86",
          passwd="ZTOqEZrvAU",
          database="qgbd0jGv86"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM maderas")
        myresult = mycursor.fetchall()
        return myresult, 200



class Postes(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("x")
        parser.add_argument("y")
        parser.add_argument("dis")
        args = parser.parse_args()
        print(args)
        return None, 201


@app.after_request
def add_security_headers(resp):
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

api.add_resource(Camiones,"/camion/<int:id>")
api.add_resource(Arboles,"/arbol/<int:id>")
api.add_resource(Salvo,"/salvo/<string:numero>")
api.add_resource(Postes,"/postes")
