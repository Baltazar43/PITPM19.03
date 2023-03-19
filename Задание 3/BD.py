import sqlite3
 
db = sqlite3.connect('mydatabase.db')

cursor = db.cursor()
#Создание таблицы

#cursor.execute("""CREATE TABLE city(
#    street text
#)""")

#Добавление

#cursor.execute("INSERT INTO city VALUES('Lenina')")
#cursor.execute("INSERT INTO city VALUES('Gercena')")
#cursor.execute("INSERT INTO city VALUES('Gagarina')")
#cursor.execute("INSERT INTO city VALUES('Mojaiskaya')")
#cursor.execute("INSERT INTO city VALUES('Pirogova')")



#Удаление

#cursor.execute("DELETE FROM city WHERE rowid = 5")

#Обновление

#cursor.execute("UPDATE city SET street = 'Mayakovskogo' WHERE street ='Lenina' ")

#Вывод
cursor.execute("SELECT * FROM city")

items = cursor.fetchall()

for el in items:
    print(el[0] + "\n")



db.commit()

db.close()
 