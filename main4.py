import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Una volta connessi al database mydatabase, si esegue il comando SHOW TABLES per elencare tutte le tabelle presenti nel database e se ne stampano i nomi.