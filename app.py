from flask import Flask


app = Flask(__name__)
app.json.ensure_ascii = False


about_me = {
    "name": "Вадим",
    "surname": "Шиховцов",
    "email": "vshihovcov@specialist.ru"
}


@app.route("/")
def hello_world() -> dict:
    """Первый эндпоинт для обработки домашней страницы"""
    return {"status": 200, "message": "OK"}


@app.route("/about")
def about() -> dict:
    """Эндпоинт для обработки url-about"""
    return about_me


if __name__ == "__main__":
    app.run(debug=True)
