from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # визначаємо поточну дату
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    # знаходимо дату понеділка в поточному тижні
    monday = today - timedelta(days=today.weekday())

    # створюємо словник, де ключі - дні тижня, значення - список ім'янинників
    birthdays_per_day = {monday + timedelta(days=i): [] for i in range(7)}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_date = datetime(birthday.year, birthday.month, birthday.day)

        # якщо день народження вже був у цьому році, додаємо користувача до списку
        # відповідного дня тижня
        if birthday_date < today:
            birthday_date = datetime(today.year + 1, birthday.month, birthday.day)
        day_of_week = birthday_date.weekday()
        birthdays_per_day[monday + timedelta(days=day_of_week)].append(name)

    # виводимо список ім'янинників по днях тижня
    for day, names in birthdays_per_day.items():
        if names:
            print(day.strftime('%A') + ': ' + ', '.join(names))


users = [
    {'name': 'Alice', 'birthday': datetime(1990, 2, 24)},
    {'name': 'Bob', 'birthday': datetime(1985, 2, 26)},
    {'name': 'Charlie', 'birthday': datetime(1978, 2, 23)},
    {'name': 'Dave', 'birthday': datetime(2000, 2, 27)},
    {'name': 'Eve', 'birthday': datetime(1995, 2, 22)},
    {'name': 'Frank', 'birthday': datetime(1992, 2, 29)}
]

get_birthdays_per_week(users)
