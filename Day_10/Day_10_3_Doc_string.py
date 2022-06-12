# Docstring  --> Way of creating documents as we are coding along the way...
# Important it will only be shown if you write it just after the declaration or
# use """ """

def is_leap(year):
    """Returns True if it's a Leap_year else returns False"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    """Returns number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
    if month > 12 and month < 1:
        return "Invalid month"
    elif(is_leap(year) and month == 2):
        return 29
    else:
        return month_days[month - 1]

  

