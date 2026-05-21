def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    a = seed_type
    b = quantity
    if (unit == "packets"):
        print(f"{a.capitalize()} seeds: {b} packets available")
    elif (unit == "grams"):
        print(f"{a.capitalize()} seeds: {b} grams total")
    elif (unit == "area"):
        print(f"{a.capitalize()} seeds: covers {b} square meters")
    else:
        print("Unknown unit type")
