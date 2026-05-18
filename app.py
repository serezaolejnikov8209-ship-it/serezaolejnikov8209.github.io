from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Данные музеев
museums = [
    {
        "name": "Государственный исторический музей",
        "hours": "Ежедневно: 10:00 - 18:00",
        "price": "400 руб.",
        "website": "http://ghm.ru",
        "location": [55.7542, 37.6173]
    },
    {
        "name": "Пушкинский музей",
        "hours": "Ежедневно: 10:00 - 21:00",
        "price": "500 руб.",
        "website": "http://pushkinmuseum.art",
        "location": [55.7493, 37.5983]
    },
    {
        "name": "Музей современного искусства 'Гараж'",
        "hours": "Ср-Вс: 11:00 - 22:00",
        "price": "750 руб.",
        "website": "https://garagemca.org",
        "location": [55.7402, 37.5862],
        "description": "Первый в России музей, посвященный современному искусству и культуре."
    },
    {
        "name": "Музей-заповедник 'Царицыно'",
        "hours": "Ежедневно: 10:00 - 18:00",
        "price": "300 руб.",
        "website": "http://museum-tsaritsyno.ru",
        "location": [55.6006, 37.6081],
        "description": "Крупный историко-культурный комплекс, включающий парк и архитектурные памятники."
    },
    {
        "name": "Государственный музей изобразительных искусств имени А.С. Пушкина",
        "hours": "Чт-Пн: 10:00 - 18:00, Вт: 11:00 - 21:00",
        "price": "500 руб.",
        "website": "https://www.arts-museum.ru",
        "location": [55.7490, 37.5982],
        "description": "Крупнейший музей в Москве, в котором хранится более 700 тысяч произведений искусства."
    },
    {
        "name": "Московский планетарий",
        "hours": "Ср-Пн: 10:00 - 19:00, Вт: выходной",
        "price": "600 руб.",
        "website": "https://planetarium.moscow",
        "location": [55.7754, 37.6285],
        "description": "Один из крупнейших планетариев в Европе, с современными научными выставками."
    },
    {
        "name": "Музей Победы",
        "hours": "Ежедневно: 10:00 - 20:00",
        "price": "400 руб.",
        "website": "http://www.museum.ru",
        "location": [55.7490, 37.5494],
        "description": "Музей, посвященный истории Второй мировой войны и подвигу советского народа."
    },
    {
        "name": "Всероссийский музей декоративного искусства",
        "hours": "Вт-Вс: 10:00 - 18:00, Пн: выходной",
        "price": "250 руб.",
        "website": "https://www.vmdpni.ru",
        "location": [55.7550, 37.6019],
        "description": "Использует музейные коллекции, чтобы показать богатство российской художественной традиции."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/museums")
def get_museums():
    return jsonify(museums)

if __name__ == "__main__":
    app.run(debug=True)