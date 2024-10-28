import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#Dopo aver stabilito una connessione al database mydatabase, si crea una tabella chiamata customers con due colonne: name e address, entrambe di tipo VARCHAR con un limite massimo di 255 caratteri.