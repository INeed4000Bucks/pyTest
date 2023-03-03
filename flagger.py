from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

weekend = Weekday.SATURDAY | Weekday.SUNDAY
print(weekend)

chores_for_ethan = {
    'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
    'answer SO\s questions': Weekday.SATURDAY,
    }
def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print("On " + day.name + " I " + chore)
show_chores(chores_for_ethan, Weekday.MONDAY)
show_chores(chores_for_ethan, Weekday.TUESDAY)
show_chores(chores_for_ethan, Weekday.WEDNESDAY)
