import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#Viene importata la libreria mysql.connector per connettersi a un database MySQL e poi viene stabilita una connessione al server locale (localhost). Infine, viene creato un nuovo database chiamato mydatabase.