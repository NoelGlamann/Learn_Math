#!/usr/bin/python3
#Noel Glamann
#Last edit made to file: September 4, 2020

''' This is the first file created to start my project Learn Math.
I will be developing a program with a variety of math files and 
lessons to help users with their most exciting work. '''

#----IMPORTS------------------------------------------------------

import pickle as p
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import BooleanVar

#----CLASSES------------------------------------------------------

class Screen(tk.Frame):
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
    def main():
        Screen.current = 0
        Screen.switch_frame()   
        
#----MAIN---------------------------------------------------------

if __name__ == "__main__":
    
    '''creating a main screen'''
    root = tk.Tk()
    #root.geometry('1000x600')
    root.title("Movie Library NG")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens = []
    
    screens.append(MainMenu())   #MainMenu  =  screens[0]    
    screens.append(Search())     #Search    =  screens[1]
    screens.append(AddEdit())    #AddEdit   =  screens[2]
    screens.append(Remove())     #Remove    =  screens[3]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.mainloop()               