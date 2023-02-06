import calendar
import datetime


def get_birthdays_per_week(users):
    # get the current day
    now = datetime.datetime.now()
    # get the day of the week, 0-monday, 1-tuesday
    day_num = now.weekday()
    # create a dictionary to store the list of users per day
    birthdays_by_day = dict()

    # iterate over the users list
    for user in users:
        # calculate the difference in days between the current day and the user's birthday
        difference_in_days = (user['birthday'] - now).days
        # check if the difference is between 0 and 7
        if 0 <= difference_in_days <= 7:
            # get the day number of the user's birthday
            user_day_num = (user['birthday'].weekday() - day_num) % 7
            # extract the name of the user
            user_name = user['name']
            # get the list of users for the user's birthday day
            user_list = birthdays_by_day.get(user_day_num, [])
            # add the name of the user to the list of users on the user's birthday day
            user_list.append(user_name)
            # update the dictionary
            birthdays_by_day[user_day_num] = user_list

    # loop over days
    for day_num, user_list in birthdays_by_day.items():
        # get the day name
        day_name = calendar.day_name[day_num]
        # format and print users
        print('{}: {}'.format(day_name, ', '.join(user_list)))

