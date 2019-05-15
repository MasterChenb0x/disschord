#!/usr/local/bin/python3

import random

def dice_roll(sides):
    """
    Dice rolling function
    """
    try:
        if sides == 2:
            return "Oh, you mean a coin flip?"
        elif sides % 2 == 0:
            return random.randint(1,sides)
        else:
            return "That's a weird sided die. Let's be realistic."
    except TypeError:
        return "Do you know how dice work?"


