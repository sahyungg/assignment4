def getEverything():
    money_owned = int(input("How much money do I have? "))
    apple_price = int(input("How much does an apple cost? "))
    maximum = money_owned // apple_price
    change = money_owned % apple_price
    return maximum, change

def display():
    print(f"You can buy {max} apples and your change is {change} pesos.")


max, change = getEverything()
display()