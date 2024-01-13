from datetime import date, datetime, timedelta




users = [
            {"name": "Bill Gates", "birthday": datetime(1955, 1, 2).date()},
            {"name": "Gate Bills", "birthday": datetime(1956, 1, 3).date()},
            {"name": "Adam Smith", "birthday": datetime(1723, 12, 30).date()},
            {"name": "John Lock", "birthday": datetime(1704, 12, 31).date()},
            {"name": "Jeremy Bentham", "birthday": datetime(1748, 1, 4).date()},
            {"name": "John Dow", "birthday": datetime(1748, 1, 5).date()}
        ]

def get_birthdays_per_week(users):

    today = date.today().strftime('%m-%d')
    yesterday = (date.today()-timedelta(days=1)).strftime('%m-%d')
    b_yesterday = (date.today()-timedelta(days=2)).strftime('%m-%d')
    next_week = (date.today()+timedelta(weeks=1)).strftime('%m-%d')
    current_year = date.today().year

    users_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
       
    for person in users:
        day_name = person["birthday"].replace(year = current_year).strftime('%A')
        new_year_day_name = person["birthday"].replace(year = current_year+1).strftime('%A')
        birth = person["birthday"].strftime('%m-%d')

        # Обробляємо понеділки, щоб привітати минулу суботу і неділю
 
        if date.today().strftime('%A') == "Monday":
            if birth == yesterday or birth == b_yesterday:
                users_dict["Monday"].append(person["name"])

        # Обробляємо стандіртні ситуації

        if today < next_week:
            if today <= birth <next_week:
        # Перекидаємо вікенди на понеділок 
                if day_name == "Saturday" or day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
        # Обробляємо будні дні 
                else:
                    users_dict[day_name].append(person["name"])

        # Події при Новому році                                   
        else:
            # Свято в цьому році
            if today <= birth:
                if day_name == "Saturday" or day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
                else:
                    users_dict[day_name].append(person["name"])
            # Свято в новому році
            elif birth < next_week:
                if new_year_day_name == "Saturday" or new_year_day_name == "Sunday":
                    users_dict["Monday"].append(person["name"])
                else:
                    users_dict[new_year_day_name].append(person["name"])


    non_empty_dict = {key: value for key, value in users_dict.items() if value}
    print (non_empty_dict)
    return (non_empty_dict)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}, {"name": "Bill Gates", "birthday": datetime(1955, 1, 2).date()},
            {"name": "Gate Bills", "birthday": datetime(1956, 1, 15).date()},
            {"name": "Adam Smith", "birthday": datetime(1723, 1, 17).date()},
            {"name": "John Lock", "birthday": datetime(1704, 12, 31).date()},
            {"name": "Jeremy Bentham", "birthday": datetime(1748, 1, 4).date()},
            {"name": "John Dow", "birthday": datetime(1748, 1, 5).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
