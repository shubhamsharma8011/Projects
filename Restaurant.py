
restaurant = input("Enter restaurant name: ")
menu = {1: ["Burger", 180],2: ["Pizza", 350],3: ["Momo", 150],4: ["Chowmein", 120],5: ["Fried Rice", 200],6: ["Coffee", 80]}
orders = {}
occupied = []
print("---", restaurant, "---")
choice = input("Enter your choice: \n"
    "1. Show Menu\n"
    "2. Order Food\n"
    "3. Generate Bill\n"
    "4. Check Tables\n"
    "5. Exit")

if choice == "1":
    print("--- FOOD MENU ---")
    for i in menu:
        print(i, menu[i][0], "- Rs.", menu[i][1])

elif choice == "2":
    table = int(input("Enter table number (1-10): "))
    if table < 1 or table > 10:
        print("Invalid table number!")
    elif table in occupied:
        print("Table is already occupied!")
    else:
        order = []
        total = 0
        count = 0
        print("Enter 0 to finish ordering.")
        while True:
            item = int(input("Enter food number: "))
            if item == 0:
                break
            if item not in menu:
                print("Invalid food number!")
                continue
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Enter a valid quantity!")
                continue
            name = menu[item][0]
            price = menu[item][1]
            amount = price * qty
            order.append([name, qty, amount])
            total = total + amount
            count = count + qty
            if count == 0:
                print("No items ordered.")
            else:
                discount = 0
                if count >= 5:
                    discount = total * 0.10
                final = total - discount
                orders[table] = [order, total, discount, final]
                occupied.append(table)
                print("Order placed successfully!")
                print("Total: Rs.", total)
                print("Discount: Rs.", discount)
                print("Final Amount: Rs.", final)
elif choice == "3":
    table = int(input("Enter table number: "))
    if table in orders:
        print("--- CUSTOMER BILL ---")
        print("Restaurant:", restaurant)
        print("Table Number:", table)
        for item in orders[table][0]:
            print(item[0], "x", item[1], "= Rs.", item[2])
            print("Total: Rs.", orders[table][1])
            print("Discount: Rs.", orders[table][2])
            print("Final Bill: Rs.", orders[table][3])
            print("Thank you for visiting!")
            del orders[table]
            occupied.remove(table)
            print("Table is now available.")
    else:
        print("No order found for this table.")
elif choice == "4":
    print("--- TABLE STATUS ---")
    for table in range(1, 11):
        if table in occupied:
            print("Table", table, "- Occupied")
        else:
            print("Table", table, "- Available")
elif choice == "5":
    print("Thank you for using", restaurant)
    

