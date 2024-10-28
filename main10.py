import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Questo codice esegue una query per selezionare solo i campi name e address dalla tabella customers. I risultati sono recuperati con fetchall() e stampati.