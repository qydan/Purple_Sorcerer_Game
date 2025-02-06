# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-097"

#==========================================#
# Place your script for your text_UI after this line
from curve_fit import *
from load_data import *
from sort import *
from histogram import *

def load_data_prompt() -> list[dict]:
    """Return list of dictionaries after calling imported load_data function and prompting user for file name, attribute to filter and value to filter.
    
    Precondition: Valid .csv file name entered.
    
    >>> load_data_prompt(loaded_data)
    Please enter the name of the file: <characters-mat.csv>
    Please enter the attribute to use as a filter: <Strength>
    Please enter the value of the attribute: <13>
    Data Loaded
    
    >>> load_data_prompt(loaded_data)
    Please enter the name of the file: <characters-mat.csv>
    Please enter the attribute to use as a filter: <All>
    Data Loaded
    
    >>> load_data_prompt(loaded_data)
    Please enter the name of the file: <xxxx>
    Please enter the attribute to use as a filter: <All>
    File Not Loaded
    """
    
    file_name = input("Please enter the name of the file: ").strip()
    attribute = input("Please enter the attribute to use as a filter: ").strip()

    while attribute not in ['Occupation', 'Strength', 'Luck', 'Weapon', 'All']:
        attribute = input("Invalid Key, please enter the attribute to use as a filter: ").strip()

    if attribute == 'Occupation' or attribute == 'Weapon':
        value = input("Please enter the value of the attribute: ").strip()
        data_loaded = load_data(file_name, (attribute, value))
    elif attribute == "All":
        data_loaded = calculate_health(load_data(file_name, ('All', '')))
    else:
        value = int(input("Please enter the value of the attribute: ").strip())
        data_loaded = load_data(file_name, (attribute, value))

    if data_loaded:
        print("Data Loaded")
        return data_loaded
    else:
        print("File not loaded")


def sort_data_prompt(loaded_data: list[dict]):
    """Print sorted list of dictionaries after prompting user for attribute to sort and sorting order.
    
    Precondition: Data is loaded using load data command before hand, if Health is used to sort, health key must be present in dictionaries.
    
    >>> sort_data_prompt(loaded_data)
    Please enter attibute the you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): <Agility>
    Ascending (A) or Descending (D) order: <A>
    Data Sorted. Do you want to display the data? (Y/N): <N>
    
    >>> load_data_prompt(loaded_data)
    Please enter attibute the you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): <Health>
    Ascending (A) or Descending (D) order: <D>
    Data Sorted. Do you want to display the data? (Y/N): <N>
    
    >>> load_data_prompt(loaded_data)
    Please enter attibute the you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): <Weapon>
    Invalid attribute, Please enter the you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): <Intelligence>
    Ascending (A) or Descending (D) order: <S>
    Invalid order, Ascending (A) or Descending (D) order: <A>
    Data Sorted. Do you want to display the data? (Y/N): <Y>
    [...]
    """
    
    attribute = input("Please enter attibute the you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): ").strip()

    while attribute not in ['Agility', 'Armor', 'Intelligence', 'Health']:
        attribute = input("Invalid attribute, please enter the attribute you want to use for sorting ('Agility', 'Armor', 'Intelligence', 'Health'): ").strip()

    order = input("Ascending (A) or Descending (D) order: ").strip().upper()

    while order not in ['A', 'D']:
        order = input("Invalid order, Ascending (A) or Descending (D) order:").strip().upper()

    display_data = input("Data Sorted. Do you want to display the data? (Y/N): ").strip().upper()
    if display_data == 'Y':
        print(sort(loaded_data, order, attribute))


def curve_fit_prompt(loaded_data: list[dict]):
    """Print polynomial equation for the best fit of health based on loaded data and specifed numerical attribute.
    
    Precondition: Data is loaded using load data command before hand.
    
    >>> curve_data_prompt(loaded_data)
    Please enter the attribute you want to use to find the best fit for Health ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): <Agility>
    Please enter the order of the polynomial to be fitted: <2>
    Equation: y = 0.08814591293291718x^2 + 3.688379859584909x^1 + 69.9243260652074x^0
    
    >>> load_data_prompt()
    Please enter the attribute you want to use to find the best fit for Health ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): <xyz>`
    Invalid attribute, Please enter the attribute you want to use to find the best fit for Health ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): <Agility>
    Please enter the order of the polynomial to be fitted: <2>
    Equation: y = 0.08814591293291718x^2 + 3.688379859584909x^1 + 69.9243260652074x^0
    
    >>> load_data_prompt()
    Please enter the attribute you want to use to find the best fit for Health ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): <Stamina>
    Please enter the order of the polynomial to be fitted: <2>
    Equation: y = -0.0596483242894354x^2 + 1.3625544625659778x^1 + 102.62592301842143x^0
    """
        
    attribute = input("Please enter the attribute you want to use to find the best fit for Health ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): ")

    while attribute not in ['Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina']:
        attribute = input("Invalid attribute, please enter the attribute you want to use for fitting ('Agility', 'Armor', 'Intelligence', 'Luck', 'Strength', 'Personality', 'Stamina'): ").strip()

    polynomial_order = int(input("Please enter the order of the polynomial to be fitted: ").strip())

    print("Equation: " + curve_fit(loaded_data, attribute, polynomial_order))


def histogram_prompt(loaded_data: list[dict]):
    """Displays histogram of loaded data and specifed attribute for plotting.
    
    Precondition: Data is loaded using load data command before hand.
    
    >>> histogram_prompt(loaded_data)
    Please enter the attribute you want to use for plotting ('Occupation', 'Weapon', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina'): <Agility>
    <displays histogram>
    
    >>> histogram_prompt(loaded_data)
    Please enter the attribute you want to use for plotting ('Occupation', 'Weapon', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina'): <xyz>
    Invalid attribute, Please enter the attribute you want to use for plotting ('Occupation', 'Weapon', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina'): <Armor>
    <displays histogram>

    >>> histogram_prompt(loaded_data)
    Please enter the attribute you want to use for plotting ('Occupation', 'Weapon', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina'): <Intelligence>
    <displays histogram>
    """
    attribute = input("Please enter the attribute you want to use for plotting ('Occupation', 'Weapon', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina'): ").strip()

    while attribute not in ['Occupation', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina', 'Weapon']:
        attribute = input("Invalid attribute, please enter the attribute you want to use for plotting ('Occuptation', 'Agility', 'Armor', 'Intelligence', 'Health', 'Luck', 'Strength', 'Personality', 'Stamina', 'Weapon'): ").strip()

    histogram(loaded_data, attribute)


#Main function to run command prompts.
def main():
    initial_prompt = """
The available commands are:
    L)oad Data
    S)ort Data
    C)urve Fit        
    H)istogram
    E)xit
"""
    while True:
        print(initial_prompt)
        command = input("Please type your command: ").lower().strip()
        if command == 'l':
            loaded_data = load_data_prompt()
        elif command == 's':
            try:
                sort_data_prompt(loaded_data)
            except:
                print("File not loaded. Please, load a file first.")
        elif command == 'c':
            try:
                curve_fit_prompt(loaded_data)
            except:
                print("File not loaded. Please, load a file first.")
        elif command == 'h':
            try:
                histogram_prompt(loaded_data)
            except:
                print("File not loaded. Please, load a file first.")
        elif command == 'e':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
