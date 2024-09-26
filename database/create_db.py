import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('admin', 'password'))
cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('hanen', 'G_R!xjZs7RC3C*.'))

cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Projecteur', 'BJ99', '', "ferme", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Prise', 'BJ12', 'Les prises sont en feu', "en-cours", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Enceinte', 'BJ99', 'L\'enceinte ne fonctionne pas', "a-traiter", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Prise', 'BJ12', 'Les prises sont en feu', "ferme", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Prise', 'BJ12', '', "en-cours", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Serveurs', 'MyDIL', 'Les serveurs sont en panne', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Serveurs', 'MyDIL', 'Trop de bruit !', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Chaise', 'B301', '5 chaises cassées (dangereux)', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Projecteur', 'B301', 'Marche une fois sur cinq', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Enceintes', 'B200', 'Pas de son', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Clime', 'B006', 'Pas de clime, horrible', 'en-cours', '1'))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Radio', 'MyDIL', 'Cassée', 'en-cours', '1'))

cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Imprimante 3D', '1'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('LED', '50'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Casque VR', '1'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Raspberry Pi 3', '3'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Serveur', '4'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Arduino', '2'))



connection.commit()
connection.close()
