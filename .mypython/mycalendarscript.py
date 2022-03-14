#! /usr/bin/python3
#Python Script to display the calendar depending on the user
#flags
import datetime
import argparse
import calendar
from time import strftime, strptime
CURRENT_YEAR = datetime.datetime.now().year
CURRENT_MONTH = datetime.datetime.now().month

def display_current_month(year, month):
    print(calendar.month(year, month))

def display_current_month_plus_next(year , month):
    cur = calendar.month(year , month).split("\n")
    month +=1
    #Chech if month is december
    if month == 13:
        month = 1
        year +=1
    next = calendar.month(year , month).split("\n")
    my_cal = ""
    #the ammoung of letters in the weekdays row
    #since its always the same for all months and 
    #its used for spacing
    buffer = " " * 2
    formating = len(cur[1])
    if len(cur) == len(next):
        for index in range(len(cur)):
            my_cal += cur[index] +" "*(formating-len(cur[index]))+ buffer +next[index] + "\n"
    elif len(cur) < len(next):
        for index in range(len(cur)):
            my_cal += cur[index] +" "*(formating-len(cur[index]))+ buffer +next[index] + "\n"
        for index in range(len(cur) - len(next) , 0):
            my_cal += " " * formating + buffer + next[index] + "\n"
    elif len(cur) > len(next):
        for index in range(len(next)):
            my_cal += cur[index] +" "*(formating-len(cur[index]))+ buffer +next[index] + "\n"
        for index in range(len(next) - len(cur) , 0):
            my_cal +=cur[index] + buffer  +"\n"
    print(my_cal)

def display_current_year(year):
    print(calendar.calendar(year))

def main(args):
    if args.month:
        display_current_month(CURRENT_YEAR , CURRENT_MONTH)
    elif args.next:
        display_current_month_plus_next(CURRENT_YEAR , CURRENT_MONTH)
    elif args.year:
        display_current_year(CURRENT_YEAR)
    else:
        display_current_month(CURRENT_YEAR , CURRENT_MONTH)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program to show calendar in terminal")
    parser.add_argument("-year" ,  action="store_true" , help = "display the whole current year")
    parser.add_argument("-month" , action="store_true" , help = "display the current month (default)")
    parser.add_argument("-next" ,  action="store_true" , help = "display the current month together with the next one")
    args = parser.parse_args()
    main(args)