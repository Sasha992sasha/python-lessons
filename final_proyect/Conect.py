import sqlite3 #це для бази даних
import requests # це для підключення до сайтів
from bs4 import BeautifulSoup # це для очищення інформації з сайтів від мусору тегів і так далі

def page(url): #це підключення
    conect = requests.get(url) 
    sup = BeautifulSoup(conect.text , "html.parser")
    return sup.get_text().lower() # цей шматок дістаєж тільки текст маленькими буквами

def clean(text): # тут текст чиститься від мусору він заміняється на пробіли а ну й розбивається на слова
    for i in ".,!&?;:'\"-_":
        text = text.replace(i , " ")
    return text.lower().split() 

def search(query): #основна функція
    con = sqlite3.connect("site.db") #підключення до бази данних
    cursor = con.cursor() 
    
    cursor.execute("SELECT url FROM site") #тут я беру всі url 
    urls = [row[0] for row in cursor.fetchall()] # тут перетворюю на список
    
    con.close() # ну й закриваю базу
    
    query_words = clean(query) # чистка від мусору і розбиття на слова
    
    result = []
    
    for url in urls: # перебираю сайти
        text = page(url) #скачую весь текст сторінки
        words = clean(text) 
        
        score = 0 # рейтинг сайту
        
        for q_word in query_words: #перебираю слова з запиту
            score+= words.count(q_word) # а тут рахую сіки разів зустрічається слово
    
        result.append((url , score)) 
            
    result.sort(key=lambda x: x[1], reverse=True) # тут сортую список з сайтами
        
    return result 
    
def run(query): # тут функція запуску
    result = search(query) 
    print('Результати:') # заголовок
    for url , score in result:
        print(f"{score} - {url}") # виводжу всі результати
    
run(input('Шо шукаєм ')) # ну а це запуск всього коду




"""
над фінальним проєктом - я старався 
мені наприкад пайтон - дуже інтересна тема тому я стараюся в ній розвиваться
на всякий напишу
Автор : Батуревич Олександр
"""
