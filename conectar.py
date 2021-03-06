from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector
import numpy as np



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
        mycursor.execute("SELECT id, origen, destino, claseRecurso, descripcion, formaOtorgamiento, numero, volumen FROM salvoconducto WHERE numero = "+numero)
        myresult = mycursor.fetchall()[0]

        Salvo={}
        Salvo["id"]=myresult[0]
        Salvo["origen"]=myresult[1]
        Salvo["destino"]=myresult[2]
        Salvo["claseRecurso"]=myresult[3]
        Salvo["descripcion"]=myresult[4]
        Salvo["formaOtorgamiento"]=myresult[5]
        Salvo["numero"]=myresult[6]
        Salvo["volumen"]=myresult[7]


        mycursor.execute("SELECT idArbol,idSalvo FROM SalvoArbol WHERE idSalvo = "+str(Salvo["id"]))
        myresult = mycursor.fetchall()

        mycursor.execute("SELECT id, nombre, nombreCientifico,descripcion,urlImagen,densidad FROM maderas WHERE id = "+str(myresult[0][0]))
        myresult = mycursor.fetchall()[0]

        Salvo["idArb"]=myresult[0]
        Salvo["nombreArb"]=myresult[1]
        Salvo["nombreCientificoArb"]=myresult[2]
        Salvo["descripcionArb"]=myresult[3]
        Salvo["urlImagenArb"]=myresult[4]
        Salvo["densidadArb"]=myresult[4]


        mycursor.execute("SELECT idConductor,idSalvo FROM SalvoConductor WHERE idSalvo = "+str(Salvo["id"]))
        myresult = mycursor.fetchall()

        mycursor.execute("SELECT id, nombre, apellido, cedula FROM personas WHERE id = "+str(myresult[0][0]))
        myresult = mycursor.fetchall()[0]

        Salvo["idCon"]=myresult[0]
        Salvo["nombreCon"]=myresult[1]
        Salvo["apellidoCon"]=myresult[2]
        Salvo["cedulaCon"]=myresult[3]


        mycursor.execute("SELECT idEmpresa,idSalvo FROM SalvoEmpresa WHERE idSalvo = "+str(Salvo["id"]))
        myresult = mycursor.fetchall()

        mycursor.execute("SELECT id, nombre, nit FROM empresas WHERE id = "+str(myresult[0][0]))
        myresult = mycursor.fetchall()[0]

        Salvo["idEmpresa"]=myresult[0]
        Salvo["nombreEmpresa"]=myresult[1]
        Salvo["nitEmpresa"]=myresult[2]


        mycursor.execute("SELECT idCamion,idSalvo FROM SalvoCamion WHERE idSalvo = "+str(Salvo["id"]))
        myresult = mycursor.fetchall()

        mycursor.execute("SELECT id, marca, descripcion,placa FROM camiones WHERE id = "+str(myresult[0][0]))
        myresult = mycursor.fetchall()[0]

        Salvo["idCaminon"]=myresult[0]
        Salvo["marcaCamion"]=myresult[1]
        Salvo["descripcionCamion"]=myresult[2]
        Salvo["placaCamion"]=myresult[3]


        return Salvo, 200


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
        parser.add_argument("Placa")
        parser.add_argument("Cambios")
        args = parser.parse_args()
        Placa=args["Placa"]
        Decodificado=np.fromstring(args["Cambios"], np.int)
        Massa=np.reshape(Decodificado,(int(len(Decodificado)/3),3))
        densidad=10
        volumen=6
        Lugarllenado=[57,62]
        Masa=57
        for i in range(int(len(Decodificado)/3)):
            #or (Lugarllenado[0]!=Massa[i,0] and Lugarllenado[1]!=Massa[i,1])
            if (abs(Masa-Massa[i,2])>3):
                print("entro")
                Placa = Placa[0:6]
                Dicc={'Placa':Placa,'Alerta': True}
                mydb = mysql.connector.connect(
                  host="remotemysql.com",
                  port="3306",
                  user="qgbd0jGv86",
                  passwd="ZTOqEZrvAU",
                  database="qgbd0jGv86"
                )
                mycursor = mydb.cursor()
                sql="SELECT id,placa FROM camiones WHERE placa = '"+Placa+"'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()

                sql="INSERT INTO sosp(idCamion) VALUES("+str(myresult[0][0])+")"
                mycursor.execute(sql)
                mydb.commit()
                return None,201

        return None, 201

class Sosp(Resource):
    def get(self):
        mydb = mysql.connector.connect(
          host="remotemysql.com",
          port="3306",
          user="qgbd0jGv86",
          passwd="ZTOqEZrvAU",
          database="qgbd0jGv86"
        )
        mycursor = mydb.cursor()
        sql="SELECT * FROM sosp"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        so =[]
        for o in myresult:
            sql="SELECT id, marca, descripcion,placa FROM camiones WHERE id = "+str(o[0])
            mycursor.execute(sql)
            myres = mycursor.fetchall()[0]
            Salvo={}
            Salvo["id"]=myres[0]
            Salvo["marca"]=myres[1]
            Salvo["descripcion"]=myres[2]
            Salvo["placa"]=myres[3]
            so.append(Salvo)


        return so,201

@app.after_request
def add_security_headers(resp):
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

api.add_resource(Camiones,"/camion/<int:id>")
api.add_resource(Arboles,"/arbol/<int:id>")
api.add_resource(Salvo,"/salvo/<string:numero>")
api.add_resource(Postes,"/postes")
api.add_resource(Sosp,"/sosp")
app.run(host="0.0.0.0",debug=True)
