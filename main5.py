import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Si crea una tabella customers con tre colonne: id, name, e address. La colonna id è un campo numerico (INT) che si incrementa automaticamente e fa da chiave primaria (PRIMARY KEY).