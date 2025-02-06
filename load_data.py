# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = ""

# Update "" with your team (e.g. T102)
__team__ = "T097"


#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """Return a list with dictionary elements that shows the other keys/values for each occupation specified for every character

    Precondition: 
    Occupation can only be a string with the values of ["AT", "DB", "EB", "H", "HG", "M", "VF", "WA"]

    Examples:
    >>> character_occupation_list ('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element}, … ]
    >>> character_occupation_list ('characters-mat.csv', 'W')
    []
    >>> character_occupation_list ('characters-mat.csv', Wa)
    [{'Strength': '14', 'Agility': '6', 'Stamina': '2', 'Personality': '8', 'Intelligence': '11', 'Luck': '0.39', 'Armor': '9', 'Weapon': 'short sword'}, {another element}, … ]
    """

    in_file = open(file_name, 'r') #open file
    #read line by line
    general_count = 1
    character = []
    occupation = occupation.lower()
    occupation_column = ""
    for line in in_file: #main loop through lines
        if general_count == 1: #setting a header list
            header = line.strip('\n').split(',')
        else:
            line_list = line.strip('\n').lower().split(',')
            character_line = {} # create new dictionnary every iteration

#Adding resiliency for occupation(String can be changed for what you're looking for) column position

            for item in range(0, len(line_list)):
                if header[item] == "Occupation" and occupation_column == "":
                    occupation_column = item

            for item in range(0, len(line_list)): #loop through the items in line
                if line_list[occupation_column] == occupation and item != occupation_column:
                    try: #setting the dictionnary and the possible values to float
                        character_line[header[item]] = int(line_list[item])
                    except:
                        try:
                            character_line[header[item]] = float(line_list[item])
                        except:
                            character_line[header[item]] = line_list[item].capitalize()

            if character_line != {}: #check for empty dictionnaries
                character.append(character_line) #creating the list of dictionnary
        general_count += 1
    in_file.close()
    return character

#==========================================#
# Place your character_strength_list function after this line
def character_strength_list(file_name: str, strength_range: tuple[int, int]) -> list[dict]:
    """Return a list of characters with strength in the given range from a .csv file.

    Precondition: 
    file_name has to be a .CSV file, .txt file or a valid string 
    strength_range is tuple of two ints >= 0

    Examples:
    >>> character_strength_list('characters-mat.csv', (8, 11))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, ...]
    >>> character_strength_list('characters-mat', (1000, 1001))
    []
    >>> character_strength_list('characters-mat.csv', (9, 9))
    [{'Occupation': 'AT', 'Agility': '9', 'Stamina': '8', 'Personality': '8', 'Intelligence': '15','Luck': '0.72', 'Armor': '10', 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Agility': '9', 'Stamina': '3', 'Personality': '9', 'Intelligence': '15', 'Luck': '0.5', 'Armor': '10', 'Weapon': 'Club'}, ...]
    """

    profiles = []
    file = open(file_name, 'r')
    header = None
    for line in file:
        if header is None:
            header = line.strip().split(',')
            continue
        values = line.strip().split(',')
        for i in range(len(values)):
            if i == 6:
                values[i] = float(values[i])
            elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 7:
                values[i] = int(values[i])
        data = {}
        for i in range(len(header)):
            data[header[i]] = values[i]
        strength = int(data['Strength'])
        if strength_range[0] <= strength <= strength_range[1]:
            character = {}
            for key in data:
                if key != 'Strength':
                    character[key] = data[key]
            profiles.append(character)
    file.close()
    return profiles


#==========================================#
# Place your character_luck_list function after this line
def character_luck_list(file_name: str, luck_value: float) -> list[dict]:
    """Return all the characters as different dictionaries in a list who have a luck number less than the luck_value. The luck entry is omitted from the character's dictionaries.

    Preconditions: 
    file_name has to be a .CSV file, .txt file or a valid string 
    The file_name containts the following headers for the collumns
    ['Occupation', 'Strengh', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Armor', 'Luck', 'Weapon']

    Examples:
    >>> character_luck_list('characters-mat.csv', 0.2)
    [{'Occupation': 'VF', 'Strengh': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14, 'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    >>> character_luck_list('character-mat.csv', 0.05)
    []
    >>> character_luck_list('character-mat.csv',0.30)
    [{'Occupation': 'AT', 'Strengh': 14, 'Agility': 5, 'Stamina': 6, 'Personality': 13, 'Intelligence': 19, 'Armor': 9, 'Weapon': 'Staff'}, {'Occupation': 'DB', 'Strengh': 9, 'Agility': 7, 'Stamina': 7, 'Personality': 11, 'Intelligence': 5, 'Armor': 10, 'Weapon': 'Staff'},
    ...]
    """

    list_characters = []
    head_check = True
    file = open(file_name, "r")
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        if head_check:
            header = line
            head_check = False
        else:
            character = {}
            character[header[0]] = line[0]
            character[header[1]] = int(line[1])
            character[header[2]] = int(line[2])
            character[header[3]] = int(line[3])
            character[header[4]] = int(line[4])
            character[header[5]] = int(line[5])
            character[header[6]] = float(line[6])
            character[header[7]] = int(line[7])
            character[header[8]] = line[8]

            if character.pop(header[6]) < luck_value:
                list_characters += [character]

    file.close()

    return list_characters


#==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(file_name: str, weapon_type: str) -> list[dict]:
    """Return a list containing dicitionaries for every character whos weapon type is matching the specified weapon type.

    Preconditions:
    file_name has to be a .CSV file, .txt file or a valid string 
    has the following columns: ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon']

    Examples:
    >>> character_ocupation_list('characters-mat.csv', 'Dagger') 
    [{'Occupation': 'WA', 'Strength': '11', 'Agility': '10', 'Stamina': '5', 'Personality': '7', 'Intelligence': '6', 'Luck': '0.67', 'Armor': '10'},
    {next item},
    ...]
    >>> character_ocupation_list('characters-mat.csv', 'Staff') 
    [{'Occupation': 'WA', 'Strength': '14', 'Agility': '7', 'Stamina': '8', 'Personality': '8', 'Intelligence': '7', 'Luck': '0.39', 'Armor': '10'},
    {next item},
    ...]
    >>> character_ocupation_list('characters-mat.csv', 'XXXX') 
    []
    """

    characters_list = []
    first_line = True
    with open(file_name, "r") as in_file:  #Opens file with specification to reading the file only.

        for line in in_file:  #Loop through every line in the .csv file.
            line = line.strip("\n").split(",")  #formats each attribute into a list for each line.

            if first_line:  #Checks if we are on first line, if so sets that line as the headers for the dictionary and tables.
                first_line = False
                table_header = line
                continue

            character = {}

            for i in range(len(line)):
                if table_header[i] != 'Weapon':
                    if i == 0 or i == 8:
                        character[table_header[i]] = line[i]
                    elif i == 6:
                        character[table_header[i]] = float(line[i])
                    else:
                        character[table_header[i]] = int(line[i])

            if line[-1] == weapon_type:  #Checks if weapon types matching using index.
                characters_list.append(character)  #Appends character with matching weapon type to character list to be returned.

    return characters_list  #Return list of characters with matching weapon type.


#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, data: tuple[str, any]) -> list[dict]:
    """Return a list of characters (as dictionnaries) whose attribute (first entry in tuple) is either 'Occupation', 'Strength', 'Luck' or 'Weapon' and euqals the specified value (second entry in tuple). The dictionnairies will contain all their attributes except the specified attribute and their respective value.
    If function is called with 'All' as an attribute no modification to the characters' attributes will be made and they will all show up as dictionnairies in the list.
    If wrong input parameter, the function will return an empty string and inform user of error

    Preconditions:
    file_name has to be a .CSV file
    The file_name containts the following headers for the collumns
    ['Occupation', 'Strengh', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Armor', 'Luck', 'Weapon']

    Examples:
    >>> load_data('characters-mat.csv', ('All', 2))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element},
    ...]
    >>> load_data('characters-mat.csv', ('Occupation', 'EB'))
    [{'Strength': 14, 'Agility': 5, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Dart'}, 
    {another element},
    ...]
    >>> load_data('characters-mat.csv', ('Armor', '13'))
    Invalid Value
    []
    """

    if 'All' == data[0]:
        file = open(file_name, 'r')
        list_characters = []
        head_check = True
        for line in file:
            line = line.strip("\n").split(",")      
            if head_check:
                header = line
                head_check = False

            else:
                character = {}
                character[header[0]] = line[0]
                character[header[1]] = int(line[1])
                character[header[2]] = int(line[2])
                character[header[3]] = int(line[3])
                character[header[4]] = int(line[4])
                character[header[5]] = int(line[5])
                character[header[6]] = float(line[6])
                character[header[7]] = int(line[7])
                character[header[8]] = line[8]

                list_characters += [character]

        file.close()
    elif 'Occupation' == data[0]:
        list_characters = character_occupation_list(file_name, data[1])
    elif 'Strength' == data[0]:
        list_characters = character_strength_list(file_name, (data[1], data[1]))
    elif 'Luck' == data[0]:
        list_characters = character_luck_list(file_name, data[1])
    elif 'Weapon' == data[0]:
        list_characters = character_weapon_list(file_name, data[1])
    else:
        print("Invalid Value")
        list_characters = []
    return list_characters 


#==========================================#
# Place your calculate_health function after this line
def calculate_health(character_list: list[dict]) -> list[dict]:
    """Return the list of dictionay that was inputed with the health value calculated added to each dictionary in the list.
    Preconditions: character_list is a list of dictionnaries
    >>> calculate_health([{'Occupation','Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element}, … ])
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff','Health': 78.88}, {another element}, …]
    >>> calculate_health([{'Occupation','Strength': 12, 'Agility': 2, 'Stamina': 8, 'Personality': 5, 'Intelligence': 8, 'Luck': 0.45, 'Armor': 6, 'Weapon': 'Staff'}, {another element}, … ])
    [{'Occupation','Strength': 12, 'Agility': 2, 'Stamina': 8, 'Personality': 5, 'Intelligence': 8, 'Luck': 0.45, 'Armor': 6, 'Weapon': 'Staff','Health': 59.2}, {another element}, …]
    >>> calculate_health([{'Occupation','Strength': 10, 'Agility': 7, 'Stamina': 9, 'Personality': 5, 'Intelligence': 6, 'Luck': 0.88, 'Armor': 9, 'Weapon': 'Staff'}, {another element}, … ])
    [{'Occupation','Strength': 10, 'Agility': 7, 'Stamina': 9, 'Personality': 5, 'Intelligence': 6, 'Luck': 0.88, 'Armor': 9, 'Weapon': 'Staff', 'Health': 108.28}, {another element}, …]
    """

    for character in character_list:
        character['Health'] = (character['Strength'] + character['Agility'] + character['Stamina'] + character['Personality'] + character['Intelligence']) + ((character['Armor'] ** 2) * character['Luck'])

    return character_list


# Do NOT include a main script in your submission


#print(character_weapon_list('characters-mat.csv', 'Dagger'))
#print(character_occupation_list('characters-mat.csv', 'VF'))
#print(character_strength_list('characters-mat.csv', (7, 10)))
#print(character_luck_list('characters-mat.csv', 0.7))
#print(load_data('characters-mat.csv', ('Strength', 10)))
#print(calculate_health([{'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}]))
