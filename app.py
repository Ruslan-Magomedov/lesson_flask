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


@app.get("/quotes")
def get_quotes():
    """Эндпоинт для обработки url-quotes"""
    return quotes


@app.get("/quotes/<int:item_id>")
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


if __name__ == "__main__":
    app.run(debug=True)
