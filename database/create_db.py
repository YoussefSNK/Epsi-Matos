import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('admin', 'password'))
cur.execute("INSERT INTO user (login, password) VALUES (?, ?)",('salecon', 'G_R!xjZs7RC3C*.'))



cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Problème de problème', 'BJ99', 'Il y a un piège devant la porte', "Ouvert", "1"))
cur.execute("INSERT INTO signalement (titre, salle, description, etat, id_user) VALUES (?, ?, ?, ?, ?)",('Prise', 'BJ12', 'Les prises sont en feu', "Ouvert", "1"))


cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Bras Robot', '3'))
cur.execute("INSERT INTO materiel (nom, stock) VALUES (?, ?)",('Lampe Terrible', '0'))



connection.commit()
connection.close()
