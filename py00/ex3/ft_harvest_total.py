#!/usr/bin/env python3

def ft_harvest_total():
    day1 = input("Enter the harvest for day 1: ")
    day2 = input("Enter the harvest for day 2: ")
    day3 = input("Enter the harvest for day 3: ")
    total_harvest = int(day1) + int(day2) + int(day3)
    print("Total harvest: ", total_harvest)
