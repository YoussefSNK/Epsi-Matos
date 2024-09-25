DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    password TEXT NOT NULL
    id_1 INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_1) REFERENCES suggestion(id)
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

DROP TABLE IF EXISTS suggestion;
CREATE TABLE suggestion(
   id INT,
   titre VARCHAR(50) NOT NULL,
   quantite INT NOT NULL,
   description VARCHAR(180),
   PRIMARY KEY(id)
);

DROP TABLE IF EXISTS jaime;
CREATE TABLE jaime(
   id INT,
   id_1 INT NOT NULL,
   id_2 INT NOT NULL,
   PRIMARY KEY(id),
   FOREIGN KEY(id_1) REFERENCES suggestion(id),
   FOREIGN KEY(id_2) REFERENCES user(id)
);