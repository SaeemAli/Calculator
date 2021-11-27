import tkinter
from tkinter import *
import math

num1 = ""
num2 = ""
calculation = ""
complete = False
ans = ""

def first(x):
    global num1
    global num2
    global value
    global value2
    if complete == False:
        num1 = num1 + str(x)
        value = Label(root, text = num1).place(x = 10, y = 20)
    else:
        num2 = num2 + str(x)
        value2 = Label(root, text = num2).place(x = 10, y = 50)

def symbol(sig):
    global complete
    global sign
    global caluclation
    sign = sig
    complete = True
    if sign == "add":
        calculation = "+"
    elif sign == "min":
        calculation = "-"
    elif sign == "mul":
        calculation = "x"
    elif sign == "div":
        calculation = "/"
    calc = Label(root, text = calculation).place(x = 10, y = 35)

def answer(num1, num2):
    if sign == "add":
        ans = float(num1) + float(num2)
    elif sign == "min":
        ans = float(num1) - float(num2)
    elif sign == "mul":
        ans = float(num1) * float(num2)
    elif sign == "div":
        ans = float(num1) / float(num2)
    result = Label(root, text = ans).place(x = 50, y =20)    

def ac():
    global complete
    global num1
    global num2
    global value
    global value2
    global calc
    global result
    complete = False
    num1 = ""
    num2 = ""
    value = Label(root, text = "                      ").place(x = 10, y = 20)
    value2 = Label(root, text = "                     ").place(x = 10, y = 50)
    calc = Label(root, text = "                       ").place(x = 10, y = 35)
    result = Label(root, text = "                                                                                              ").place(x = 50, y = 20)    

root = Tk()
root.geometry("600x600")
root.resizable(0,0)

plus = Button(root, text = "+", font = 'arial 15 bold' ,bg = 'light blue', height = 2, width = 4, command = lambda: symbol("add")).place(x = 50, y = 500)
minus = Button(root, text = "-", font = 'arial 15 bold', bg = 'light blue', height = 2, width = 4, command = lambda: symbol("min")).place(x = 150, y = 500)
multiply = Button(root, text = "x", font = 'arial 15 bold', bg = 'light blue', height = 2, width = 4, command = lambda: symbol("mul")).place(x = 250, y = 500)
divide = Button(root, text = "/", font = 'arial 15 bold', bg = 'light blue', height = 2, width = 4, command = lambda: symbol("div")).place(x = 350, y = 500)
equal = Button(root, text = "=", font = 'arial 15 bold', bg = 'light blue', height = 2, width = 4, command = lambda: answer(num1, num2)).place(x = 450, y = 500)
clear = Button(root, text = "AC", font = 'arial 15 bold', bg = 'light pink', height = 2, width = 4, command = ac).place(x = 50, y = 400)

decimal = Button(root, text = ".", font = 'arial 15 bold', bg = 'light green', height = 1, width = 3, command = lambda: first(".")).place(x = 450, y = 435)
zero = Button(root, text = "0", font = 'arial 15 bold' ,bg = 'light green', height = 1, width = 21, command = lambda: first(0)).place(x = 150, y = 435)
one = Button(root, text = "1", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(1)).place(x = 150, y = 350)
two = Button(root, text = "2", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(2)).place(x = 250, y = 350)
three = Button(root, text = "3", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(3)).place(x = 350, y = 350)
four = Button(root, text = "4", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(4)).place(x = 150, y = 250)
five = Button(root, text = "5", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(5)).place(x = 250, y = 250)
six = Button(root, text = "6", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(6)).place(x = 350, y = 250)
seven = Button(root, text = "7", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(7)).place(x = 150, y = 150)
eight = Button(root, text = "8", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(8)).place(x = 250, y = 150)
nine = Button(root, text = "9", font = 'arial 15 bold' ,bg = 'light green', height = 2, width = 4, command = lambda: first(9)).place(x = 350, y = 150)

root.mainloop()
