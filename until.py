#!/usr/bin/env python

import datetime

def getRemainingMonths(value):
    today = datetime.datetime.today()
    if isDateInFuture(value):
        if value.year == today.year:
            return str(value.month - today.month) + " months remaining"
        else:
            return str((value.year-today.year-1)*12 + (12-today.month) + value.month) + " months remaining"
    else:
        print "Date not in future"

#def getRemainingDays(date):

def getDateValue(value):
    try:
        value = datetime.datetime.strptime(str(value), '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect date format, should be dd/mm/YYYY")
    return value


def isDateInFuture(value):    
    return value > datetime.datetime.today()

input = raw_input("Date: ")
date_value = getDateValue(input)
print getRemainingMonths(date_value)