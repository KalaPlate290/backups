import time
print("Welcome to BFC")
order1 = "1. Hot Spicy Chicken (6-Piece)"
price1 = 8.49
order2 = "2. Leg Piece Bucket"
price2 = 5.49
order3 = "3. Zinger Bogo"
price3 = 5.99
order4 = "4. Double Down (NO BUN, ONLY CHICKEN!)"
price4 = 2.99

def order(total=0):
    choice = input(f"What would you like to have?\n {order1} - $8.49\n {order2} - $5.49\n {order3} - $5.99\n {order4} - $2.99\n")

    if choice == "1":
        wants1 = int(input(f"How many of {order1} do you want? "))
        total += wants1 * price1
    elif choice == "2":
        wants2 = int(input(f"How many of {order2} do you want? "))
        total += wants2 * price2
    elif choice == "3":
        wants3 = int(input(f"How many of {order3} do you want? "))
        total += wants3 * price3
    elif choice == "4":
        wants4 = int(input(f"How many of {order4} do you want? "))
        total += wants4 * price4
    else:
        print("Please input a valid value.\n")
        order(total)
        return

    ask = input("Anything else? (y/n): ").lower()

    if ask == "y":
        order(total)
    elif ask == "n":
        print(f"Thanks for visiting BFC. Your total is: ${total:.2f}. Have a great day!")
        time.sleep(5)
        print("Closing now...")
    else:
        print("Please enter 'y' or 'n'.")
        order(total)

order()