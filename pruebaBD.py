import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  port="3306",
  user="qgbd0jGv86",
  passwd="ZTOqEZrvAU",
  database="qgbd0jGv86"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
