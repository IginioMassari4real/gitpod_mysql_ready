import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#Si effettua una connessione al server MySQL usando le credenziali e poi si esegue il comando SHOW DATABASES per visualizzare tutti i database esistenti nel server e si stampano i nomi dei database trovati.