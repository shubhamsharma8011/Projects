#Given a list of words, sort it according to word length. 
lst = input("Enter the words: ").split()
new_lst = []
while len(lst) > 0:
    smallest = lst[0]
    for i in lst:
        if len(i) < len(smallest):
            smallest = i
    new_lst.append(smallest)
    lst.remove(smallest)
print("Sorted list:", new_lst)


#Create a menu-driven program for these list operations:
# Add an element ; Delete an element ; Search an element ; Display list ; Exit 
lst=input("Enter the list: ").split()
choice=int(input("Enter the numbers given below to get the specific output:\n" \
    "===  To Add an element  --> 1  ===\n" \
    "===  To Delete an element --> 2  ===\n" \
    "===  To Search an element  --> 3  ===\n" \
    "===  To Display list  --> 4  ===\n" \
    "===  EXIT --> 5  ===\n"  ))
if choice==1:
    element = input("Enter element: ")
    lst.append(element)
    print(lst)
if choice==2:
    element = input("Enter element to delete: ")
    if element in lst:
        lst.remove(element)
        print(lst)
    else:
        print("Element not found.")
if choice==3:
    element = input("Enter element to search: ")
    if element in lst:
        print(lst.index(element))
    else:
        print("Element not found.")
if choice==4:
    print("List:", lst)
if choice==5:
    print("EXIT")


# Store student names and marks in separate lists. Display the name(s) of student(s) with the highest marks. 
names = list(input("Enter the names of students: ").split())
marks = list(map(int, input("Enter the marks of students: ").split()))
high_marks = 0
for i in marks:
    if i > high_marks:
        high_marks = i
print("Highest marks:", high_marks)
print("Student(s) with highest marks:")
for i in range(len(marks)):
    if marks[i] == high_marks:
        print(names[i])


#Accept 10 integers and create separate lists for prime and non-prime numbers. 
lst = list(map(int, input("Enter 10 integers: ").split()))
prime = []
non_prime = []
for n in lst:
    if n < 2:
        non_prime.append(n)
    else:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            prime.append(n)
        else:
            non_prime.append(n)
print("Prime numbers:", prime)
print("Non-prime numbers:", non_prime)


#Store monthly sales in a list and display:
# Total sales ; Best month ; Lowest-sales month ; Months with sales above average
months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]
sales = list(map(int, input("Enter sales for 12 months: ").split()))
total = 0
highest = sales[0]
lowest = sales[0]
for i in sales:
    total = total + i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / len(sales)
print("Total sales:", total)
print("Best month:", months[sales.index(highest)])
print("Lowest-sales month:", months[sales.index(lowest)])
print("Months with sales above average:")
for i in range(len(sales)):
    if sales[i] > average:
        print(months[i]) 


#Store temperatures for seven days and count how many days had temperature above 30°C. 
temperatures = list(map(int, input("Enter temperatures for 7 days: ").split()))
count = 0
for i in temperatures:
    if i > 30:
        count = count + 1
print("Number of days above 30°C:", count)


#Accept a sentence, split it into words, and create a list of unique words.
sentence = input("Enter a sentence: ")
words = sentence.split()
usual_words=["apple", "book", "school", "student", "teacher",
         "friend", "water", "house", "computer", "phone",
         "table", "chair", "music", "game", "food",
         "car", "tree", "flower", "mountain", "travel"]
unique_words = []
for i in words:
    if i not in usual_words:
        unique_words.append(i)
print("Unique words:", unique_words)


# Simulate a shopping cart using a list: add, remove, search, and display products. 
cart=input("Enter the list: ").split()
choice=int(input("Enter the numbers given below to get the specific output:\n" \
    "1. Add product\n"\
    "2. Remove product\n"\
    "3. Search product\n"\
    "4. Display cart\n"\
    "5. Exit\n"))
if choice==1:
    product = input("Enter product: ")
    cart.append(product)
    print("Product added.")
if choice==2:
    product = input("Enter product to remove: ")
    if product in cart:
        cart.remove(product)
        print("Product removed.")
    else:
        print("Product not found.")
if choice==3:
    product = input("Enter product to search: ")
    if product in cart:
        print("Product found.")
    else:
        print("Product not found.")
if choice==4:
    print("Shopping cart:", cart)
if choice==5:
    print("EXIT")


# Create a list-based inventory system where an item is removed after it is sold. 
inventory = list(input("Enter the inventory: ").split())
print("Inventory:", inventory)
item = input("Enter item sold: ")
if item in inventory:
    inventory.remove(item)
    print("Item sold and removed from inventory.")
else:
    print("Item not available.")
print("Updated inventory:", inventory)


#Input a list of exam marks and assign grades using a second list. 
marks = list(map(int, input("Enter marks: ").split()))
grades = []
for i in marks:
    if i >= 90:
        grades.append("A")
    elif i >= 75:
        grades.append("B")
    elif i >= 60:
        grades.append("C")
    elif i >= 40:
        grades.append("D")
    else:
        grades.append("E")
print("Marks:", marks)
print("Grades:", grades)


#Accept a list and returns a new list containing only distinct prime numbers.
lst = list(map(int, input("Enter the integers: ").split()))
prime = []
for n in lst:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        prime.append(n)
distint_prime = []
for i in prime:
    if i not in distint_prime:
        distint_prime.append(i)
print("Prime numbers:", prime)
print("Distint Prime numbers:", distint_prime)
