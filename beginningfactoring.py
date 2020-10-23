#!/usr/bin/python3
#Noel Glamann
#Created September 4, 2020
#Edited: Sep. 11, 2020  NG

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
                                  bg = "lightgrey", fg = "black",
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
                                  activebackground = "lightcoral",
                                  activeforeground = "black",
                                 command = self.factoring,
                                 font = ("Courier", "15"))
        self.btn_fact.grid(row = 3, 
                     column = 1, 
                       sticky = "news")     
        
        self.btn_quad = tk.Button(self, text = "Quadratic Equations",
                                  activebackground = "peachpuff",
                                  activeforeground = "black",
                                 command = self.quadratic,
                                 font = ("Courier", "15"))
        self.btn_quad.grid(row = 4, 
                     column = 1, 
                       sticky = "news") 
        
        self.btn_rad = tk.Button(self, text = "Solving Radicals",
                                  activebackground = "palegreen",
                                  activeforeground = "black",
                                 command = self.radicals,
                                 font = ("Courier", "15"))
        self.btn_rad.grid(row = 5, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_tri = tk.Button(self, text = "Rules of Trigonometry",
                                  activebackground = "powderblue",
                                  activeforeground = "black",
                                 command = self.trigonometry,
                                 font = ("Courier", "15"))
        self.btn_tri.grid(row = 6, 
                     column = 1, 
                       sticky = "news")   
        
        
        
        self.btn_lim = tk.Button(self, text = "Understanding Limits",
                                  activebackground = "thistle",
                                  activeforeground = "black",
                                 command = self.limits,
                                 font = ("Courier", "15"))
        self.btn_lim.grid(row = 7, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_ss = tk.Button(self, text = "Study Sets",
                                  activebackground = "pink",
                                  activeforeground = "black",
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
    def radicals(self):
        Screen.current = 3
        Screen.switch_frame()        
    def trigonometry(self):
        Screen.current = 4
        Screen.switch_frame()
    def limits(self):
        Screen.current = 5
        Screen.switch_frame()
    def sets(self):
        Screen.current = 6
        Screen.switch_frame()
            
class FactoringM(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Let's Start Factoring",
                                  fg = "lightcoral",
                             font = ("Times", "36"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news") 
        
        self.lbl_space1 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space1.grid(row = 1, 
                       column = 1, 
                       sticky = "news") 
        
        
        self.btn_poltut = tk.Button(self, text = "Polynomial Tutorials", 
                                    activeforeground="lightcoral",
                                    command = self.polytut,
                                    font = ("Courier New", "15"))
        self.btn_poltut.grid(row = 2,
                          column = 1,
                          sticky = "news")
        self.btn_polprac = tk.Button(self, text = "Polynomial Practice Problems", 
                                    activeforeground="lightcoral",
                                 font = ("Courier New", "15"))
        self.btn_polprac.grid(row = 3,
                          column = 1,
                          sticky = "news")
        self.btn_polquiz = tk.Button(self, text = "Polynomial Factoring Quiz", 
                                    activeforeground="lightcoral",
                                 font = ("Courier New", "15"))
        self.btn_polquiz.grid(row = 4,
                          column = 1,
                          sticky = "news")
        
        
        self.lbl_space2 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space2.grid(row = 5, 
                       column = 1, 
                       sticky = "news")  
        
        
        self.btn_tritut = tk.Button(self, text = "Trinomial Tutorials",
                                    activeforeground="lightcoral", 
                                 font = ("Courier New", "15"))
        self.btn_tritut.grid(row = 6,
                          column = 1,
                          sticky = "news")
        self.btn_triprac = tk.Button(self, text = "Trinomial Practice Problems", 
                                    activeforeground="lightcoral",
                                 font = ("Courier New", "15"))
        self.btn_triprac.grid(row = 7,
                          column = 1,
                          sticky = "news")
        self.btn_triquiz = tk.Button(self, text = "Trinomial Factoring Quiz", 
                                    activeforeground="lightcoral",
                                 font = ("Courier New", "15"))
        self.btn_triquiz.grid(row = 8,
                          column = 1,
                          sticky = "news") 
        
        self.lbl_space3 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space3.grid(row = 9, 
                       column = 1, 
                       sticky = "news")  
        
        
        self.btn_back = tk.Button(self, text = "Main Menu",
                                  command = self.goback,
                                 font = ("Courier New", "15"))
        self.btn_back.grid(row = 10,
                          column = 0)        
        
        #self.grid_columnconfigure(0, weight = 1)
        #self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
    def goback(self): 
        Screen.current = 0
        Screen.switch_frame()  
    def polytut(self):
        Screen.current = 7
        Screen.switch_frame()

class FactoringPolynomialsTutorial(Screen):
    def __init__(self):
        Screen.__init__(self)        
        
class QuadraticM(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Time for Quadratics",
                             font = ("Times", "36"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news")
        
        self.lbl_space1 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space1.grid(row = 1, 
                       column = 1, 
                       sticky = "news")
        
        
        self.btn_qetut = tk.Button(self, text = "Quadratic Equation Tutorials", 
                                 font = ("Courier New", "15"))
        self.btn_qetut.grid(row = 2,
                          column = 1,
                          sticky = "news")
        self.btn_qeprac = tk.Button(self, text = "Quadratic Equation Practice", 
                                 font = ("Courier New", "15"))
        self.btn_qeprac.grid(row = 3,
                          column = 1,
                          sticky = "news")
        self.btn_qequiz = tk.Button(self, text = "Solving Equations Quiz", 
                                 font = ("Courier New", "15"))
        self.btn_qequiz.grid(row = 4,
                          column = 1,
                          sticky = "news") 
        
        
        self.lbl_space2 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space2.grid(row = 5, 
                       column = 1, 
                       sticky = "news")
        
        
        self.btn_gqtut = tk.Button(self, text = "Graphing Quadratics Tutorials", 
                                 font = ("Courier New", "15"))
        self.btn_gqtut.grid(row = 6,
                          column = 1,
                          sticky = "news")
        self.btn_gqprac = tk.Button(self, text = "Quadratic Graph Practice ", 
                                 font = ("Courier New", "15"))
        self.btn_gqprac.grid(row = 7,
                          column = 1,
                          sticky = "news")
        self.btn_gqquiz = tk.Button(self, text = "Graphing Quadratic Equations Quiz", 
                                 font = ("Courier New", "15"))
        self.btn_gqquiz.grid(row = 8,
                          column = 1,
                          sticky = "news") 
        
        
        self.lbl_space3 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space3.grid(row = 9, 
                       column = 1, 
                       sticky = "news")  
        
        
        self.btn_back = tk.Button(self, text = "Main Menu",
                                  command = self.goback,
                                 font = ("Courier New", "15"))
        self.btn_back.grid(row = 10,
                          column = 0)          
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)        
        self.grid_columnconfigure(2, weight = 1)
        
    def goback(self): 
        Screen.current = 0
        Screen.switch_frame()       
        
class RadicalsM(Screen):
    def __init__(self):
        Screen.__init__(self)
        
class TrigonometryM(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Terrific Trig",
                             font = ("Times", "36"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news") 
        self.btn_rttut = tk.Button(self, text = "Learn Right Triangle Trig", 
                                 font = ("Courier New", "15"))
        self.btn_rttut.grid(row = 2,
                          column = 1,
                          sticky = "news")   
        self.btn_rtquiz = tk.Button(self, text = "Right Triangle Quiz", 
                                 font = ("Courier New", "15"))
        self.btn_rtquiz.grid(row = 3,
                          column = 1,
                          sticky = "news") 
        
        self.lbl_space3 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space3.grid(row = 9, 
                       column = 1, 
                       sticky = "news")  
        
        
        self.btn_back = tk.Button(self, text = "Main Menu",
                                  command = self.goback,
                                 font = ("Courier New", "15"))
        self.btn_back.grid(row = 10,
                          column = 0) 
        
    def goback(self): 
        Screen.current = 0
        Screen.switch_frame()     
    
        
class LimitsM(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Learning Limits",
                             font = ("Times", "36"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news") 
        
        
        self.lbl_space1 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space1.grid(row = 1, 
                       column = 1, 
                       sticky = "news") 
        
        
        self.btn_gltut = tk.Button(self, text = "How to Find Limits Graphically", 
                                 font = ("Courier New", "15"))
        self.btn_gltut.grid(row = 2,
                          column = 1,
                          sticky = "news")  
        self.btn_glprac = tk.Button(self, text = "Graphic Limit Practice", 
                                 font = ("Courier New", "15"))
        self.lbl_space = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.btn_glprac.grid(row = 3,
                          column = 1,
                          sticky = "news")  
        
        
        self.lbl_space2 = tk.Label(self, text = " ",
                             font = ("Times", "5"))        
        self.lbl_space2.grid(row =4, 
                       column = 1, 
                       sticky = "news")         
        
        
        self.btn_nltut = tk.Button(self, text = "How to Find Limits Numerically", 
                                 font = ("Courier New", "15"))
        self.btn_nltut.grid(row = 5,
                          column = 1,
                          sticky = "news")  
        self.btn_nlprac = tk.Button(self, text = "Analytical Limit Practice", 
                                 font = ("Courier New", "15"))
        self.btn_nlprac.grid(row = 6,
                          column = 1,
                          sticky = "news") 
        
        
        self.lbl_space3 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space3.grid(row = 7, 
                       column = 1, 
                       sticky = "news")       
        
        
        self.btn_iltut = tk.Button(self, text = "Infinite Limit Tutorial", 
                                 font = ("Courier New", "15"))
        self.btn_iltut.grid(row = 8,
                          column = 1,
                          sticky = "news")  
        self.btn_ilprac = tk.Button(self, text = "Infinite Limit Practice", 
                                 font = ("Courier New", "15"))
        self.btn_ilprac.grid(row = 9,
                          column = 1,
                          sticky = "news")  
        
        
        self.lbl_space4 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space4.grid(row = 10, 
                       column = 1, 
                       sticky = "news") 
        
        
        self.btn_limquiz = tk.Button(self, text = "Finding Limits Quiz", 
                                 font = ("Courier New", "15"))
        self.btn_limquiz.grid(row = 11,
                          column = 1,
                          sticky = "news") 
        
        self.lbl_space3 = tk.Label(self, text = " ",
                             font = ("Times", "5"))
        self.lbl_space3.grid(row = 9, 
                       column = 1, 
                       sticky = "news")  
        
        
        self.btn_back = tk.Button(self, text = "Main Menu",
                                  command = self.goback,
                                 font = ("Courier New", "15"))
        self.btn_back.grid(row = 10,
                          column = 0)    
            
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)   
        
    def goback(self): 
        Screen.current = 0
        Screen.switch_frame()      
        
class StudySetsM(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        

               
        
#----MAIN---------------------------------------------------------

if __name__ == "__main__":
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry('700x500')
    root.title("Movie Library NG")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens = []
    
    screens.append(MainMenu())      #screens[0] = MainMenu  
    #individual option menus
    screens.append(FactoringM())     #screens[1] = FactoringM
    screens.append(QuadraticM())     #screens[2] = QuadraticM
    screens.append(RadicalsM())      #screens[3] = RadicalsM
    screens.append(TrigonometryM())  #screens[4] = TrigonometryM
    screens.append(LimitsM())        #screens[5] = LimitsM
    screens.append(StudySetsM())     #screens[6] = StudySetsM
    #beginning actual functions
    screens.append(FactoringPolynomialsTutorial())     #screens[7] 
    
    
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news")
    screens[6].grid(row = 0, column = 0, sticky = "news")
    screens[7].grid(row = 0, column = 0, sticky = "news")
    
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.mainloop()               