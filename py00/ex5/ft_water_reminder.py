#!/usr/bin/env python3

def ft_water_reminder():
    last_watered = input("Enter last time plants were watered: ")
    if int(last_watered) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
