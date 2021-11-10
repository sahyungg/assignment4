def getPrices():
    price_of_apples = int(20)
    apples_to_buy = int(input("How many apples would you like to buy? "))
    apple = (apples_to_buy) * (price_of_apples)
    price_of_oranges = int(25)
    oranges_to_buy = int(input("How many oranges would you like to buy? "))
    orange = (oranges_to_buy) * (price_of_oranges)
    return apple, orange

def getCompute():
    computation = apples + oranges
    return computation

def display():
    print(f"The total amount is {total_amount}.")


apples, oranges = getPrices()
total_amount = getCompute()
display()