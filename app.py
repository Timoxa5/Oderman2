from flask import Flask, render_template

app = Flask(__name__)

# Дані про меню піц
pizza_menu = [
    {"name": "Маргарита", "description": "Томатний соус, моцарела, базилік", "price": "120 грн"},
    {"name": "Пепероні", "description": "Томатний соус, моцарела, пепероні", "price": "150 грн"},
    {"name": "Гавайська", "description": "Томатний соус, моцарела, курка, ананас", "price": "170 грн"},
    {"name": "Чотири сири", "description": "Моцарела, пармезан, горгонзола, едам", "price": "200 грн"}
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", pizzas=pizza_menu)


if __name__ == "__main__":
    app.run(port=5006, debug=True)
