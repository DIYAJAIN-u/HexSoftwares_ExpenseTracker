#HEXSOFTWARES INTERNSHIP TASK 2
print("Simple Expense Tracker")

expenses = []

while True:
    print('\n------------ Select an choice -------------')
    print('\n1. Add Expense')
    print('2. View Expenses')
    print('3. Total Expenses')
    print('4. Exit')

    choice = input("Enter your choice: ").strip()

    if choice == '1':
     while True:
        category = input("Enter category (Food/Travel/Shopping/etc): ").strip().lower()
        name = input("Enter expense name: ").strip()
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "name": name,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added!")
        print(f"\nAdded Expense: {name} - ₹{amount}")

        more = input("\nAdd another expense? (y/n): ").strip().lower()

        if more != 'y':
            break

    elif choice == '2':
        if not expenses:
            print("\nNo expenses found!")
        else:
            print("\nYour Expenses:")
            for exp in expenses:
                print(f"{exp['category'].capitalize()} | {exp['name']} | ₹{exp['amount']}")

        print("Expenses listed!")

    elif choice == '3':
        total = sum(exp["amount"] for exp in expenses)
        print(f"\nTotal Expenses: ₹{total}")

    elif choice == '4':
        print("\nExiting the Expense Tracker. Goodbye!")
        print("Thank You!")
        break

    else:
        print("\nInvalid choice! Please try again.")