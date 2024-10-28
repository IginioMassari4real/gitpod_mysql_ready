import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

#Questo codice connette al database e recupera solo il primo record della tabella customers utilizzando fetchone(), che ritorna un singolo risultato invece di tutti i record.