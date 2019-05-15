#!/usr/local/bin/python3

import random

def dice_roll(sides):
    """
    Dice rolling function
    """
    try:
        if sides == 2:
            return f"Oh, you mean a coin flip? {coin_flip()} I guess"
        elif sides % 2 == 0:
            return random.randint(1,sides)
        else:
            return "That's a weird sided die. Let's be realistic."
    except TypeError:
        return "Do you know how dice work?"

def coin_flip():
    """
    Flips a coin
    """
    flip = random.randint(1,2)
    if flip == 1:
        return "Heads"
    elif flip == 2:
        return "Tails"


