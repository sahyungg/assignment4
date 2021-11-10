price_of_apples = int(20)
price_of_oranges = int(25)

def getPrices():
    apples_to_buy = int(input("How many apples would you like to buy? "))
    oranges_to_buy = int(input("How many oranges would you like to buy? "))
    computation = (apples_to_buy*price_of_apples) + (oranges_to_buy*price_of_oranges)
    return computation

def display():
    print(f"The total amount is {total}.")


total = getPrices()
display()