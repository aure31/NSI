
/* Creation de la table des acteurs */

CREATE TABLE IF NOT EXISTS acteurs (
          idActeur     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          nom	       text,
          prenom       text,
          birth	       date,
          site	       text
);

CREATE TABLE IF NOT EXISTS realisateurs (
		idRea      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nom	       text,
        prenom     text
);

/* Creation de la table des films */

CREATE TABLE IF NOT EXISTS films (
          iDfilm      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          titre       text,
          annee       INTEGER,
		  Realisateur INTEGER,
		  FOREIGN KEY (Realisateur) REFERENCES realisateurs(idRea)
);

/* Creation de l'association joueDans */

CREATE TABLE IF NOT EXISTS joueDans (
		film 	INTEGER,
		acteur  INTEGER,
		FOREIGN KEY (film) REFERENCES films(iDfilm),
		FOREIGN KEY (acteur) REFERENCES acteurs(iDActeur),
		PRIMARY KEY (film, acteur)
);








