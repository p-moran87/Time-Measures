# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:21:07 2023

@author: PaulMoran
"""
"This program determines the number of whole days, hours, \
minutes and seconds contained within a given period of time expressed in seconds."

sec = int(input("Enter a number of seconds:\n"))

# number of whole days in that period of seconds
days = sec // (24 * 60 * 60)

# seconds left after pooling the whole days
sec_hours = sec % (24 * 60 * 60)

# number of hours in that period
hours = sec_hours // (60 *60)

# number of seconds left after pooling the days and hours
sec_mins = sec_hours % (60 * 60)

# number of whole minutes left
mins = sec_mins // 60

# number of seconds left after pooling the days, hours, and minutes

sec_left = sec_mins %  (60)

print("{} seconds is equal to: {} days, {} hours, {} minutes, {} seconds.".format(sec,days, hours, mins, sec_left))