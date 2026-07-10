from datetime import datetime
import json

FILENAME = "expenses.json"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()
     
    def load_data(self):
        try:
            with open(FILENAME, 'r') as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def save_data(self):
        with open(FILENAME, 'w') as f:
            json.dump(self.expenses, f)
    
    def add_expenses(self):
        try:
            amount = float(input('Enter amount: '))
        except ValueError:
            print('Please enter valid number')
            return
        category = input('Enter category: ') 
        date = datetime.now().strftime("%y-%m-%d")
        self.expenses.append({"amount": amount,
                              "category": category,
                              "date": date})
        self.save_data()
        print(f"Expenses of {amount} added under {category} ")       
            
    def show_all(self):
        if not self.expenses:
            print('No expenses yet')
            return
        print('\nYour Expenses:')
        for i, item in enumerate(self.expenses,start=1):
            print(f"{i} {item["amount"]} - {item["category"]} - {item["date"]}")

    def get_total(self):
        total = sum(item["amount"] for item in self.expenses)
        print(f"Total Expenses {total}")
        
    def get_category_summary(self):
        summary = {}
        if not self.expenses:
            print('No expenses yet')
            return
        print('\nHere is your category wise summary')
        for item in self.expenses:
            cat = item["category"]
            amt = item["amount"]
            if cat in summary:
                summary[cat] += amt
            else:
                summary[cat] = amt
            
        for cat, total in summary.items():
            print(f"{cat}: {total}")     

    def remove_expenses(self):
        self.show_all()
        if not self.expenses:
            print(f'No expenses yet')
            return
        index = int(input('Enter expense number to delete: '))-1
        if 0<= index<len(self.expenses):
            remove = self.expenses.pop(index)
            self.save_data()
            print(f'{remove["amount"]} - {remove["category"]} is now deleted ')
        else:
            print('Invalid number')

def main():
    tracker = ExpenseTracker()
    menu = """Expenses tracker!
        1. Add expenses
        2. View all expenses
        3. total expenses
        4. category wise summary
        5. delete expenses
        6. exit"""
    
    while True:

        chose = int(input('Enter a number between (1-6): '))
        if chose == 1:
            tracker.add_expenses()
        elif chose == 2:
            tracker.show_all()
        elif chose == 3:
            tracker.get_total()
        elif chose == 4:
            tracker.get_category_summary()
        elif chose == 5:
            tracker.remove_expenses()
        elif chose ==6:
            print('Thank you Goodbye!')
            break

main()
   