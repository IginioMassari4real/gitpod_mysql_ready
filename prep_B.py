import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, nome_proprio VARCHAR(255), razza VARCHAR(255), peso INT, eta INT) VALUES (%s, %s)"
val = [
  ('Leone', 'mammifero', '200', '30'),
  ('Balena', 'mammifero', '1000', '25'),
  ('Delfino', 'mammifero', '200', '35'),
  ('Elefante', 'mammifero', '900', '40'),
  ('Lupo', 'mammifero', '150', '20'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "dati inseriti.")