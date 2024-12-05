import sqlite3

def execute_script(datafile, conn):
    cur = conn.cursor()
    sql_file = open(datafile)
    sql_as_string = sql_file.read()
    cur.executescript(sql_as_string)
    conn.commit()
    cur.close()

def reset_table(conn):
    execute_script('projetsql/delete.sql', conn)
    execute_script('projetsql/schema.sql', conn)
    execute_script('projetsql/datas.sql', conn)

operation = ['INSERT INTO', 'DELETE TABLE', 'UPDATE']
command =""

print('Que voulez vous faire ?')
print('1. insérer des données ?')
print('2. supprimer des données ?')
print('3. mettre à jour les données ?')
val = eval(input('Entrez votre choix : '))
if val > 3 or val < 1:
    print('Choix invalide')
    exit()

conn = sqlite3.connect('films.db')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'; ")
liste : list[str] = cur.fetchall()
lenth = len(liste)

cur.close()
conn.close()

for i in range(lenth):
    print(i+1,'. ',liste[i][0])

i = eval(input('Entrez votre choix : '))
table = liste[i-1][0]

conn = sqlite3.connect('films.db')
cur = conn.cursor()



cur.close()
conn.close()


conn = sqlite3.connect('films.db')
cur = conn.cursor()

cur.close()
conn.close()