import sqlite3

def get_tickets():
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT titre, salle, description, etat FROM signalement')
    data = cursor.fetchall()
    conn.close()
    return data
