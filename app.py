from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

import finalProj

# FigureCanvasTkAgg: create the library needed for canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import the modules needed for drawing
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sym
plt.style.use('ggplot')

x = sym.Symbol('x')
arr = np.linspace(-2*math.pi, 2*math.pi, 100)

# Initialize and creates the root window
root = Tk()
# Create canvas: rectangular area intended for drawing pictures or other complex layouts
# root: parent window & set width and height
canvas = Canvas(root, width = 800, height = 400)
# Packs canvas
canvas.pack()

# Initial value 
coefficient = 0
trigonometry = None
power = 0
start = 0
n = 0
add_param = 0

# Function to set up the label for each Entry
def setup_label():
    # label1: "Taylor Series Generator"
    label1 = Label(root, text='Taylor Series Generator')
    label1.config(font=('Arial', 20))
    canvas.create_window(400, 50, window=label1)

    # label2: "Coefficient"
    label2 = Label(root, text="Coefficient")
    canvas.create_window(250, 90, window=label2)

    # label3: "Trigonometry"
    label3 = Label(root, text="Trigonometry")
    canvas.create_window(250, 110, window=label3)

    # label4: "Power"
    label4 = Label(root, text="Power")
    canvas.create_window(250, 130, window=label4)

    # label5: "Start"
    label5 = Label(root, text="Start")
    canvas.create_window(250, 150, window=label5)

    # label6: "Number of Polynomials"
    label6 = Label(root, text="Number of Polynomials")
    canvas.create_window(250, 170, window=label6)

    # label7: "Additional Parameter(use +/-)"
    label7 = Label(root, text="Additional Parameter(use +/-)")
    canvas.create_window(250, 190, window=label7)

# Function to get the input from Entry
def get_input():
    # Set variables as global
    global coefficient_input
    global combo_box
    global power_input
    global start_input
    global n_input
    global add_param_input
    global my_label
    global button1
    global button2
    global button3

    global coefficient
    global trigonometry
    global power
    global start
    global n
    global add_param

    # If there is no input in the Entry box
    if len(coefficient_input.get() and power_input.get() and start_input.get() and n_input.get() and add_param_input.get()) == 0:
        # Show a warning message
        messagebox.showwarning("Warning", "Fill in all the required data!")
    # Else,
    else: 
        # Get the input
        coefficient = int(coefficient_input.get())
        trigonometry = str(combo_box.get())
        power = int(power_input.get())
        start = int(start_input.get())
        n = int(n_input.get())
        add_param = int(add_param_input.get())

        # If the coefficient <= 0 and power <=0: show a warning message
        if (coefficient <= 0 or power <= 0):
            messagebox.showwarning("Warning", "Coefficient and power should be bigger than 0!")
        # Else,
        else:
            # If the inputted power equals to 1
            if power == 1:
                # If add_param is positive number
                if add_param >=0: 
                    # Set the label "+", because add_param int is ignoring the + sign
                    my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "x" + ")" + "+" + str(add_param)
                                    , font=('Arial', 12, "bold"))
                    # Packs my_label
                    my_label.pack()
                    # Put label on the canvas
                    canvas.create_window(400, 220, window=my_label)
                    # Set the state of button1 as disabled, button2 as normal, button3 as disabled
                    button1['state'] = DISABLED
                    button2['state'] = NORMAL
                    button3['state'] = DISABLED
                else:
                    # Set the label
                    my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "x" + ")" + str(add_param)
                                    , font=('Arial', 12, "bold"))
                    # Packs my_label
                    my_label.pack()
                    # Put label on the canvas
                    canvas.create_window(400, 220, window=my_label)
                    # Set the state of button1 as disabled, button2 as normal, button3 as disabled
                    button1['state'] = DISABLED
                    button2['state'] = NORMAL
                    button3['state'] = DISABLED
            else:
                # If add_param is positive number
                if add_param >= 0:
                    # Set the label "+", because add_param int is ignoring the + sign
                    my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "x**" + str(power) + ")" + "+" + str(add_param)
                                    , font=('Arial', 12, "bold"))
                    # Packs my_label               
                    my_label.pack()   
                    # Put label on the canvas             
                    canvas.create_window(400, 220, window=my_label)
                    # Set the state of button1 as disabled, button2 as normal, button3 as disabled
                    button1['state'] = DISABLED
                    button2['state'] = NORMAL
                    button3['state'] = DISABLED
                else:
                    # Set the label
                    my_label = Label(root, text="f(x) = " + trigonometry + "(" + str(coefficient) + "x**" + str(power) + ")" + str(add_param)
                                    , font=('Arial', 12, "bold"))
                    # Packs my_label  
                    my_label.pack()         
                    # Put label on the canvas        
                    canvas.create_window(400, 220, window=my_label) 
                    # Set the state of button1 as disabled, button2 as normal, button3 as disabled
                    button1['state'] = DISABLED 
                    button2['state'] = NORMAL
                    button3['state'] = DISABLED    

# Function to create the function
def check_taylor(coef, trigo, power, add_param):
    global x

    if(trigo == "sin"):
        tay = sym.sin(coef*x**power) + add_param
    elif(trigo == "cos"):
        tay = sym.cos(coef*x**power) + add_param
    elif(trigo == "tan"):
        tay = sym.tan(coef*x**power) + add_param
    elif(trigo == "cosec"):
        tay = 1/sym.sin(coef*x**power) + add_param
    elif(trigo == "sec"):
        tay = 1/sym.cos(coef*x**power) + add_param
    elif(trigo == "cot"):
        tay = 1/sym.tan(coef*x**power) + add_param
    elif(trigo == "arcsin"):
        tay = sym.asin(coef*x**power) + add_param
    elif(trigo == "arccos"):
        tay = sym.acos(coef*x**power) + add_param
    else:
        tay = sym.atan(coef*x**power) + add_param   
    return tay                                

# Function to create the graph
def plot_taylor(tay, arr, start, n, add_param):
    global x
    global graph

    # Call the function created in finalProj.py and find the taylor series of the inputted trigonometric function
    tayl = finalProj.taylor(tay, arr, start, n)
    # Get a lambda function from the trigonometric function inputted
    y = sym.lambdify(x, tay)

    # Set figure and subplot
    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot(111)
    # If the inputted power equals to 1
    if power == 1:
        # If add_param is positive number
        if add_param >=0: 
            # Set to this title 
            ax.set_title(f"f(x) = {trigonometry}({coefficient}x)+{add_param}")
        # Else,
        else:
            # Set to this title 
            ax.set_title(f"f(x) = {trigonometry}({coefficient}x){add_param}")
    # Else,
    else:
        # If add_param is positive number
        if add_param >=0: 
            # Set to this title 
            ax.set_title(f"f(x) = {trigonometry}({coefficient}$x^{power}$)+{add_param}")
        # Else,
        else:
            # Set to this title 
            ax.set_title(f"f(x) = {trigonometry}({coefficient}$x^{power}$){add_param}")

    # Plot the data
    ax.plot(arr, y(arr), label="Original")
    ax.plot(arr, tayl, label="Taylor")
    ax.set_ylim([add_param - 2, add_param + 2])

    # A tk.DrawingArea
    graph = FigureCanvasTkAgg(fig, root) 
    # Graph can fill in the parent widget entirely
    graph.get_tk_widget().pack(fill=BOTH, expand=0)

# Function to show graph
def show_graph():  
    # Show the graph of the corresponding taylor series of the inputted trigonometric function
    plot_taylor(check_taylor(coefficient, trigonometry, power, add_param), arr, start, n, add_param)
    # Set button2 state to disabled and button3 state to normal
    button2['state'] = DISABLED
    button3['state'] = NORMAL

# Function to clear the inputted data, label of the entry, and graph
def clear_all():
    global coefficient
    global trigonometry
    global power
    global start
    global n
    global add_param
    global my_label
    global button1
    global button2
    global button3

    # Destroy label and delete all the entry text
    my_label.destroy()
    coefficient_input.delete(0, END)
    power_input.delete(0, END)
    start_input.delete(0, END)
    n_input.delete(0, END)
    add_param_input.delete(0, END)
    # Hide graph
    graph.get_tk_widget().pack_forget()
    
    # Set the variables again to its initial value
    coefficient = 0
    trigonometry = None
    power = 0
    start = 0
    n = 0
    add_param = 0
    # Set the button1 state to normal, button2 and button3 to disabled
    button1['state'] = NORMAL
    button2['state'] = DISABLED
    button3['state'] = DISABLED


# Create entry box for coefficient input
coefficient_input = Entry(root)
canvas.create_window(400, 90, window= coefficient_input)

# Create combo box of choices
choices_variable = StringVar(root)
user_choices = ("sin", "cos", "tan", "cosec", "sec", "cot", "arcsin", "arccos", "arctan")
choices_variable.set(user_choices[0])

combo_box = Combobox(root, textvariable=choices_variable, values=user_choices)
canvas.create_window(400, 110, window=combo_box)

# Creta entry box for power input
power_input = Entry(root)
canvas.create_window(400, 130, window=power_input)

# Creta entry box for start input
start_input = Entry(root)
canvas.create_window(400, 150, window=start_input)

# Creta entry box for n input
n_input = Entry(root)
canvas.create_window(400, 170, window=n_input)

# Creta entry box for additional parameter input
add_param_input = Entry(root)
canvas.create_window(400, 190, window=add_param_input)

# Create button "Submit" and onClick to function get_input
button1 = Button(root, text="  Submit  ", command=get_input, bg='#ff996e', fg='white', font=('Arial', 11, 'bold'), activebackground="#ffd97a")
canvas.create_window(400, 260, window=button1)

# Create button "Show Graph" and onClick to function show_graph
button2 = Button(root, text="  Show Graph  ", command=show_graph, 
                    bg='#b280f2', font=('Arial', 11, 'bold'), fg='white', activebackground="#f071a3"
                )
canvas.create_window(400, 300, window=button2)

# Create button "Clear" and onClick to function clear_all
button3 = Button(root, text="  Clear  ", command=clear_all, bg='#6d71ed', font=('Arial', 11, 'bold'), fg='white', activebackground="#5ed6ba")
canvas.create_window(400, 340, window=button3)

# Set the initial state of button2 and button3 to disabled
button2['state'] = DISABLED
button3['state'] = DISABLED

# Call the setup_label() function
setup_label()
# Create the window's title
root.title("Taylor Series")
# Run the application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()