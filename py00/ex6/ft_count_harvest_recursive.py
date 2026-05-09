#!/usr/bin/env python3

def ft_recursive(i: int, day: int):
    if i == day:
        print("Harvest time!")
    else:
        i += 1
        print("Day ", i)
        ft_recursive(i, day)


def ft_count_harvest_recursive():
    try:
        harvest_day = int(input("Enter the day of the harvest: "))
    except ValueError:
        print("Enter valid harvest day")
        return
    ft_recursive(0, int(harvest_day))
