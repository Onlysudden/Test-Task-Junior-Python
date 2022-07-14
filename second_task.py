"""
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
"""

#pip install beautifulsoup4 requests lxml
from bs4 import BeautifulSoup
import requests

def count_animals() -> dict:
    # Вставляем свой юзер-агент
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36"
    }
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    req = requests.get(url, headers=headers)
    flag = True
    # Создаем словарь для хранения количества страниц
    d = {x: 0 for x in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"}
    count = 0

    
    while flag:
        soup = BeautifulSoup(req.text, features="lxml")
        # Парсим страницу и убираем первые две строчки с подкатегориями
        groups = (soup.find_all('div', class_="mw-category-group"))[2:]

        # Парсим заголовки, их количество добавляем в словарь по букве алфавита
        for group in groups:
            letter = group.find("h3").text
            # Цикл остановится когда дойдет до английского алфавита
            if letter == "A":
                flag = False
                break
            d[letter] += len(group.find_all('li'))
        
        count += 1
        print(f"Страниц обработано: {count}")
        # Парсим, создаем ссылку на следующую страницу и делаем запрос новой страницы. Возвращаемся обратно
        link = soup.find("div", id="mw-pages").find("a", text="Следующая страница")
        url = "https://ru.wikipedia.org/" + link.get('href')
        req = requests.get(url, headers=headers)
    return d

if __name__ == '__main__':
    animals = count_animals()
    for i in animals:
        print(i + ":", animals[i])
