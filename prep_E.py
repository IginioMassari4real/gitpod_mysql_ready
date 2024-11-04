import mysql.connector

connessione = mysql.connector.connect(
    host="localhost",      
    user="root",       
    password="",   
    database="Animali"         
)

cursore = connessione.cursor()

query = "SELECT nome, tipo, età, peso FROM animali WHERE peso > 2"

cursore.execute(query)

animali = cursore.fetchall()

print("Animali che pesano più di 2 kg:")
for animale in animali:
    nome, tipo, età, peso = animale
    print(f"- Nome: {nome}, Tipo: {tipo}, Età: {età}, Peso: {peso} kg")

cursore.close()
connessione.close()