import random

''' Variables '''
initial_choice = 0
drink_input = 0
drink_input_number = 0
x = 0
continue_choice = "yes"
y1 = 0
drink_choice = 0
total_paid = 0
total_returned = 0
temp_total = 0

# Money
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

# Prices
price_coca_cola = float(1.50)
price_mountain_dew = float(1.50)
price_pepsi = float(1.50)
price_sprite = float(1.50)
price_dr_pepper = float(1.50)

price_d_coca_cola = float(1.50)
price_d_mountain_dew = float(1.50)
price_d_pepsi = float(1.50)
price_d_sprite = float(1.50)
price_d_dr_pepper = float(1.50)

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

# Products
product_coca_cola = ["Coca-Cola", stock_coca_cola]
product_mountain_dew = ["Mountain Dew", stock_mountain_dew]
product_pepsi = ["Pepsi", stock_pepsi]
product_sprite = ["Sprite", stock_sprite]
product_dr_pepper = ["Dr. Pepper", stock_dr_pepper]

product_d_coca_cola = ["Diet Coke", stock_d_coca_cola]
product_d_mountain_dew = ["Diet Mountain Dew", stock_d_mountain_dew]
product_d_pepsi = ["Diet Pepsi", stock_d_pepsi]
product_d_sprite = ["Sprite Zero", stock_d_sprite]
product_d_dr_pepper = ["Diet Dr. Pepper", stock_d_dr_pepper]

## Lists ##
products = ["Coca-Cola", "Mountain Dew", "Pepsi", "Sprite", "Dr. Pepper", "Diet Coke", "Diet Mountain Dew", "Diet Pepsi", "Sprite Zero", "Diet Dr. Pepper"]
stock = [stock_coca_cola, stock_mountain_dew, stock_pepsi, stock_sprite, stock_dr_pepper, stock_d_coca_cola, stock_d_mountain_dew, stock_d_pepsi, stock_d_sprite, stock_d_dr_pepper]
prices = [1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50]
products_stock = [product_coca_cola, product_mountain_dew, product_pepsi, product_sprite, product_dr_pepper, product_d_coca_cola, product_d_mountain_dew, product_d_sprite, product_d_dr_pepper]

''' Functions '''
# Product Choice
def drink_choice_():
    global drink_input
    global drink_input_number
    global products_stock
    global y1
    global drink_choice

    global products
    global stock
    global prices

    global product_coca_cola
    global product_mountain_dew
    global product_pepsi
    global product_sprite
    global product_dr_pepper

    global product_d_coca_cola
    global product_d_mountain_dew
    global product_d_pepsi
    global product_d_sprite
    global product_d_dr_pepper

    print("Here are your options and how many are available of each...")
    print('{:^20} {:^7} {:^5}'.format("Products", "Stock", "Prices"))
    for i in range(0, 9):
        print('{:^20} {:^7} {:^5}'.format(products[i], stock[i], prices[i]))
    print("--------")
    drink_input = input("What would you like to drink? ")
    drink_input.lower()
    drink_input.strip()
    while True:
        if drink_input == "coca-cola":
            drink_choice = price_coca_cola
            break
        elif drink_input == "mountain dew":
            drink_choice = price_mountain_dew
            break
        elif drink_input == "pepsi":
            drink_choice = price_pepsi
            break
        elif drink_input == "sprite":
            drink_choice = price_sprite
            break
        elif drink_input == "dr. pepper":
            drink_choice = price_dr_pepper
            break
        elif drink_input == "diet coke":
            drink_choice = price_d_coca_cola
            break
        elif drink_input == "diet mountain dew":
            drink_choice = price_d_mountain_dew
            break
        elif drink_input == "diet pepsi":
            drink_choice = price_d_pepsi
            break
        elif drink_input == "sprite zero":
            drink_choice = price_d_sprite
            break
        elif drink_input == "diet dr. pepper":
            drink_choice = price_d_dr_pepper
            break
        else:
            print("Invalid input. Please try again...")
            drink_input = input("What would you like to drink? ")
            drink_input.lower()

# How Much Product
def how_many_drinks():
    global drink_input
    global drink_input_number
    global products_stock
    global y1
    global drink_choice

    global product_coca_cola
    global product_mountain_dew
    global product_pepsi
    global product_sprite
    global product_dr_pepper

    global product_d_coca_cola
    global product_d_mountain_dew
    global product_d_pepsi
    global product_d_sprite
    global product_d_dr_pepper

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

    drink_input_number = str(input("How many would you like? "))
    drink_input_number.lower()
    drink_input_number.strip()
    drink_input_number = int(drink_input_number)
    while True:
        if drink_input == "coca-cola":
            while drink_input_number > stock[0]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[0] = stock[0] - drink_input_number
            return
        elif drink_input == "mountain dew":
            while drink_input_number > stock[1]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[1] = stock[1] - drink_input_number
            return
        elif drink_input == "pepsi":
            while drink_input_number > stock[2]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[2] = stock[2] - drink_input_number
            return
        elif drink_input == "sprite":
            while drink_input_number > stock[3]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[3] = stock[3] - drink_input_number
            return
        elif drink_input == "dr. pepper":
            while drink_input_number > stock[4]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[4] = stock[4] - drink_input_number
            return
        elif drink_input == "diet coke":
            while drink_input_number > stock[5]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[5] = stock[5] - drink_input_number
            return
        elif drink_input == "diet mountain dew":
            while drink_input_number > stock[6]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[6] = stock[6] - drink_input_number
            return
        elif drink_input == "diet pepsi":
            while drink_input_number > stock[7]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[7] = stock[7] - drink_input_number
            return
        elif drink_input == "sprite zero":
            while drink_input_number > stock[8]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[8] = stock[8] - drink_input_number
            return
        elif drink_input == "diet dr. pepper":
            while drink_input_number > stock[9]:
                print("Your request exceeds what is in stock. Please choose a different number.")
                drink_input_number = str(input("How many would you like? "))
                drink_input_number.lower()
                drink_input_number.strip()
                drink_input_number = int(drink_input_number)
            stock[9] = stock[9] - drink_input_number
            return
        else:
            print("Invalid input. Please try again...")
            drink_input_number = str(input("How many would you like? "))
            drink_input_number.lower()
            drink_input_number.strip()
            drink_input_number = int(drink_input_number)

# What Bills?
def what_bills():
    global drink_input
    global products_stock
    global y1
    global drink_choice
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

    print("How will you be paying today?")
    print("Below will be a series of inputs for each monetary denominations.")
    print("Please enter how many of each denomination will be used to pay today.")
    print("For any that would be none type 'none'.")
    print("--------")
    while True:
        try:
            bill_20 = int(input("How many $20 bills? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            bill_10 = int(input("How many $10 bills? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            bill_5 = int(input("How many $5 bills? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            bill_1 = int(input("How many $1 bills? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_100 = int(input("How many silver dollars? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_50 = int(input("How many 50-cent pieces? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_25 = int(input("How many quarters? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_10 = int(input("How many dimes? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_5 = int(input("How many nickels? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")
    while True:
        try:
            coin_1 = int(input("How many pennies? "))
            break
        except ValueError:
            print("Invalid input. Please try again...")

# Make Change
def make_change():
    global drink_input
    global drink_input_number
    global products_stock
    global y1
    global drink_choice
    global total_paid
    global total_returned
    global temp_total

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

    global bill_20r
    global bill_10r
    global bill_5r
    global bill_1r
    global coin_100r
    global coin_50r
    global coin_25r
    global coin_10r
    global coin_5r
    global coin_1r

    global price_coca_cola
    global price_mountain_dew
    global price_pepsi
    global price_sprite
    global price_dr_pepper

    global price_d_coca_cola
    global price_d_mountain_dew
    global price_d_pepsi
    global price_d_sprite
    global price_d_dr_pepper

    total_paid = round(float(20*bill_20 + 10*bill_10 + 5*bill_5 + bill_1 + coin_1 + 0.5*coin_50 + 0.25*coin_25 + 0.1*coin_10 + 0.05*coin_5 + 0.01*coin_1),2)
    print("You have paid a total of $" + str(total_paid))
    print("--------")
    total_returned = round(total_paid - drink_choice*drink_input_number,2)
    print("You will be returned the following amount:")
    print("$" + str(total_returned))
    print("--------")
    while total_returned >= 0.01:
        if total_returned >= 20:
            temp_total = round(total_returned % 20,2)
            bill_20r = round((total_returned - temp_total) / 20,0)
            total_returned = temp_total
        elif total_returned >= 10:
            temp_total = round(total_returned % 10,2)
            bill_10r = round((total_returned - temp_total) / 10,0)
            total_returned = temp_total
        elif total_returned >= 5:
            temp_total = round(total_returned % 5,2)
            bill_5r = round((total_returned - temp_total) / 5,0)
            total_returned = temp_total
        elif total_returned >= 1:
            temp_total = round(total_returned % 1,2)
            bill_1r = round((total_returned - temp_total) / 1,0)
            total_returned = temp_total
        elif total_returned >= 0.5:
            temp_total = round(total_returned % 0.5,2)
            coin_50r = round((total_returned - temp_total) / 0.5,0)
            total_returned = temp_total
        elif total_returned >= 0.25:
            temp_total = round(total_returned % 0.25,2)
            coin_25r = round((total_returned - temp_total) / 0.25,0)
            total_returned = temp_total
        elif total_returned >= 0.1:
            temp_total = round(total_returned % 0.1,2)
            coin_10r = round((total_returned - temp_total) / 0.1,0)
            total_returned = temp_total
        elif total_returned >= 0.05:
            temp_total = round(total_returned % 0.05,2)
            coin_5r = round((total_returned - temp_total) / 0.05,0)
            total_returned = temp_total
        else:
            coin_1r = round(total_returned / 0.01,2)
            total_returned = total_returned - total_returned
    print(str(int(bill_20r)) + " $20 bills")
    print(str(int(bill_10r)) + " $10 bills")
    print(str(int(bill_5r)) + " $5 bills")
    print(str(int(bill_1r)) + " $1 bills")
    print(str(int(coin_50r)) + " 50-cent pieces")
    print(str(int(coin_25r)) + " quarters")
    print(str(int(coin_10r)) + " dimes")
    print(str(int(coin_5r)) + " nickels")
    print(str(int(coin_1r)) + " pennies")

''' Vending Maching Code Begins Here'''
print("Hello!")
print("Welcome to Matt's Superior Vending!")
print("Would you like a cool drink today?")
initial_choice = input("(Yes or No) ")
initial_choice.lower()
initial_choice.strip()
print("--------")
while True:
    if initial_choice == "yes":
        break
    elif initial_choice == "no":
        print("Have a nice day!")
        print("Maybe next time.")
        x = input("Press enter to exit...")
        exit()
    else:
        print("Invalid input. Please try again...")
        initial_choice = input("(Yes or No) ")
        initial_choice.lower()
        initial_choice.strip()

'''Main Vending Code'''
while continue_choice == "yes":
    drink_choice = str(0)
    drink_choice_()
    print("--------")
    how_many_drinks()
    print("That will be $" + str(round(drink_choice*drink_input_number,2)))
    print("--------")
    what_bills()
    make_change()
    print("Would you like another drink?")
    continue_choice = input("(Yes or No) ")
    continue_choice.lower()
    continue_choice.strip()
    while True:
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            break
        else:
            print("Invalid input. Please try again...")
            print("Would you like another drink?")
            continue_choice = input("(Yes or No) ")
            continue_choice.lower()
            continue_choice.strip()
else:
    print("Have a good day! See you next time!")
    x = input("Press enter to exit...")
    exit()

