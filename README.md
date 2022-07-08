# vending_machine
Vending Machine Project

This is a repository for my vending maching project for CS - T599

# Variable Dictionary #

## Generic variables used during various calculations.
initial_choice = 0
This variable is used to determine if the program should continue running or not.

drink_input_number = 0
Variable that contains the number of sodas to be purchased.

continue_choice = "yes"
Determines if the while-loop for the program should continue, or move to the exit program window.

drink_choice = 0
Contains the soda choice of the customer.

total_paid = 0
Contains the total money the customer pays to the machine.

total_returned = 0
Conrains the total amount of money to be returned to the customer.

total_due = 0
Contains the total cost of the purchase made by the customer.

## Money Input - These variables are all used for the monetary input function and hold the number of each bill and coin inserted into the machine.
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

## Money Output - These variables hold the number of each bill and coin being returned to the customer duringng the "making change" portion of the code.
bill_20r = 0
bill_10r = 0bill_5r = 0
bill_1r = 0
coin_100r = 0
coin_50r = 0
coin_25r = 0
coin_10r = 0
coin_5r = 0
coin_1r = 0

## Stock - These variables create the value of stock for each product in the inventory. It simply creates a random number when the program is fired.
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

# Lists #
The only list I ended up using was a list containing the stock of all the products. I used this in my stock function and each time a product was purchased the list was updated. This way the variables were randomly assigned at the start of the program, but then updated using this list after that.

stock = [stock_coca_cola, stock_mountain_dew, stock_pepsi, stock_sprite, stock_dr_pepper, stock_d_coca_cola, stock_d_mountain_dew, stock_d_pepsi, stock_d_sprite, stock_d_dr_pepper]
