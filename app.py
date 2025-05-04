from flask import Flask, request

from random import choice


app = Flask(__name__)
app.json.ensure_ascii = False


about_me = {
    "name": "Вадим",
    "surname": "Шиховцов",
    "email": "vshihovcov@specialist.ru"
}


quotes = [
    {
    "id": 3,
    "author": "Rick Cook",
    "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
    "id": 5,
    "author": "Waldi Ravens",
    "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
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


@app.get("/quotes")
def get_quotes():
    """Эндпоинт для обработки url-quotes"""
    return quotes


@app.get("/quotes/<int:item_id>")
def get_quotes_byid(item_id: int):
    """Эндпоинт для обработки url-quotes по id"""
    for d in quotes:
        if d["id"] == item_id:
            return d
    return {"status": 404, "message": "Not Found"}


@app.get("/quotes/count")
def get_quotes_count() -> int:
    """Эндпоинт для подсчёта статей url-quotes/count"""
    return {"Колличество статей": len(quotes)}


@app.get("/quotes/random")
def get_quotes_random():
    """Эндпоинт для возврата случайной статьи url-quotes/random"""
    return choice(quotes)


@app.post("/quotes")
def create_quotes():
    """Эндпоинт для создания статьи"""
    pass


if __name__ == "__main__":
    app.run(debug=True)
