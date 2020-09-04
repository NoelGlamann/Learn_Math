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
        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "LEARN MATH",
                             font = ("Times", "40"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news")  
        
        self.lbl_intro = tk.Label(self, text = "Study Topics:",
                             font = ("Times", "20"))
        self.lbl_intro.grid(row = 2, 
                       column = 0,
                       columnspan = 3,                       
                       sticky = "news")
        
        self.btn_fact = tk.Button(self, text = "Factoring Nomials",
                                 command = self.factoring,
                                 font = ("Courier", "15"))
        self.btn_fact.grid(row = 3, 
                     column = 1, 
                       sticky = "news")     
        
        self.btn_quad = tk.Button(self, text = "Quadratic Equations",
                                 command = self.quadratic,
                                 font = ("Courier", "15"))
        self.btn_quad.grid(row = 4, 
                     column = 1, 
                       sticky = "news") 
        
        self.btn_tri = tk.Button(self, text = "Rules of Trigonometry",
                                 command = self.trigonometry,
                                 font = ("Courier", "15"))
        self.btn_tri.grid(row = 5, 
                     column = 1, 
                       sticky = "news")   
        
        self.btn_rad = tk.Button(self, text = "Solving Radicals",
                                 command = self.radicals,
                                 font = ("Courier", "15"))
        self.btn_rad.grid(row = 6, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_lim = tk.Button(self, text = "Understanding Limits",
                                 command = self.limits,
                                 font = ("Courier", "15"))
        self.btn_lim.grid(row = 7, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_ss = tk.Button(self, text = "Study Sets",
                                 command = self.sets,
                                 font = ("Courier", "15"))
        self.btn_ss.grid(row = 9, 
                     column = 1, 
                       sticky = "news")        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(1, weight = 2)
        self.grid_rowconfigure(8, weight = 1)
        self.grid_rowconfigure(10, weight = 2)
        
        
    def factoring(self):
        Screen.current = 1
        Screen.switch_frame()
    def quadratic(self):
        Screen.current = 2
        Screen.switch_frame()
    def trigonometry(self):
        Screen.current = 3
        Screen.switch_frame()
    def radicals(self):
        Screen.current = 4
        Screen.switch_frame()
    def limits(self):
        Screen.current = 5
        Screen.switch_frame()
    def sets(self):
        Screen.current = 6
        Screen.switch_frame()
            
class Factoring(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class Quadratic(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class Trigonometry(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class Radicals(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class Limits(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class StudySets(Screen):
    def __init__(self):
        Screen.__init__(self)
        
#----MAIN---------------------------------------------------------

if __name__ == "__main__":
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry('800x600')
    root.title("Movie Library NG")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens = []
    
    screens.append(MainMenu())      #screens[0] = MainMenu  
    screens.append(Factoring())     #screens[1] = Factoring 
    screens.append(Quadratic())     #screens[2] = Quadratic
    screens.append(Trigonometry())  #screens[3] = Trigonometry 
    screens.append(Radicals())      #screens[4] = Radicals
    screens.append(Limits())        #screens[5] = Limits
    screens.append(StudySets())     #screens[6] = StudySets
    
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news")
    screens[6].grid(row = 0, column = 0, sticky = "news")
    
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.mainloop()               