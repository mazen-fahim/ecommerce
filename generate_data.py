#! /usr/bin/env python3

from random import choice, choices, randint, uniform

from lorem.text import TextLorem

lorem = TextLorem(wsep=" ", srange=(1, 3))

names = [lorem.sentence() for i in range(100)]
prices = [round(uniform(150.0, 1000.0), 2) for _ in range(100)]
sizes = [choice(["XS", "S", "M", "L", "XL", "XXL"]) for _ in range(100)]
colors = [
    choice(
        [
            "Black",
            "Navy",
            "Charcoal",
            "Gray",
            "Brown",
            "Beige",
            "White",
            "Cream",
            "Maroon",
            "Olive",
            "Midnight Blue",
            "Burgundy",
            "Forest Green",
            "Steel Blue",
            "Tan",
        ]
    )
    for _ in range(100)
]
