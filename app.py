from flask import Flask, request
import sqlite3

from random import choice
from pathlib import Path


BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / "store.db"
KEYS = ('id', 'author', 'text')

app = Flask(__name__)
app.json.ensure_ascii = False

<<<<<<< HEAD
about_me = {
    "name": "Вадим",
    "surname": "Шиховцов",
    "email": "vshihovcov@specialist.ru"
}

quotes = [
    {
        "id": 3,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей "
                "и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока "
                "вселенная побеждает."
    },
    {
        "id": 5,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми "
                "бритвами в руках."
    },
    {
        "id": 6,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
        "id": 8,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. На практике это не так."
    },
]


@app.get("/")
def hello_world() -> dict:
    """Первый эндпоинт для обработки домашней страницы"""
    return {"status": 200, "message": "OK"}


@app.get("/about")
def get_about() -> dict:
    """Эндпоинт для обработки url-about"""
    return about_me

=======
>>>>>>> c3dc204 (add DB)

@app.get("/quotes")
def get_quotes():
    """Первая ручка для получения всех статей"""
    select_quotes = "SELECT * from quotes"
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select_quotes)
    quotes_db = cursor.fetchall()
    cursor.close()
    connection.close()
    # Подготовка данных для отправки в правильной формате.
    # Необходимо выполнить преобразование:
    # list[tuple] -> list[dict]
    quotes = []
    for quote_db in quotes_db:
        quote = dict(zip(KEYS, quote_db))
        quotes.append(quote)
    return quotes, 200


@app.get("/quotes/<int:item_id>")
<<<<<<< HEAD
def get_quotes_by_id(item_id):
    """Эндпоинт для обработки url-quotes по id"""
    for d in quotes:
        if d["id"] == item_id:
            return d
    return {"status": 404, "message": "Not Found"}


@app.get("/quotes/count")
def get_quotes_count():
    """Эндпоинт для подсчёта статей url-quotes/count"""
    return {"Количество статей": len(quotes)}


@app.get("/quotes/random")
def get_quotes_random():
    """Эндпоинт для возврата случайной статьи url-quotes/random"""
    return choice(quotes)


@app.post("/quotes")
def create_quotes():
    """Эндпоинт для создания статьи"""
    data = request.json
    if "author" in list(data.keys()) and "text" in list(data.keys()):
        data["id"] = quotes[-1]["id"] + 1
        quotes.append(data)
        return data, 200
    return {"message": "Bad Data"}, 400


@app.put("/quotes/<int:item_id>")
def change_quotes(item_id):
    """Эндпоинт для создания статьи"""
    data = request.json
    for i in range(len(quotes)):
        if quotes[i]["id"] == item_id:
            if "author" in list(data.keys()):
                quotes[i]["author"] = data["author"]
            if "text" in list(data.keys()):
                quotes[i]["text"] = data["text"]
            return {"message": "OK"}, 200
    return {"message": "Not Found"}, 404


@app.delete("/quotes/<int:item_id>")
def delete_quotes(item_id):
    for i in range(len(quotes)):
        if quotes[i]["id"] == item_id:
            quotes.pop(i)
            return {"message": f"Quotes with id {item_id} is deleted"}, 200
    return {"message": "Not Found"}, 404
=======
def get_quotes_byid(item_id: int):
    """Ручка для обработки url-quotes по id"""
    select_quotes = f"SELECT * from quotes where id={item_id}" 
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select_quotes)
    quotes_db = cursor.fetchone()
    cursor.close()
    connection.close()
    # Подготовка данных для отправки в правильной формате.
    # Необходимо выполнить преобразование:
    # list[tuple] -> list[dict]
    result = {"id": quotes_db[0], "author": quotes_db[1], "text": quotes_db[2],}
    return result, 200


@app.post("/quotes")
def create_quote():
    """Ручка для создания статьи"""
    data = request.json
    select_quotes = f"""
    INSERT INTO quotes (author, text) VALUES
    ("{data["author"]}", "{data["text"]}")
    """
    print(f"{select_quotes}")
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select_quotes)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "OK"}, 201


@app.put("/quotes/<int:item_id>")
def edit_quote(item_id: int):
    data = request.json
    if set(data.keys()) - set(KEYS[1:]):
        return {"message": "Bad Request"}, 400
    select_quotes = f"""
    UPDATE quotes SET author="{data["author"]}", text="{data["text"]}"
    WHERE id={item_id}
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select_quotes)
    connection.commit()
    responce = cursor.fetchone()
    cursor.close()
    connection.close()
    return {"message": "OK"}, 201


@app.delete("/quotes/<int:item_id>")
def delete_quote(item_id: int):
    select_quotes = f"DELETE FROM quotes WHERE id={item_id}"
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select_quotes)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "OK"}, 201
>>>>>>> c3dc204 (add DB)


if __name__ == "__main__":
    app.run(debug=True)
