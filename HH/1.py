def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return year % 4 == 0
    else:
        return leap


print(is_leap(2100))
