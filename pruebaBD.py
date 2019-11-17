import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  port="3306",
  user="qgbd0jGv86",
  passwd="ZTOqEZrvAU",
  database="qgbd0jGv86"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE salvoconducto ADD COLUMN volumen INT ")
'''
sql = "INSERT INTO  camiones(marca, descripcion,placa,urlImagen) VALUES (%s, %s, %s, NULL)"
val = ("Chevrolet", "Lorem Impus Dolorem","EHY234")
mycursor.execute(sql, val)

mydb.commit()

'''
mycursor.execute("SHOW COLUMNS FROM salvoconducto")
#mycursor.execute("SELECT * FROM maderas")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
