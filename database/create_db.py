import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('admin', 'password'))
cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('abc', 'abc'))
cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('salecon', 'G_R!xjZs7RC3C*.'))

cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Problème de problème', 'BJ99', 'Il y a un piège devant la porte', "Ouvert", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Prise', 'BJ12', 'Les prises sont en feu', "Ouvert", "1"))

cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Bras Robot', '3'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Lampe Terrible', '1'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Chaise', '0'))

cur.execute("INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel) VALUES (?, ?, ?, ?, ?)",('2024-09-30', 9, 18, 1, 1))
cur.execute("INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel) VALUES (?, ?, ?, ?, ?)",('2024-09-30', 9, 13, 1, 0))
cur.execute("INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel) VALUES (?, ?, ?, ?, ?)",('2024-09-24', 9, 13, 0, 0))
cur.execute("INSERT INTO reservation (date_emprunt, debut_emprunt_heure, fin_emprunt_heure, id_user, id_materiel) VALUES (?, ?, ?, ?, ?)",('2024-09-24', 9, 13, 0, 1))



connection.commit()
connection.close()
