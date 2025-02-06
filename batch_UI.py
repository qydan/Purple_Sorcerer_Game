# ECOR 1042 Lab 6 - Template batch UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-097"

#==========================================#
# Place your script for your text_UI after this line
"""
This is the user interface for the project. To interact with this user interface the functions have to be written in a .txt file in this format:
L;characters-test.csv;Occupation;AT where each part of the input is seperated by ';'. Once this file is written, when running this program, specify which file the program should read the inputs from and it will output the entirity of the sequence.
"""

from load_data import *
from sort import *
from curve_fit import *
from histogram import *

data = []
filename = input('Please enter the name of the file where your commands are stored:\n')
cases = open(filename, 'r')
for line in cases:
    command = line.strip().split(';')


    action = command[0].upper()
    if action == 'E':
        break
    else:
        if action =='L':
            file, attribute, = command[1], command[2]
            try:
                value = float(command[3])
            except:
                value = command[3]
            try:
                value_2 = float(command[4])
            except:
                value_2 = 0
            if attribute == 'Strength':
                data = load_data(file, (attribute, (value, value_2)))
            else:
                try:
                    data = calculate_health(load_data(file, (attribute, value)))
                except:
                    data = load_data(file, (attribute, value))
            if data != []:
                print('Data loaded')

        elif data != []:
            #try:
                if action =='S':
                    attribute, order, show = command[1], command[2], command[3].upper(),
                    sorted_ = sort(data, order, attribute)
                    print('Data Sorted')
                    if show == 'Y':
                        print(sorted_)


                elif action =='C':

                    attribute, deg = command[1], int(command[2])
                    print(curve_fit(data, attribute, deg))


                elif action =='H':
                    attribute = command[1]
                    histogram(data, attribute)
                else:
                    print('Invalid command.')
           # except:
                #print('Invalid command.')
        else:
            print('File not loaded. Please, load a file first.')

cases.close()

