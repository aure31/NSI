
/* Insertion des acteurs */

INSERT INTO acteurs VALUES (1,'Depp','Johnny','1963-06-09',
       'http://www.johnny-depp.net/');

INSERT INTO acteurs VALUES (2,'McQueen','Steve','1930-05-24',
       'http://members.tripod.com/~stvmcqueen/index.html');

INSERT INTO acteurs VALUES (3,'Stallone','Sylvester','1946-07-06',
       'http://www.sylvesterstallone.com/');

INSERT INTO acteurs VALUES (4,'Hanks','Tom','1956-07-09',
       'http://www.tomhanksland.com/');

INSERT INTO acteurs VALUES (5,'Smith','Will','1968-09-25',
       'http://www.willsmith.net/intro_flash.html');

INSERT INTO acteurs VALUES (6,'Malden','Karl','1914-03-22',
       'http://www.reelclassics.com/Actors/Malden/malden.htm');
	   
INSERT INTO acteurs VALUES (7,'Knightley','Keira','1985-03-26',
       'https://queenknightley.fr/');
	   
INSERT INTO acteurs VALUES (8,'Grant','Hugh','1960-09-09',
       'https://fr.wikipedia.org/wiki/Hugh_Grant');
	   
INSERT INTO acteurs VALUES (9,'Bonham Carter','Elena','1966-05-26',
       'https://fr.wikipedia.org/wiki/Helena_Bonham_Carter');
	   
INSERT INTO acteurs VALUES (10,'Pitt','Brad','1963-12-18',
       'https://fr.wikipedia.org/wiki/Brad_Pitt');
	   
INSERT INTO acteurs VALUES (11, 'Waltz', 'Christoph', '1956-10-04',
       'https://fr.wikipedia.org/wiki/Brad_Pitt');
	   
INSERT INTO acteurs VALUES (12, 'Clooney', 'Georges', '1961-05-06',
       'https://fr.wikipedia.org/wiki/Christoph_Waltz');
	   
INSERT INTO acteurs VALUES (13, 'Foxx', 'Jamie', '1967-10-13',
       'https://fr.wikipedia.org/wiki/Jamie_Foxx');
	   
INSERT INTO acteurs VALUES (14, 'Jackson', 'Samuel L.', '1948-12-21',
       'https://fr.wikipedia.org/wiki/Samuel_L._Jackson');	   
	   
INSERT INTO acteurs VALUES (15, 'Thurman', 'Uma', '1970-04-29',
       'https://fr.wikipedia.org/wiki/Uma_Thurman');	 
	   
INSERT INTO acteurs VALUES (16, 'Willis', 'Bruce', '1955-03-19',
       'https://fr.wikipedia.org/wiki/Bruce_Willis');	
	   
INSERT INTO acteurs VALUES (17, 'Norton', 'Edward', '1969-08-18',
       'https://fr.wikipedia.org/wiki/Edward_Norton');	
	  


/* Insertion des Realisteurs */
INSERT INTO realisateurs VALUES (1, 'Burton', 'Tim');
INSERT INTO realisateurs VALUES (2, 'Sturges', 'John');
INSERT INTO realisateurs VALUES (3, 'Avildsen', 'John G.');
INSERT INTO realisateurs VALUES (4, 'Zemeckis', 'Robert');
INSERT INTO realisateurs VALUES (5, 'Spielberg', 'Steven');
INSERT INTO realisateurs VALUES (6, 'Sonnenfeld', 'Barry');
INSERT INTO realisateurs VALUES (7, 'Lawrence', 'Francis');
INSERT INTO realisateurs VALUES (8, 'Demme', 'Jonathan');
INSERT INTO realisateurs VALUES (9, 'Darabont', 'Frank');
INSERT INTO realisateurs VALUES (10, 'Verbinski', 'Gore');
INSERT INTO realisateurs VALUES (11, 'Curtis', 'Richard');
INSERT INTO realisateurs VALUES (12, 'Tyldum', 'Morten');
INSERT INTO realisateurs VALUES (13, 'Fincher', 'David');
INSERT INTO realisateurs VALUES (14, 'Tarantino', 'Quentin');
INSERT INTO realisateurs VALUES (15, 'Cohen', 'Freres');
INSERT INTO realisateurs VALUES (16, 'Soderbergh', 'Steven');
INSERT INTO realisateurs VALUES (17, 'Yates', 'David');
INSERT INTO realisateurs VALUES (18, 'Fincher', 'David');
INSERT INTO realisateurs VALUES (19, 'Niccol', 'Andrew');
INSERT INTO realisateurs VALUES (20, 'Shyamalan', 'Night');
INSERT INTO realisateurs VALUES (21, 'Gilliam', 'Terry');
INSERT INTO realisateurs VALUES (22, 'Anderson', 'Wes');


/* Insertion des films */

INSERT INTO films VALUES (1, 'Sleepy Hollow',1999,1);
INSERT INTO films VALUES (2, 'La grande evasion',1963, 2);
INSERT INTO films VALUES (3, 'Rocky',1976, 3);
INSERT INTO films VALUES (4, 'Forrest Gump',1994, 4);
INSERT INTO films VALUES (5, 'Il faut sauver le soldat Ryan',1998, 5);
INSERT INTO films VALUES (6, 'Men in black',1997, 6);
INSERT INTO films VALUES (7, 'Je suis un legende', 2007, 7);
INSERT INTO films VALUES (8, 'Philadelphia', 1993, 8);
INSERT INTO films VALUES (9, 'La ligne Verte', 1999, 9);
INSERT INTO films VALUES (10, 'Pirate des Caraibes', 2003, 10);
INSERT INTO films VALUES (11, 'Love Actually', 2003, 11);
INSERT INTO films VALUES (12, 'Imitation Game', 2014, 12);
INSERT INTO films VALUES (13, 'Big Fish', 2003, 1);
INSERT INTO films VALUES (14, 'Alice au pays des merveilles', 2010, 1);
INSERT INTO films VALUES (15, 'Fight Club', 1999, 13);
INSERT INTO films VALUES (16, 'Charlie et la chocolaterie', 2005, 1);
INSERT INTO films VALUES (17, 'Inglourious Basterds', 2009, 14);
INSERT INTO films VALUES (18, 'Burn After Reading', 2008, 15);
INSERT INTO films VALUES (19, 'Oceans Eleven', 2001, 16);
INSERT INTO films VALUES (20, 'Django unchained', 2012, 14);
INSERT INTO films VALUES (21, 'Tarzan', 2016, 17);
INSERT INTO films VALUES (22, 'Pulp Fiction', 1994, 14);
INSERT INTO films VALUES (23, 'Bienvenue a Gattaca', 1997, 19);
INSERT INTO films VALUES (24, 'Kill Bill', 2003, 14);
INSERT INTO films VALUES (25, 'Incassable', 2003, 20);
INSERT INTO films VALUES (26, '12 Monkeys', 1995, 21);
INSERT INTO films VALUES (27, 'Oceans twelve', 2004, 16);
INSERT INTO films VALUES (28, 'Glass', 2019, 20);
INSERT INTO films VALUES (29, 'Moonrise Kingdom', 2012, 22);

/* Insertion des associations Films/Acteurs */

INSERT INTO joueDans VALUES (1, 1);
INSERT INTO joueDans VALUES (2, 2);
INSERT INTO joueDans VALUES (3, 3);
INSERT INTO joueDans VALUES (4, 4);
INSERT INTO joueDans VALUES (5, 4);
INSERT INTO joueDans VALUES (6, 5);
INSERT INTO joueDans VALUES (5, 7);
INSERT INTO joueDans VALUES (8, 4);
INSERT INTO joueDans VALUES (9, 4);
INSERT INTO joueDans VALUES (10, 1);
INSERT INTO joueDans VALUES (10, 7);
INSERT INTO joueDans VALUES (11, 8);
INSERT INTO joueDans VALUES (11, 7);
INSERT INTO joueDans VALUES (12, 7);
INSERT INTO joueDans VALUES (13, 9);
INSERT INTO joueDans VALUES (14, 1);
INSERT INTO joueDans VALUES (14, 9);
INSERT INTO joueDans VALUES (15, 9);
INSERT INTO joueDans VALUES (15, 10);
INSERT INTO joueDans VALUES (16, 1);
INSERT INTO joueDans VALUES (16, 9);
INSERT INTO joueDans VALUES (17, 10);
INSERT INTO joueDans VALUES (17, 11);
INSERT INTO joueDans VALUES (18, 10);
INSERT INTO joueDans VALUES (19, 10);
INSERT INTO joueDans VALUES (18, 12);
INSERT INTO joueDans VALUES (19, 12);
INSERT INTO joueDans VALUES (20, 11);
INSERT INTO joueDans VALUES (20, 13);
INSERT INTO joueDans VALUES (21, 11);
INSERT INTO joueDans VALUES (21, 14);
INSERT INTO joueDans VALUES (17, 14);
INSERT INTO joueDans VALUES (20, 14);
INSERT INTO joueDans VALUES (22, 14);
INSERT INTO joueDans VALUES (22, 15);
INSERT INTO joueDans VALUES (23, 15);
INSERT INTO joueDans VALUES (24, 15);
INSERT INTO joueDans VALUES (22, 16);
INSERT INTO joueDans VALUES (25, 14);
INSERT INTO joueDans VALUES (25, 16);
INSERT INTO joueDans VALUES (26, 16);
INSERT INTO joueDans VALUES (26, 10);
INSERT INTO joueDans VALUES (27, 16);
INSERT INTO joueDans VALUES (27, 10);
INSERT INTO joueDans VALUES (27, 12);
INSERT INTO joueDans VALUES (28, 14);
INSERT INTO joueDans VALUES (28, 16);
INSERT INTO joueDans VALUES (29, 16);
INSERT INTO joueDans VALUES (29, 17);
INSERT INTO joueDans VALUES (15, 17);












