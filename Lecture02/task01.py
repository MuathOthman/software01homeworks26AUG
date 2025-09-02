total_coins = 0

coins = int(input("Give me money: "))
total_coins += coins

while total_coins <= 5:
    print(f"Not enough! Give me {5-total_coins}")
    coins = int(input("Add more money: "))
    total_coins += coins
print("Thank You!")