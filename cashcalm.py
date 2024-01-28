
class CalendarManager:

    def __init__(self):
        self.calendar_events = {}

    def add_event(self, date, event):
        if date not in self.calendar_events:
            self.calendar_events[date] = []
        self.calendar_events[date].append(event)

    def display_calendar(self):
        print("\nCalendar:")
        for date, events in self.calendar_events.items():
            print(f"{date}: {', '.join(events)}")


class BudgetManager:
    def __init__(self):
        self.balance = 0
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        self.balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

    def display_expenses(self):
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"${expense['amount']} - {expense['category']}")

            
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTasks:")
        for task in self.tasks:
            print(task)



def main():
    calendar_manager = CalendarManager()
    budget_manager = BudgetManager()
    task_manager = TaskManager()

    while True:
        print("\n===== CashCalm =====")
        print("1. Add Expense")
        print("2. Display Balance")
        print("3. Display Expenses")
        print("4. Add Calendar Event")
        print("5. Display Calendar")
        print("6. Add Task")
        print("7. Display Tasks")
        print("8. Mindfulness Prompt")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            budget_manager.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == "2":
            budget_manager.display_balance()

        elif choice == "3":
            budget_manager.display_expenses()

        elif choice == "4":
            date = input("Enter event date (YYYY-MM-DD): ")
            event = input("Enter event description: ")
            calendar_manager.add_event(date, event)
            print("Calendar event added successfully!")

        elif choice == "5":
            calendar_manager.display_calendar()

        elif choice == "6":
            task = input("Enter task description: ")
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == "7":
            task_manager.display_tasks()

        elif choice == "8":
            print("Mindfulness Prompt: Take a deep breath and relax for a moment.")

        elif choice == "9":
            print("Exiting CashCalm. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
