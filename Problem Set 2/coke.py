"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
"""

def main():
    coke(50)

def coke(x):
    amount_due = x
    while True:
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin: ")
        coin = int(coin)
        if coin in [5, 10, 25]:
            amount_due -= coin
            if amount_due <= 0:
                print("Change owned:", -amount_due)
                break

main()