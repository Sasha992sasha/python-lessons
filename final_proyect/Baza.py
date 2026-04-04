import sqlite3

con = sqlite3.connect("site.db") #тут створюється файл
cursor = con.cursor()

#тут інтересніше
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS site (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL
)
""")

#вище написана функція яка робить таблицю site шоби:
#в кожного обєкта свій id який сам збільшується
#далі url - текст який не може буть пустий


site = [
    ("https://en.wikipedia.org/wiki/Python_(programming_language)",),
    ("https://www.python.org",),
    ("https://docs.python.org/3/",)
]
#список сайтів - такий собі але для тесту вистачить

cursor.executemany("INSERT INTO site (url) VALUES (?)", site) #цей шматок вставляє сайти в таблицю

con.commit() # цей кусок зберігає зміни
con.close() # ну а цей - закриває
