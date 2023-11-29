from datetime import datetime
from collections import defaultdict

users = [{"name": "Bill Gates", "birthday": datetime(1955, 11, 29)}, 
         {"name": "Some Guy", "birthday": datetime(1989, 12, 2)},
         {"name": "Harry Potter", "birthday": datetime(1991, 12, 4)},
         {"name": "Joe Biden", "birthday": datetime(1945, 11, 30)}]

# Have no idea how lambda works to be honest but I didn't find any simpler way to sort it without braking any logic or changing the way how this was intended to be solved)
def sort_lines_by_weekdays(lines):
    weekday_order = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5}
    lines = lines.split('\n')
    sorted_lines = sorted(lines, key=lambda line: weekday_order.get(line.split(':')[0], float('inf')))
    result = '\n'.join(sorted_lines)
    return result



def get_birthdays_per_week(users):
    next_week_birthdays = defaultdict(list)
    next_week_birthdays_string = ''
    current_date = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year+1)
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            if birthday_this_year.weekday() == 1:
                next_week_birthdays['Tuesday'].append(name)
            elif birthday_this_year.weekday() == 2:
                next_week_birthdays['Wednesday'].append(name)
            elif birthday_this_year.weekday() == 3:
                next_week_birthdays['Thursday'].append(name)
            elif birthday_this_year.weekday() == 4:
                next_week_birthdays['Friday'].append(name)
            else:
                next_week_birthdays['Monday'].append(name)
    for weekday in next_week_birthdays:
        next_week_birthdays_string += f'{weekday}: {", ".join(next_week_birthdays[weekday])}\n'
    next_week_birthdays_string = sort_lines_by_weekdays(next_week_birthdays_string.strip())
    if next_week_birthdays_string == '':
        print('Sorry, no birthdays this week')
    print(next_week_birthdays_string)


get_birthdays_per_week(users)
