# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = ""

# Update "" with your team (e.g. T102)
__team__ = "T-097"

#from load_data import *

#==========================================#
# Place your sort_characters_agility_bubble function after this line
def sort_characters_agility_bubble(characters: list[dict], order: str) -> list[dict]:
    """Return sorted list of characters based on their agility using bubble sort algorithm and sepcified order.
    
    Precodittions: characters = list[dict] and order = str
    
    Examples:
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    >>> sort_characters_agility_bubble([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Agility" key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D")
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]
    """

    if order.upper() != "A" and order.upper() != "D":
        return 

    for dict in range(len(characters)):
        if 'Agility' not in characters[dict].keys():
            print("\"Agility\" key not present")
            return characters

    #bubble sorting algorithm
    for i in range(len(characters)):
        for j in range(0, len(characters)-i-1):
            if (order.upper() == 'A' and characters[j]["Agility"] > characters[j+1]["Agility"]) or (order.upper() == 'D' and characters[j]["Agility"] < characters[j+1]["Agility"]):
                characters[j], characters[j+1] = characters[j+1], characters[j]

    return characters


#==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(List: list[dict], order: str) -> list[dict]:
    """Return a list of dictionaries that are sorted in ascending or descending order based on the value of the key 'Intelligence'.

    Preconditions: List is a list of dictionaries, order is a string that is either 'A' or 'B'

    >>> sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 9}, {'Occupation': 'H','Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB','Intelligence': 9}]
    >>> sort_characters_intelligence_selection([{'Occupation':'EB'}, {'Occupation': 'M'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 2}, {'Occupation': 'EB','Intelligence': 1},{'Occupation': 'EB','Intelligence': 4},{'Occupation': 'EB','Intelligence': 3},{'Occupation': 'EB','Intelligence': 7},{'Occupation': 'EB','Intelligence': 10},{'Occupation': 'EB','Intelligence': 5},{'Occupation': 'EB','Intelligence': 9}], "A")
    [{'Occupation': 'EB','Intelligence': 1}, {'Occupation': 'EB','Intelligence': 2},{'Occupation': 'EB','Intelligence': 3},{'Occupation': 'EB','Intelligence': 4},{'Occupation': 'EB','Intelligence': 5},{'Occupation': 'EB','Intelligence': 7},{'Occupation': 'EB','Intelligence': 9},{'Occupation': 'EB','Intelligence': 10}]
    """

    if order.upper() != "A" and order.upper() != "D":
        return 

    for dict in range(len(List)):
        if 'Intelligence' not in List[dict].keys():
            print('\"Intelligence\" key is not present')
            return List

    #Selection Sorting Algorithm
    for i in range(len(List)):
        index = i

        for j in range(i + 1, len(List)):
            if List[index]['Intelligence'] > List[j]['Intelligence'] and order.upper() == "A":
                index = j 

            elif List[index]['Intelligence'] < List[j]['Intelligence'] and order.upper() == "D":
                index = j 

        (List[i], List[index]) = (List[index], List[i])

    return List


#==========================================#
# Place your sort_characters_health_insertion function after this line
def sort_characters_health_insertion(character_list: list[dict], order: str) -> list[dict]:
    """Return sorted list of dictionaries based on specified order (ascending or descending) and value of key 'Health'.

    Preconditions: second parameter must be 'A' or 'D' and dictionaries must contain 'Health' key.

    Examples:
    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]
    >>> sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Health" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    >>> sort_characters_healht_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'H', 'Health': 62.74}], "D")
    [{'Occupation': 'H', 'Health': 62.74}, {'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'EB', 'Health': 62.37}]
    """

    if order.upper() != 'A' and order.upper() != 'D':
        return
    
    #check if health key is present in the dictionaries provided
    for dict in range (len(character_list)):
        if 'Health' not in character_list[dict].keys():
            print("\"Health\" key is not present")
            return character_list

    #insertion sort algorithm
    for i in range(1, len(character_list)):
        key = character_list[i]
        j = i - 1
        while j >= 0 and ((order.upper() == 'A' and key["Health"] < character_list[j]["Health"]) or (order.upper() == 'D' and key["Health"] > character_list[j]["Health"])):
            character_list[j + 1] = character_list[j]
            j -= 1
        character_list[j + 1] = key
    
    return character_list


#==========================================#
# Place your sort_characters_armor_bubble function after this line
def sort_characters_armor_bubble(characters: list[dict], order: str) -> list[dict]:
    """Return an ordered list of dictionnairies based on the armor key in the dictionairy. It will sort the dictionnairies in the list based on Ascending order ('A') or Descending order ('D'). If the key 'Armor' is not present in the dictionnairy the function will print an error message and return the inputed function

    Preconditions:
    order is either 'A' or 'D' for ascending or descending respectively
    The dictionnairies in characters have a 'Armor' key

    >>> sort_characters_armor_bubble([{'Strength': 12, 'Armor': 15}, {'Strength': 7, 'Armor': 12}, {'Strength': 14, 'Armor': 17}], 'A')
    [{'Strength': 7, 'Armor': 12}, {'Strength': 12, 'Armor': 15}, {'Strength': 14, 'Armor': 17}]

    >>> sort_characters_armor_bubble([{'Strength': 12, 'Armor': 15},{'Strength': 7, 'Armor': 12}, {'Strength': 14, 'Armor': 17}], 'D')
    [{'Strength': 14, 'Armor': 17}, {'Strength': 12, 'Armor': 15}, {'Strength': 7, 'Armor': 12}]

    >>> sort_characters_armor_bubble([{'Strength': 12, 'Agility': 15},{'Strength': 7, 'Agility': 12}, {'Strength': 14, 'Agility': 17}], 'A')
    "Armor" key is not present.
    [{'Strength': 12, 'Agility': 15},{'Strength': 7, 'Agility': 12}, {'Strength': 14, 'Agility': 17}]
    """
    
    # determine if armor is a key in the dictionnaires
    try:
        #determine wheter to order in acscending or decsending order
        swap = True

        if order == 'A':
            while swap == True:
                swap = False
                for i in range(len(characters)-1):
                    if characters[i]['Armor'] > characters[i+1]['Armor']:
                        characters[i], characters[i+1] = characters[i+1], characters[i]
                        swap = True

        elif order == 'D':
            while swap == True:
                swap = False
                for i in range(len(characters)-1):
                    if characters[i]['Armor'] < characters[i+1]['Armor']:
                        characters[i], characters[i+1] = characters[i+1], characters[i]
                        swap = True            
    except:
        print('\"Armor\" key is not present.')

    return characters


#==========================================#
# Place your sort function after this line
def sort(characters: list[dict], order: str, key: str) -> list[dict]:
    """Return an ordered list of dictionaries based on specified order and specified key.

    Preconditions: order is either 'A' or 'D', specified key must be in accepted key values.
    
    >>> sort([{'Strength': 12, 'Armor': 15}, {'Strength': 7, 'Armor': 12}, {'Strength': 14, 'Armor': 17}], 'A', 'Armor')
    [{'Strength': 7, 'Armor': 12}, {'Strength': 12, 'Armor': 15}, {'Strength': 14, 'Armor': 17}]
    >>> sort([{'Strength': 12, 'Armor': 15}, {'Strength': 7, 'Armor': 12}, {'Strength': 14, 'Armor': 17}], 'A', 'Strength')
    Cannot be sorted by "Strength".
    [{'Strength': 12, 'Armor': 15}, {'Strength': 7, 'Armor': 12}, {'Strength': 14, 'Armor': 17}]
    >>> sort([{'Occupation':'EB'}, {'Occupation': 'M'}], 'A', 'Health')
    "Health" key is not present
    [{'Occupation':'EB'}, {'Occupation': 'M'}]
    """

    accepted = ['Agility', 'Intelligence', 'Health', 'Armor']
    if key not in accepted:
        print("Cannot be sorted by \"" + key + '\".')
        return characters
    
    else:
        if key == accepted[0]:
            return sort_characters_agility_bubble(characters, order)
        if key == accepted[1]:
            return sort_characters_intelligence_selection(characters, order)
        if key == accepted[2]:
            return sort_characters_health_insertion(characters, order)
        else:
            return sort_characters_armor_bubble(characters, order)


# Do NOT include a main script in your submission

#print (sort(load_data('characters-test.csv', ('All', '')), 'A', 'Agility'))
#print (sort(load_data('characters-test.csv', ('All', '')), 'A', 'Armor'))
#print (sort(calculate_health(load_data('characters-test.csv', ('All', ''))), 'A', 'Health'))
#print (sort(load_data('characters-test.csv', ('All', '')), 'A', 'Intelligence'))
