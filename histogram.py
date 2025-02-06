# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Peter Abou Mrad"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297408"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-097"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt
import numpy

def histogram(List: list[dict], attribute: str) -> int:
    """Return a histogram of number of attribute found in a list of dictionaries, it will then return the largest value found for a numeric key or -1 for a word key.

    Preconditions: attributes are part of the existing attributes for the csv file and List is a list of dictionaries

    >>> histogram([{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'W', 'Agility': 9, 'Stamina': 3, 'Personality': 9,'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}], 'Occupation')
    (return a histogram)
    -1
    >>> histogram([{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'W', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}], 'Intelligence')
    (return a histogram)
    15
    >>> histogram([{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'W', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}], 'Luck')
    (return a histogram)
    0.72
    """

    #create a dictionary with the number of times every value apprears
    attribute_dictionary = {}
    for dictionary in List:
        attr = dictionary[attribute]
        if attr in attribute_dictionary:
            attribute_dictionary[attr] += 1
        else:
            attribute_dictionary[attr] = 1

    #Set variables
    key_max = max(attribute_dictionary.keys())
    key_list = list(attribute_dictionary.keys())
    value_list = list(attribute_dictionary.values())

    #Check if numeric value
    if type(attr) == float or type(attr) == int:
        returned = key_max

        #Create a dictionnary with 20 keys and all values as 0
        bins_dictionary = {}
        bins = numpy.linspace(0, key_max, 20)
        for element in range(len(bins)):
            bins_dictionary[bins[element]] = 0

        #Enter the correct value of repetion for bins_dictionary
        for element in range(len(key_list)):
            for i in range(1, 20):
                if bins[i - 1] < key_list[element] <= bins[i]:
                    bins_dictionary[bins[i]] += value_list[element]

        #Set variables
        x_list = list(bins_dictionary.keys())
        y_list = list(bins_dictionary.values())

    else: #if string value return -1
        returned = -1
        x_list = key_list
        y_list = value_list

    #Make a histogram
    plt.figure()
    plt.title('Character Attribute Histogram')
    plt.xlabel(attribute)
    plt.ylabel('Count')
    plt.bar(x_list, y_list)
    plt.show()

    return returned


# Do NOT include a main script in your submission
