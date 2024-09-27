import sqlite3

# Fonction pour ajouter une suggestion dans la base de données
def add_suggestion(nom_materiel, nombre_materiel, description_materiel):
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO suggestion (titre, quantite, description) VALUES (?, ?, ?);', 
                   (nom_materiel, nombre_materiel, description_materiel))
    conn.commit()
    cursor.close()
    conn.close()

# Fonction pour récupérer toutes les suggestions de la base de données
def get_all_suggestions():
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT titre, quantite, description FROM suggestion')
    data = cursor.fetchall()
    conn.close()
    return data