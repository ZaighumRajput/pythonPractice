#!/usr/bin/python3
import datetime as dt

def header(character, lengthOfLines, appName):
    header = character*lengthOfLines + "\n\t" +  appName + "\n" + character*lengthOfLines
    return header 

def get_birthday_from_user():
    BirthdayYear = int(input("What year you born [YYYY]? "))
    BirthdayMonth = int(input("What month were you born [MM]? "))
    BirthdayDay = int(input("What day were you born [DD]? "))
    Birthday = dt.date(BirthdayYear, BirthdayMonth, BirthdayDay)

    return Birthday

def compute_days_between_dates(date1, date2):

    now = dt.datetime.now()
    thisYearDate1 = dt.datetime(now.year,date1.month, date1.day)
    thisYearDate2 = dt.datetime(now.year,date2.month, date2.day)
    return (thisYearDate1 - thisYearDate2).days

def print_birthday_information(Birthday, comparisonDate):
    daysBetween = compute_days_between_dates(Birthday, comparisonDate)

    print("You were born on {}".format(Birthday.strftime("%Y/%m/%d")))
    if (daysBetween >  0):
        print("There are {} days till your birthday".format(daysBetween))
    elif daysBetween < 0:
        print("Your birthday was {} days ago".format(-daysBetween))
    else:
        print("Its your birthday!")


def BirthdayApp():
    print(header("-", 30, "BIRTHDAY APP"))
    birthday = get_birthday_from_user()
    print_birthday_information(birthday, dt.datetime.today())
    



if __name__ == "__main__":
    BirthdayApp()
