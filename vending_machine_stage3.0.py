import random

from tkinter import *
import tkinter.messagebox

from PIL import ImageTk, Image

''' Variables '''
# Generic variables used during various calculations.
initial_choice = 0
drink_input_number = 0
continue_choice = "yes"
drink_choice = 0
total_paid = 0
total_returned = 0
total_due = 0

# Money Input
bill_20 = 0
bill_10 = 0
bill_5 = 0
bill_1 = 0
coin_100 = 0
coin_50 = 0
coin_25 = 0
coin_10 = 0
coin_5 = 0
coin_1 = 0

# Money Output
bill_20r = 0
bill_10r = 0
bill_5r = 0
bill_1r = 0
coin_100r = 0
coin_50r = 0
coin_25r = 0
coin_10r = 0
coin_5r = 0
coin_1r = 0

# Stock
stock_coca_cola = random.randint(1,100)
stock_mountain_dew = random.randint(1,100)
stock_pepsi = random.randint(1,100)
stock_sprite = random.randint(1,100)
stock_dr_pepper = random.randint(1,100)

stock_d_coca_cola = random.randint(1,100)
stock_d_mountain_dew = random.randint(1,100)
stock_d_pepsi = random.randint(1,100)
stock_d_sprite = random.randint(1,100)
stock_d_dr_pepper = random.randint(1,100)

## Lists ##
stock = [stock_coca_cola, stock_mountain_dew, stock_pepsi, stock_sprite, stock_dr_pepper, stock_d_coca_cola, stock_d_mountain_dew, stock_d_pepsi, stock_d_sprite, stock_d_dr_pepper]

## Functions ##
def opening_question(value):
    global initial_choice
    initial_choice = value
    print(value)
    print(initial_choice)
    win1.destroy()

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def drink_choice_f(value):
    global drink_choice
    drink_choice = value
    print(drink_choice)
    drink_choice_label2 = Label(win3, text="You Selected: " + str(drink_choice), height=2)
    drink_choice_label2.grid(row=18, column=0, columnspan=2)

def drink_input_number_f():
    global drink_input_number
    drink_input_number = drink_input_number_entry.get()
    print(drink_input_number)
    drink_input_number_label2 = Label(win3, text="You want " + str(drink_input_number) + " sodas today.")
    drink_input_number_label2.grid(row=19, column=0, columnspan=2)
    stock_update()

def exit_screen_3():
    if not drink_choice == 0:
        win3.destroy()

def total_due():
    global drink_input_number
    total_due = int(drink_input_number)*1.50

def total_paid_f():
    global bill_20
    global bill_10
    global bill_5
    global bill_1
    global coin_100
    global coin_50
    global coin_25
    global coin_10
    global coin_5
    global coin_1
    global total_paid

    bill_20 = int(bill_20_entry.get())
    bill_10 = int(bill_10_entry.get())
    bill_5 = int(bill_5_entry.get())
    bill_1 = int(bill_1_entry.get())
    coin_100 = int(coin_100_entry.get())
    coin_50 = int(coin_50_entry.get())
    coin_25 = int(coin_25_entry.get())
    coin_10 = int(coin_10_entry.get())
    coin_5 = int(coin_5_entry.get())
    coin_1 = int(coin_1_entry.get())

    total_paid = round(float(20*bill_20 + 10*bill_10 + 5*bill_5 + bill_1 + coin_100 + 0.5*coin_50 + 0.25*coin_25 + 0.1*coin_10 + 0.05*coin_5 + 0.01*coin_1),2)
    print("Total Payment: " + str(total_paid))

    total_paid_label = Label(win4, text="Total Paid: " + str(total_paid), height=2)
    total_paid_label.grid(row=17, column=0, columnspan=2)

def exit_screen_4():
    win4.destroy()

def exit_screen_5():
    win5.destroy()

def continue_choice_f(value):
    global continue_choice
    continue_choice = value
    print(continue_choice)
    win6.destroy()

def stock_update():
    global drink_input_number
    global drink_choice

    global stock_coca_cola
    global stock_mountain_dew
    global stock_pepsi
    global stock_sprite
    global stock_dr_pepper

    global stock_d_coca_cola
    global stock_d_mountain_dew
    global stock_d_pepsi
    global stock_d_sprite
    global stock_d_dr_pepper

    if drink_choice == "Coca-Cola":
        stock[0] = stock[0] - int(drink_input_number)
        print(stock[0])
    elif drink_choice == "Mountain Dew":
        stock[1] = stock[1] - int(drink_input_number)
    elif drink_choice == "Pepsi":
        stock[2] = stock[2] - int(drink_input_number)
    elif drink_choice == "Sprite":
        stock[3] = stock[3] - int(drink_input_number)
    elif drink_choice == "Dr. Pepper":
        stock[4] = stock[4] - int(drink_input_number)
    elif drink_choice == "Diet Coke":
        stock[5] = stock[5] - int(drink_input_number)
    elif drink_choice == "Diet Mountain Dew":
        stock[6] = stock[6] - int(drink_input_number)
    elif drink_choice == "Diet Pepsi":
        stock[7] = stock[7] - int(drink_input_number)
    elif drink_choice == "Sprite Zero":
        stock[8] = stock[8] - int(drink_input_number)
    elif drink_choice == "Diet Dr. Pepper":
        stock[9] = stock[9] - int(drink_input_number)

'''The main program starts here with the initial question.'''
## Initial Question ##

win1 = Tk()
# win1.geometry("500x300")
win1.title("Vending Machine")

welcome = Label(win1, text = "Welcome to Matt's Vending!", bg = "blue", fg = "white", font = ('Arial', 30))
welcome.grid(row=0, column=0, columnspan=2)
initial_choice_label = Label(win1, text = "Would you like a cold soda today?", bg = "green", fg = "white", font = ('Arial', 20))
initial_choice_label.grid(row=1, column=0, columnspan=2)

button_yes = Button(text="Yes", command= lambda: opening_question("yes"))
button_yes.grid(row=2, column=0)

button_no = Button(text="no", command= lambda: opening_question("no"))
button_no.grid(row=2, column=1)

print(initial_choice)

win1.mainloop()

## Initial Question Response ##
win2 = Tk()

if initial_choice == "no":
    good_day = Label(win2, text = "Alrighty then, have a good day!", font=('Arial',20))
    good_day.grid(row=0, column=0)
    button_exit = Button(win2, text = "Exit Program", command=exit)
    button_exit.grid(row=1, column=0)
else:
    text1 = Label(win2, text="Let's get you a soda!", font=('Arial',20))
    text1.grid(row=0, column=0)
    button_next = Button(win2, text="Next", command=win2.destroy)
    button_next.grid(row=1, column=0)

win2.mainloop()

''' Time to choose a drink '''
while continue_choice == "yes":
    win3 = Tk()
    win3.title("What to Drink?")

    drink_choice_label = Label(win3, text="What would you like to drink?", height=5)
    drink_choice_label.grid(row=0,column=0, columnspan=2)

    # Regular Soda Buttons #
    button_coca_cola = Button(win3, text="Coca-Cola", width=20, height=2, command= lambda: drink_choice_f("Coca-Cola"))
    button_coca_cola.grid(row=1, column=0)

    button_mountain_dew = Button(win3, text="Mountain Dew", width=20, height=2, command= lambda: drink_choice_f("Mountain Dew"))
    button_mountain_dew.grid(row=1, column=1)

    button_pepsi = Button(win3, text="Pepsi", width=20, height=2, command= lambda: drink_choice_f("Pepsi"))
    button_pepsi.grid(row=2, column=0)

    button_sprite = Button(win3, text="Sprite", width=20, height=2, command= lambda: drink_choice_f("Sprite"))
    button_sprite.grid(row=2, column=1)

    button_dr_pepper = Button(win3, text="Dr. Pepper", width=20, height=2, command= lambda: drink_choice_f("Dr. Pepper"))
    button_dr_pepper.grid(row=3, column=0, columnspan=2)

    # Diet Soda Buttons #
    button_d_coca_cola = Button(win3, text="Diet Coke", width=20, height=2, command= lambda: drink_choice_f("Diet Coke"))
    button_d_coca_cola.grid(row=4, column=0)

    button_d_mountain_dew = Button(win3, text="Diet Mountain Dew", width=20, height=2, command= lambda: drink_choice_f("Diet Mountain Dew"))
    button_d_mountain_dew.grid(row=4, column=1)

    button_d_pepsi = Button(win3, text="Diet Pepsi", width=20, height=2, command= lambda: drink_choice_f("Diet Pepsi"))
    button_d_pepsi.grid(row=5, column=0)

    button_d_sprite = Button(win3, text="Sprite Zero", width=20, height=2, command= lambda: drink_choice_f("Sprite Zero"))
    button_d_sprite.grid(row=5, column=1)

    button_d_dr_pepper = Button(win3, text="Diet Dr. Pepper", width=20, height=2, command= lambda: drink_choice_f("Diet Dr. Pepper"))
    button_d_dr_pepper.grid(row=6, column=0, columnspan=2)

    # Current Stock of Soda #
    current_stock_label = Label(win3, text="The current stock of all products are listed below:", height=2)
    current_stock_label.grid(row=7, column=0, columnspan=2)

    stock_coca_cola_label = Label(win3, text="Coca-Cola: " + str(stock[0]), width=20, height=2)
    stock_mountain_dew_label = Label(win3, text="Mountain Dew: " + str(stock[1]), width=20, height=2)
    stock_pepsi_label = Label(win3, text="Pepsi: " + str(stock[2]), width=20, height=2)
    stock_sprite_label = Label(win3, text="Sprite: " + str(stock[3]), width=20, height=2)
    stock_dr_pepper_label = Label(win3, text="Dr. Pepper: " + str(stock[4]), height=2)

    stock_coca_cola_label.grid(row=8, column=0)
    stock_mountain_dew_label.grid(row=8, column=1)
    stock_pepsi_label.grid(row=9, column=0)
    stock_sprite_label.grid(row=9, column=1)
    stock_dr_pepper_label.grid(row=10, column=0, columnspan=2)

    stock_d_coca_cola_label = Label(win3, text="Diet Coke: " + str(stock[5]), width=20, height=2)
    stock_d_mountain_dew_label = Label(win3, text="Diet Mountain Dew: " + str(stock[6]), width=20, height=2)
    stock_d_pepsi_label = Label(win3, text="Diet Pepsi: " + str(stock[7]), width=20, height=2)
    stock_d_sprite_label = Label(win3, text="Sprite Zero: " + str(stock[8]), width=20, height=2)
    stock_d_dr_pepper_label = Label(win3, text="Diet Dr. Pepper: " + str(stock[9]), width=20, height=2)

    stock_d_coca_cola_label.grid(row=11, column=0)
    stock_d_mountain_dew_label.grid(row=11, column=1)
    stock_d_pepsi_label.grid(row=12, column=0)
    stock_d_sprite_label.grid(row=12, column=1)
    stock_d_dr_pepper_label.grid(row=13, column=0, columnspan=2)

    drink_input_number_label = Label(win3, text="How many would you like? Please Enter an integer only.", height = 2)
    drink_input_number_label.grid(row=14, column=0, columnspan=2)
    drink_input_number_entry = Entry(win3, width=20)
    drink_input_number_entry.grid(row=15, column=0, columnspan=2, pady=2)

    drink_input_number_button = Button(win3, text="Enter Soda Value", height=2, command=drink_input_number_f)
    drink_input_number_button.grid(row=16, column=0, columnspan=2)

    next_button = Button(win3, text="Next", height=2, command=exit_screen_3)
    next_button.grid(row=17, column=0, columnspan=2)

    win3.mainloop()

    ''' How will you pay? '''
    win4 = Tk()
    win4.title("How will you pay today?")

    how_will_you_pay_label = Label(win4, text="How will you be paying today?")
    how_will_you_pay_label.grid(row=0, column=0, columnspan=2)
    what_bills_label1 = Label(win4, text="Put the number of each bill and coin you will be using today, below.")
    what_bills_label1.grid(row=1, column=0, columnspan=2)
    what_bills_label2 = Label(win4, text="Please use integer values only.")
    what_bills_label2.grid(row=2, column=0, columnspan=2)

    # Bills
    bills_label = Label(win4, text="Bills")
    bills_label.grid(row=3, column=0, columnspan=2)

    bill_20_label = Label(win4, text="$20", height=3, width=20)
    bill_10_label = Label(win4, text="$10", height=3, width=20)
    bill_5_label = Label(win4, text="$5", height=3, width=20)
    bill_1_label = Label(win4, text="$1", height=3, width=20)

    bill_20_label.grid(row=4, column=0)
    bill_10_label.grid(row=5, column=0)
    bill_5_label.grid(row=6, column=0)
    bill_1_label.grid(row=7, column=0)

    bill_20_entry = Entry(win4, width=20)
    bill_10_entry = Entry(win4, width=20)
    bill_5_entry = Entry(win4, width=20)
    bill_1_entry = Entry(win4, width=20)

    bill_20_entry.grid(row=4, column=1)
    bill_10_entry.grid(row=5, column=1)
    bill_5_entry.grid(row=6, column=1)
    bill_1_entry.grid(row=7, column=1)

    bill_20_entry.insert(0, "0")
    bill_10_entry.insert(0, "0")
    bill_5_entry.insert(0, "0")
    bill_1_entry.insert(0, "0")

    # Coins
    coins_label = Label(win4, text="Coins")
    coins_label.grid(row=8, column=0, columnspan=2)

    coin_100_label = Label(win4, text = "$1", height=3, width=20)
    coin_50_label = Label(win4, text = "$0.50", height=3, width=20)
    coin_25_label = Label(win4, text = "$0.25", height=3, width=20)
    coin_10_label = Label(win4, text = "$0.10", height=3, width=20)
    coin_5_label = Label(win4, text = "$0.05", height=3, width=20)
    coin_1_label = Label(win4, text = "$0.01", height=3, width=20)

    coin_100_label.grid(row=9, column=0)
    coin_50_label.grid(row=10, column=0)
    coin_25_label.grid(row=11, column=0)
    coin_10_label.grid(row=12, column=0)
    coin_5_label.grid(row=13, column=0)
    coin_1_label.grid(row=14, column=0)

    coin_100_entry = Entry(win4, width=20)
    coin_50_entry = Entry(win4,  width=20)
    coin_25_entry = Entry(win4, width=20)
    coin_10_entry = Entry(win4, width=20)
    coin_5_entry = Entry(win4, width=20)
    coin_1_entry = Entry(win4, width=20)

    coin_100_entry.grid(row=9, column=1)
    coin_50_entry.grid(row=10, column=1)
    coin_25_entry.grid(row=11, column=1)
    coin_10_entry.grid(row=12, column=1)
    coin_5_entry.grid(row=13, column=1)
    coin_1_entry.grid(row=14, column=1)

    coin_100_entry.insert(0, "0")
    coin_50_entry.insert(0, "0")
    coin_25_entry.insert(0, "0")
    coin_10_entry.insert(0, "0")
    coin_5_entry.insert(0, "0")
    coin_1_entry.insert(0, "0")

    total_due_label = Label(win4, text="You owe " + str(int(drink_input_number)*1.50) + "0" + " today.", height=2)
    total_due_label.grid(row=15, column=0, columnspan=2)

    enter_money_button = Button(win4, text="Check Payment", height=2, width=20, command=total_paid_f)
    enter_money_button.grid(row=16, column=0, columnspan=2)

    next_button = Button(win4, text="Next", height=2, width=20, command=exit_screen_4)
    next_button.grid(row=18, column=0, columnspan=2)

    win4.mainloop()

    ''' Making Change '''

    win5 = Tk()
    win5.title("Your Change")

    # Displaying Important Information

    total_paid_label = Label(win5, text="You paid: " + str(total_paid))
    total_paid_label.grid(row=0, column=0, columnspan=2)

    total_due = str(int(drink_input_number)*1.50)

    total_due_label2 = Label(win5, text="You owe: " + str(total_due))
    total_due_label2.grid(row=1, column=0, columnspan=2)

    total_returned = float(total_paid) - float(total_due)

    total_returned_label = Label(win5, text="You will be returned: " + str(total_returned))
    total_returned_label.grid(row=2, column=0, columnspan=2)

    # Determining Change in Fewest Bills

    while total_returned >= 0.01:
        if total_returned >= 20:
            temp_total = round(total_returned % 20, 2)
            bill_20r = round((total_returned - temp_total) / 20, 0)
            total_returned = temp_total
        elif total_returned >= 10:
            temp_total = round(total_returned % 10, 2)
            bill_10r = round((total_returned - temp_total) / 10, 0)
            total_returned = temp_total
        elif total_returned >= 5:
            temp_total = round(total_returned % 5, 2)
            bill_5r = round((total_returned - temp_total) / 5, 0)
            total_returned = temp_total
        elif total_returned >= 1:
            temp_total = round(total_returned % 1, 2)
            bill_1r = round((total_returned - temp_total) / 1, 0)
            total_returned = temp_total
        elif total_returned >= 0.5:
            temp_total = round(total_returned % 0.5, 2)
            coin_50r = round((total_returned - temp_total) / 0.5, 0)
            total_returned = temp_total
        elif total_returned >= 0.25:
            temp_total = round(total_returned % 0.25, 2)
            coin_25r = round((total_returned - temp_total) / 0.25, 0)
            total_returned = temp_total
        elif total_returned >= 0.1:
            temp_total = round(total_returned % 0.1, 2)
            coin_10r = round((total_returned - temp_total) / 0.1, 0)
            total_returned = temp_total
        elif total_returned >= 0.05:
            temp_total = round(total_returned % 0.05, 2)
            coin_5r = round((total_returned - temp_total) / 0.05, 0)
            total_returned = temp_total
        else:
            coin_1r = round(total_returned / 0.01, 2)
            total_returned = total_returned - total_returned

    # Displaying Change

    bill_20r_label = Label(win5, text=str(int(bill_20r)) + " $20 bills")
    bill_20r_label.grid(row=3, column=0, columnspan=2)

    bill_10r_label = Label(win5, text=str(int(bill_10r)) + " $10 bills")
    bill_10r_label.grid(row=4, column=0, columnspan=2)

    bill_5r_label = Label(win5, text=str(int(bill_5r)) + " $5 bills")
    bill_5r_label.grid(row=5, column=0, columnspan=2)

    bill_1r_label = Label(win5, text=str(int(bill_1r)) + " $1 bills")
    bill_1r_label.grid(row=6, column=0, columnspan=2)

    coin_50r_label = Label(win5, text=str(int(coin_50r)) + " 50-cent pieces")
    coin_50r_label.grid(row=7, column=0, columnspan=2)

    coin_25r_label = Label(win5, text=str(int(coin_25r)) + " quarters")
    coin_25r_label.grid(row=8, column=0, columnspan=2)

    coin_10r_label = Label(win5, text=str(int(coin_10r)) + " dimes")
    coin_10r_label.grid(row=9, column=0, columnspan=2)

    coin_5r_label = Label(win5, text=str(int(coin_5r)) + " nickels")
    coin_5r_label.grid(row=10, column=0, columnspan=2)

    coin_1r_label = Label(win5, text=str(int(coin_1r)) + " pennies")
    coin_1r_label.grid(row=11, column=0, columnspan=2)

    next_button = Button(win5, text="Next", height=2, width=20, command=exit_screen_5)
    next_button.grid(row=12, column=0, columnspan=2)

    win5.mainloop()

    '''Continuing your soda choice?'''
    win6 = Tk()
    win6.title("Continuing?")

    continue_choice_label = Label(win6, text="Would you like any more soda today?")
    continue_choice_label.grid(row=0, column=0, columnspan=2)

    continue_choice_button_y = Button(win6, text="Yes", height=2, width=20, command= lambda: continue_choice_f("yes"))
    continue_choice_button_y.grid(row=1, column=0)

    continue_choice_button_n = Button(win6, text="No", height=2, width=20, command= lambda: continue_choice_f("no"))
    continue_choice_button_n.grid(row=1, column=1)

    win6.mainloop()

'''End of Program, Goodbye'''
win7 = Tk()
win7.title("Good Day")

good_day = Label(win7, text = "Alrighty then, have a good day!", font=('Arial',20))
good_day.grid(row=0, column=0)
button_exit = Button(win7, text = "Exit Program", command=exit)
button_exit.grid(row=1, column=0)

win7.mainloop()