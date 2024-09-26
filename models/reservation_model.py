import sqlite3

def get_available_materials(date):
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    query = '''
    SELECT m.nom, m.stock - IFNULL(COUNT(r.id_materiel), 0) AS disponible
    FROM materiel m
    LEFT JOIN reservation r ON m.id = r.id_materiel
    AND r.date_emprunt = ?
    GROUP BY m.id
    '''
    cursor.execute(query, (date,))
    available_materials = cursor.fetchall()
    conn.close()
    return available_materials

def confirm_reservation_db(data, user_id):
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    
    for material in data.get('materials', []):
        cursor.execute('''
            INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel)
            VALUES (?, ?, ?, ?, (SELECT id FROM materiel WHERE nom = ?))
        ''', (data['date_emprunt'], 9, 18, user_id, material))
    
    conn.commit()
    conn.close()
    return {"success": True, 'redirect': '/reservation'}
