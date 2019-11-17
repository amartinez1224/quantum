import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  port="3306",
  user="qgbd0jGv86",
  passwd="ZTOqEZrvAU",
  database="qgbd0jGv86"
)

mycursor = mydb.cursor()


sql = "INSERT INTO maderas (nombre, nombreCientifico,descripcion,urlImagen) VALUES (%s, %s, %s, NULL)"
val = ("Nealchornea yapurensis", "Nealchornea Yapurensis","Lorem Impus Dolorem")
mycursor.execute(sql, val)

mydb.commit()

'''
mycursor.execute("SHOW COLUMNS FROM maderas")
mycursor.execute("SELECT * FROM maderas")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
'''
