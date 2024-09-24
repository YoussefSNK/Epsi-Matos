DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS signalement;
CREATE TABLE signalement(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    salle TEXT NOT NULL,
    description TEXT NOT NULL,
    etat TEXT NOT NULL,
    id_user INTEGER,
    FOREIGN KEY (id_user) REFERENCES user(id)
);


DROP TABLE IF EXISTS materiel;
CREATE TABLE materiel(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    stock INTEGER
);


DROP TABLE IF EXISTS reservation;
CREATE TABLE reservation(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_emprunt TEXT NOT NULL,
    debut_emprunt_heure INT NOT NULL,
    fin_emprunt_heure INT NOT NULL,
    id_user INTEGER,
    id_materiel INTEGER,
    FOREIGN KEY (id_user) REFERENCES user(id),
    FOREIGN KEY (id_materiel) REFERENCES materiel(id)

);
