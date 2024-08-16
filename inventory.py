
inventory = {}  


n = int(input("How many entries? "))


for i in range(1, n + 1):
    t = input("Enter title: ")
    a = input("Enter author: ")
    p = int(input("Enter book price: "))
    s = int(input("Enter stock: "))

    inventory[t] = {'author': a, 'price': p, 'stock': s}


print(inventory)


sales = 0 


while True:
    s = input("Would you like to buy a book? (y/n): ")

    if s.lower() == 'y':
        book = input(f"Which book would you like to buy? title:'{t}' ")

        if book in inventory:
            if inventory[book]['stock'] > 0:
                inventory[book]['stock'] -= 1 
                print(f"Book '{book}' by {inventory[book]['author']} successfully purchased for Rs:{inventory[book]['price']}.")
                sales += 1
            else:
                print("Sorry, that book is out of stock.")
        else:
            print("Sorry, we don't have that book in our inventory.")
    elif s.lower() == 'n':
        print("Thank you for your visit.")
        break 
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
