import datetime

# Function to add an expense
def add_expense(expenses):
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD, leave blank for today): ")
    if not date:
        date = datetime.date.today().strftime("%Y-%m-%d")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(expenses):
    print("All Expenses:")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

# Function to view spending by category
def view_spending_by_category(expenses):
    category = input("Enter the category to view spending: ")
    total_spent = sum(expense['amount'] for expense in expenses if expense['category'] == category)
    print(f"Total spending in {category}: {total_spent}")

# Main function
def main():
    expenses = []
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending by Category")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_spending_by_category(expenses)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
