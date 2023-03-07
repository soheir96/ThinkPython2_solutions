'''
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches.
'''

from datetime import datetime, timedelta
import random

def generate_birthdays(group_size):
    jan_first = datetime(2020, 1, 1)
    birthday_list = [(jan_first + timedelta(days=random.randint(0, 366))).strftime("%m/%d/%Y") for i in range(group_size)]
    return sorted(birthday_list)

def has_duplicates(t):
    if len(t) != len(set(t)):
        return True
    else:
        return False

def shared_birthday(group_size):
    birthdays = generate_birthdays(group_size)
    return has_duplicates(birthdays)

def generate_trials(group_size, trials):
    c = 0
    for i in range(trials):
        if shared_birthday(group_size) == True:
            c += 1
    return c / trials

print(generate_trials(23, 100))