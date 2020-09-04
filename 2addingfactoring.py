#!/usr/bin/python3
#Noel Glamann
#Last edit made to file: September 4, 2020

''' This is the first file created to start my project Learn Math.
I will be developing a program with a variety of math files and 
lessons to help users with their most exciting work. '''

#----IMPORTS-----------------------------------------------------



#----FUNCTIONS---------------------------------------------------

def Menu():
    print()
    print('''        WELCOME TO 
        LEARN MATH
    ------------------''')
    print()
    print("Let's get studying!")
    print('''
    1. Factoring
    2. Quadratic
    3. Trigonometry
    4. Radicals
    5. Limits
    ''')
    choice = input("What are we studying today (1, 2, 3...) ? ")
    choice = int(choice)
    if choice == 1:
        print('''
        a. Binomials
        b. Trinomials
        ''')
        specified = input("Please specify: ")
        Selection(specified)
    else:
        Selection(choice)
    
def Selection(choice):
    if type(choice) == int:
        
        if choice == 2:
            print("2")
        if choice == 3:
            print("3")
        if choice == 4:
            print("4")
        if choice == 5:
            print("5")
    else:
        if choice == "a":
            BinomialFactoring()
        if choice == "b":
            trinomials()

def BinomialFactoring():
    print("Factoring Binomials:")
    print("--------------------")

#----PROGRAM-----------------------------------------------------

Menu()