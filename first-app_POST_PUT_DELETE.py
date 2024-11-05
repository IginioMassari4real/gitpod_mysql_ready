from flask import Flask, jsonify, request
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
    try:
        connessione = connetti_db()
        cursore = connessione.cursor(dictionary=True)
        cursore.execute("SELECT * FROM Mammiferi")
        animali = cursore.fetchall()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursore.close()
        connessione.close()
    
    return jsonify(animali)

# Route per aggiungere un nuovo animale (POST)
@app.route('/api/animali', methods=['POST'])
def add_animale():
    nuovo_animale = request.json
    nome = nuovo_animale.get('nome')
    specie = nuovo_animale.get('specie')

    if not nome or not specie:
        return jsonify({"error": "Nome e specie sono obbligatori"}), 400

    try:
        connessione = connetti_db()
        cursore = connessione.cursor()
        cursore.execute("INSERT INTO Mammiferi (nome, specie) VALUES (%s, %s)", (nome, specie))
        connessione.commit()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursore.close()
        connessione.close()
    
    return jsonify({"message": "Animale aggiunto con successo"}), 201

# Route per aggiornare un animale esistente (PUT)
@app.route('/api/animali/<int:id>', methods=['PUT'])
def update_animale(id):
    dati_aggiornati = request.json
    nome = dati_aggiornati.get('nome')
    specie = dati_aggiornati.get('specie')

    if not nome or not specie:
        return jsonify({"error": "Nome e specie sono obbligatori"}), 400

    try:
        connessione = connetti_db()
        cursore = connessione.cursor()
        cursore.execute("UPDATE Mammiferi SET nome = %s, specie = %s WHERE id = %s", (nome, specie, id))
        connessione.commit()

        if cursore.rowcount == 0:
            return jsonify({"error": "Animale non trovato"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursore.close()
        connessione.close()
    
    return jsonify({"message": "Animale aggiornato con successo"})

# Route per cancellare un animale (DELETE)
@app.route('/api/animali/<int:id>', methods=['DELETE'])
def delete_animale(id):
    try:
        connessione = connetti_db()
        cursore = connessione.cursor()
        cursore.execute("DELETE FROM Mammiferi WHERE id = %s", (id,))
        connessione.commit()

        if cursore.rowcount == 0:
            return jsonify({"error": "Animale non trovato"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursore.close()
        connessione.close()
    
    return jsonify({"message": "Animale cancellato con successo"})

# Avvia l'app Flask
if __name__ == '__main__':
    app.run(debug=True)