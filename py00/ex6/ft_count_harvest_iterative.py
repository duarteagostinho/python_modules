#!/usr/bin/env python3

def ft_count_harvest_iterative():
    harvest_day = input("Enter the day of the harvest: ")
    if int(harvest_day) < 1:
        print("Enter valid harvest day")
    else:
        for i in range(1, int(harvest_day) + 1):
            print("Day ", i)
        print("Harvest time!")
