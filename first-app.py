from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Funzione per connettersi al database MySQL
def connetti_db():
    return mysql.connector.connect(
        host="localhost",      # Cambia con l'host del tuo database
        user="root",       # Cambia con il tuo username
        password="",   # Cambia con la tua password
        database="Animali"         # Cambia con il nome del tuo database
    )

# Route per ottenere i dati in formato JSON
@app.route('/api/animali', methods=['GET'])
def get_animali():
    connessione = connetti_db()
    cursore = connessione.cursor(dictionary=True)  # `dictionary=True` per ottenere risultati come dizionari
    cursore.execute("SELECT * FROM Mammiferi")
    animali = cursore.fetchall()
    cursore.close()
    connessione.close()
    return jsonify(animali)  # Converte la lista di dizionari in JSON

# Avvia l'app Flask
if __name__ == '__main__':
    app.run(debug=True)
