import datetime


def get_birthdays_per_week(users):
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    weekdays = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

    for user in users:
        if user["birthday"].weekday() == 0:
            weekdays[0].append(user["name"])
        elif user["birthday"].weekday() == 1:
            weekdays[1].append(user["name"])
        elif user["birthday"].weekday() == 2:
            weekdays[2].append(user["name"])
        elif user["birthday"].weekday() == 3:
            weekdays[3].append(user["name"])
        elif user["birthday"].weekday() == 4:
            weekdays[4].append(user["name"])
        elif user["birthday"].weekday() == 5:
            weekdays[5].append(user["name"])
        elif user["birthday"].weekday() == 6:
            weekdays[6].append(user["name"])

    for i in range(7):
        if i == 0:
            print("Monday:")
            if weekdays[i]:
                if len(weekdays[i]) == 1:
                    print(weekdays[i][0])
                else:
                    for j in range(len(weekdays[i])):
                        if j == len(weekdays[i]) - 1:
                            print(weekdays[i][j], end="")
                        else:
                            print(weekdays[i][j])


test_list = [
            {'name': 'Bill', 'birthday': datetime.datetime(2020, 8, 3)},
            {'name': 'Jill', 'birthday': datetime.datetime(2020, 8, 7)},
            {'name': 'Kim', 'birthday': datetime.datetime(2020, 8, 8)},
            {'name': 'Jan', 'birthday': datetime.datetime(2020, 8, 10)},
            ]

get_birthdays_per_week(test_list)
