#!/usr/bin/env python3

def ft_plant_age():
    age = input("Enter plant's age: ")
    if int(age) < 61:
        print("Plant needs more time to grow...")
    else:
        print("Plant is ready to harvest!")
