# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:06:29 2023

@author: PaulMoran
"""

# question 11
print ("this program asks the user to enter a number in seconds and it will return the time in hours, minutes, seconds")
time = int(input("Please enter the time in seconds: "))

# get the number of hours i.e. sec // seconds per hour (integer division)
hour = time // 3600

# get remainder of seconds
time %= 3600

# get number of minutes in the remaining seconds
minutes = time //60

# get the remaining number of seconds
time %= 60
seconds = time

print (hour,"hours", minutes,"minutes" , seconds, "seconds")