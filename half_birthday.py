import datetime


def half_birthday(year, month, day):
    bday = datetime.datetime(year, month, day)
    half = bday + datetime.timedelta(days=181)
    print(half)
    return(half)


if __name__ == '__main__':
    year = 2003
    month = 2
    day = 20
    half_birthday(year, month, day)
