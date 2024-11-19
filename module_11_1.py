import requests


def demonstrate_requests():
    print("\n=== Демонстрация requests ===")

    response = requests.get("https://api.github.com/repos/python/cpython")

    print(f"1. Статус код запроса: {response.status_code}")
    print(f"2. Тип контента: {response.headers['content-type']}")

    data = response.json()

    print(
        f"3. Информация о репозитории:\n"
        f"   - Название: {data['name']}\n"
        f"   - Звезд: {data['stargazers_count']}\n"
        f"   - Описание: {data['description']}"





# Выводы:
# - Requests
# Эта библиотека позволила нам легко и удобно отправлять HTTP-запросы, обрабатывать параметры,
# заголовки и анализировать ответы. Использование requests расширяет стандартные возможности
# Python для взаимодействия с сетью, упрощая работу с API и загрузку данных.
