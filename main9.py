import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Questo codice connette al database e seleziona tutti i record presenti nella tabella customers. Utilizza fetchall() per ottenere tutti i risultati della query, quindi li stampa uno per uno.