from datetime import date, timedelta

def get_birthdays_per_week(users):
    """
    Повертає словник з іменами користувачів, які святкують день народження в поточному тижні, розподілених за днями тижня.

    Параметри
    ----------
    users : list
        Список словників, які містять імена та дати народження користувачів у форматі datetime.date.

    Повертає
    -------
    dict
        Словник, де ключі - це дні тижня від понеділка до п'ятниці, а значення - це списки імен користувачів,
        які святкують день народження в цей день. Якщо немає користувачів, які святкують день народження в певний день,
        то цей день відсутній у словнику. Дні народження, які припадають на вихідні, переносяться на наступний понеділок.

    Приклади
    --------
    >>> users = [
                {"name": "Alice", "birthday": date(2024, 1, 15)},
                {"name": "Bob", "birthday": date(2024, 1, 16)},
                {"name": "Charlie", "birthday": date(2024, 1, 14)}
                ]
    >>> get_birthdays_per_week(users)
    {'Monday': ['Alice', 'Charlie'], 'Tuesday': ['Bob']}
    """

    today = date.today().strftime('%m-%d')
    yesterday = (date.today()-timedelta(days=1)).strftime('%m-%d')
    b_yesterday = (date.today()-timedelta(days=2)).strftime('%m-%d')
    next_week = (date.today()+timedelta(weeks=1)).strftime('%m-%d')
    current_year = date.today().year
    users_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
           
    for person in users:
        # Визначаємо, в який день тижня буде свято
        day_name = person["birthday"].replace(year = current_year).strftime('%A')
        # В який день тижня буде свято в наступному році 
        new_year_day_name = person["birthday"].replace(year = current_year + 1).strftime('%A')
        # Дата народження у форматі "місяць-день"
        birth = person["birthday"].strftime('%m-%d')

        # Обробляємо понеділки, щоб привітати минулу суботу і неділю
        if date.today().strftime('%A') == "Monday":
            if birth == yesterday or birth == b_yesterday:
                users_dict["Monday"].append(person["name"])
        # Обробляємо стандіртні ситуації
        if today < next_week:
            if today <= birth <next_week:
                if day_name == "Saturday" or day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
                else:
                    users_dict[day_name].append(person["name"])
        # Обробляємо зміну року                                   
        else:
            if today <= birth:
                if day_name == "Saturday" or day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
                else:
                    users_dict[day_name].append(person["name"])
            elif birth < next_week:
                if new_year_day_name == "Saturday" or new_year_day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
                else:
                    users_dict[new_year_day_name].append(person["name"])
    # Видаляємо пусті списки в словнику
    non_empty_dict = {key: value for key, value in users_dict.items() if value}
    return non_empty_dict

