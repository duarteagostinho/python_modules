#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    units = {
    	"packets": "available",
        "grams": "total",
        "area": "square meters"
    }
    if unit == "packets" or unit == "grams":
        print(seed_type, "seeds:", quantity, unit, units[unit])
    elif unit == "area":
        print(seed_type, "seeds: covers", quantity, units[unit])
    else:
        print("Unknown unit type")
    