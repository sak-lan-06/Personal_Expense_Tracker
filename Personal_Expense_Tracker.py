import os
import json

# file to store expenses
Expense_file = "expenses.txt"


# function to load expenses from the file
def load_expenses():
    if not os.path.exists(Expense_file):
        return []
    with open(Expense_file, "r") as file:
        return json.load(file)


# function to save expenses to the file
def save_expenses(expenses):
    with open(Expense_file, "w") as file:
        for expense in expenses:
            file.write(str(expense) + "\n")


# function to display expenses by category
def display_summary(expenses):
    if not expenses:
        print("No expenses recorded yet!")
        return

    print("\n Expense Summary by category:")
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount

    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

    total_spent = sum(item["amount"] for item in expenses)
    print(f"\n Total Spent: ${total_spent:.2f}")


def expense_tracker():
    print("Welcome to the Personal Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\n Options:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3) :")

        if choice == '1':
            description = input("Enter the description: ")
            category = input("Enter the category (e.g,food, travel, shopping) :")

            try:
                amount = float(input("Enter the amount : $"))
                expense = {"description": description, "category": category, "amount": amount}
                expenses.append(expense)
                save_expenses(expenses)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid amount! Please try again. ")

        elif choice == "2":
            display_summary(expenses)

        elif choice == "3":
            print("Goodbye! Your expenses are saved.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    expense_tracker()

Output:
Welcome to the Personal Expense Tracker!

 Options:
1. Add Expense
2. View Expense Summary
3. Exit
Enter your choice (1-3) :1
Enter the description: Stationary 
Enter the category (e.g,food, travel, shopping) :Books,Pens
Enter the amount : $120
Expense added successfully!

 Options:
1. Add Expense
2. View Expense Summary
3. Exit
Enter your choice (1-3) :1
Enter the description: lunch 
Enter the category (e.g,food, travel, shopping) :food
Enter the amount : $239
Expense added successfully!

 Options:
1. Add Expense
2. View Expense Summary
3. Exit
Enter your choice (1-3) :2

 Expense Summary by category:
Books,Pens: $120.00
food: $239.00

 Total Spent: $359.00

 Options:
1. Add Expense
2. View Expense Summary
3. Exit
Enter your choice (1-3) :3
Goodbye! Your expenses are saved.




