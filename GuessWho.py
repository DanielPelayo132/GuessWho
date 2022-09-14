import sqlite3

conn=sqlite3.connect('Destiny.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Destiny (
    Nombre TEXT PRIMARY KEY,
    Humano REAL NOT NULL,
    Exo REAL NOT NULL,
    Insomne REAL NOT NULL,
    Portaluz REAL NOT NULL,
    Cazador REAL NOT NULL,
    Titan REAL NOT NULL,
    Hechicero REAL NOT NULL,
    Armas REAL NOT NULL) """)

#c.execute("INSERT INTO Destiny VALUES ('Cayde-6' ,0,1,0,1,1,0,0,1)")
#c.execute("INSERT INTO Destiny VALUES ('Zavala'  ,0,0,1,1,0,1,0,1)")
#c.execute("INSERT INTO Destiny VALUES ('Saint-14',0,1,0,1,0,1,0,1)")
#c.execute("INSERT INTO Destiny VALUES ('Osiris'  ,1,0,0,0,0,0,1,1)")
#c.execute("INSERT INTO Destiny VALUES ('Ikora'   ,1,0,0,1,0,0,1,1)")
#c.execute("INSERT INTO Destiny VALUES ('Cuervo'  ,0,0,1,1,1,0,0,1)")
#conn.commit()

c.execute("SELECT * FROM Destiny")
Destiny=c.fetchall()

database=[]

for row in Destiny:        
    database.append({'Nombre':row[0],'Humano':bool(row[1]),'Exo':bool(row[2]),'Insomne':bool(row[3]),
    'Portaluz':bool(row[4]),'Cazador':bool(row[5]),'Titan':bool(row[6]),'Hechicero':bool(row[7]),
    'Armas':bool(row[8])},)
print(database)

def take_chance(answer,property):
    if answer == "Y":
        ans=True
    else:
        ans=False

    to_remove=[]
    for d in database:
        if d[property]!=ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

ans=input("Tu personaje es humano? (Y/N)")
take_chance(ans,"Humano")
if ans=='Y'or ans=='y':
    ans1=1
else:
    ans1=0

ans=input("Tu personaje es un Exo? (Y/N)")
take_chance(ans,"Exo")
if ans=='Y'or ans=='y':
    ans2=1
else:
    ans2=0

ans=input("Tu personaje es un Insomne? (Y/N)")
take_chance(ans,"Insomne")
if ans=='Y'or ans=='y':
    ans3=1
else:
    ans3=0

ans=input("Tu personaje es un Portaluz? (Y/N)")
take_chance(ans,"Portaluz")
if ans=='Y'or ans=='y':
    ans4=1
else:
    ans4=0

ans=input("tu personaje es un cazador? (Y/N)")
take_chance(ans,"Cazador")
if ans=='Y'or ans=='y':
    ans5=1
else:
    ans5=0

ans=input("Tu personaje es un titan? (Y/N)")
take_chance(ans,"Titan")
if ans=='Y'or ans=='y':
    ans6=1
else:
    ans6=0

ans=input("Tu personaje es un hechicero? (Y/N)")
take_chance(ans,"Hechicero")
if ans=='Y'or ans=='y':
    ans7=1
else:
    ans7=0

ans=input("Tu personaje usa armas para combatir? (Y/N)")
take_chance(ans,"Armas")
if ans=='Y'or ans=='y':
    ans8=1
else:
    ans8=0

if len(database)==1:
    print("Tu personaje es "+database[0]["Nombre"])
else:
    print("No logre adivinar tu personaje")
    print('Como se llama el personaje en el que estabas pensando?')
    ans9=input()
    c.execute("INSERT INTO Destiny VALUES (?,?,?,?,?,?,?,?,?)",(ans9,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8))
    conn.commit()

conn.close()