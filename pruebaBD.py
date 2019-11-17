import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  port="3306",
  user="qgbd0jGv86",
  passwd="ZTOqEZrvAU",
  database="qgbd0jGv86"
)

mycursor = mydb.cursor()

'''
sql = "INSERT INTO  salvoconducto(origen, destino, claseRecurso, descripcion, formaOtorgamiento, numero, volumen) VALUES (%s, %s, %s, %s,%s,%s,%s)"
val = ("Putumayo", "Cali","Rollado", "Loren Impus Dolorem","En oficina", "34567","10")
mycursor.execute(sql, val)

mydb.commit()


mycursor.execute("ALTER TABLE salvoconducto ADD COLUMN volumen INT ")




(bytearray(b'SalvoArbol'),)
(bytearray(b'SalvoCamion'),)
(bytearray(b'SalvoConductor'),)
(bytearray(b'SalvoEmpresa'),)
(bytearray(b'camiones'),)
(bytearray(b'empresas'),)
(bytearray(b'maderas'),)
(bytearray(b'personas'),)
(bytearray(b'salvoconducto'),)

'''

#mycursor.execute("SHOW COLUMNS FROM maderas")

#mycursor.execute("INSERT INTO SalvoCamion(idSalvo,idCamion) VALUES (1,1)")
#mycursor.execute("INSERT INTO personas (nombre,apellido,cedula) VALUES ('Nicolas','vergara',12345)")

sql = "CREATE TABLE sosp (idCamion int, FOREIGN KEY (idCamion) REFERENCES camiones(id))"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM sosp")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
