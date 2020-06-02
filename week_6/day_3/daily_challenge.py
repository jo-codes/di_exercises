import datetime
from datetime import date
# do you normally have to import like this? Pylint threw some errors otherwise

bday = input("Please provide your birthday in MM/DD/YYYY format ")


def roman_numeral(num):
    num = int(num)
    switch = {
        0: "X",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }
    return switch.get(num)


def print_cake(age):

    last_digit = list(age).pop()
    age = roman_numeral(last_digit)

    print(f"   _____{age}______")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")


def calculate_age(bday):
    today = date.today()
    month, day, year = map(int, bday.split("/"))
    born = datetime.date(year, month, day)

    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))

    leaps = []
    index_year = 1900

    while index_year < 3000:
        # This will only work for the next 1080 years...
        if index_year % 4 == 0 and (index_year % 100 != 0 or index_year % 400 == 0):
            leaps.append(index_year)
        index_year += 1

    leaps = set(leaps)

    if year in leaps:
        print_cake(f"{age}")
        print_cake(f"{age}")
    else:
        print_cake(f"{age}")


calculate_age(bday)
