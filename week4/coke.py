
denominations = [5, 10, 25]
price = 50

while price > 0:
    print(f"Amount Due: {price}")
    user_insert = int(input("Insert A Coin: "))

    if user_insert in denominations:
         price -= user_insert

    else:
         print("Only 5, 10 OR 25 cents coins allowed")

if price < 0:
    print(f"Change owed: {-price}")

else  :
    print("Change owed: 0")