# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-097"

import numpy as np
#==========================================#
# Place your curve_fit function after this line
def curve_fit(characters: list[dict], attribute: str, degree: int) -> str:
    """Return equation of function to fit a polynomial curve to the average health of characters at each level of the giver attribute.

    Examples:
    >>> curve_fit([{'Occupation': 'EB','Strength': 10, 'Agility': 7, 'Stamina': 9, 'Personality': 5, 'Intelligence': 6, 'Luck': 0.88, 'Armor': 9, 'Weapon': 'Staff', 'Health': 108.28}, 
    {'Occupation': 'EB','Strength': 12, 'Agility': 2, 'Stamina': 8, 'Personality': 5, 'Intelligence': 8, 'Luck': 0.45, 'Armor': 6, 'Weapon': 'Staff','Health': 59.2}], 'Strength', 2))
    y = -24.540000000000067x^1 + 353.68000000000086x^0
    >>> curve_fit([{'Occupation': 'EB', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff','Health': 78.88}, 
    {'Occupation': 'W','Strength': 10, 'Agility': 7, 'Stamina': 9, 'Personality': 5, 'Intelligence': 6, 'Luck': 0.88, 'Armor': 9, 'Weapon': 'Staff', 'Health': 108.28}], 'Agility', 3))
    y = 5.879999999999998x^1 + 67.12000000000003x^0
    >>> curve_fit([{'Occupation': 'EB', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff','Health': 78.88}, 
    {'Occupation': 'W','Strength': 10, 'Agility': 7, 'Stamina': 9, 'Personality': 5, 'Intelligence': 6, 'Luck': 0.88, 'Armor': 9, 'Weap on': 'Staff', 'Health': 108.28}, 
    {'Occupation': 'EB','Strength': 12, 'Agility': 2, 'Stamina': 8, 'Personality': 5, 'Intelligence': 8, 'Luck': 0.45, 'Armor': 6, 'Weapon': 'Staff','Health': 59.2}], 'Armor', 3))
    y = 6.520000000000009x^2 + -81.44000000000013x^1 + 313.1200000000006x^0
    """
    
    sums = {}
    average_count = {}
    for character in characters:
        level = character[attribute]
        health = character['Health']
        if level in sums:
            sums[level] += health
            average_count[level] += 1
        else:
            sums[level] = health
            average_count[level] = 1
    averages = []
    for level in sums:
        average = sums[level] / average_count[level]
        averages.append((level, average))
    averages.sort()

    levels = []
    for level, average in averages:
        levels.append(level)

    healths = []
    for level, average in averages:
        healths.append(average)

    degree = min(degree, len(levels) - 1)
    coefficients = np.polyfit(levels, healths, degree)

    equation = "y = "
    for i in range(len(coefficients)):
        power = len(coefficients) - i - 1
        equation += str(coefficients[i]) + "x^" + str(power)
        if i != len(coefficients) - 1:
            equation += " + "

    return equation
