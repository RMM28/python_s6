import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.weekly_expenses = {}
        self.monthly_expenses = {}

        self.label_expense = tk.Label(root, text="Expense:")
        self.label_expense.grid(row=0, column=0, padx=5, pady=5)

        self.entry_expense = tk.Entry(root)
        self.entry_expense.grid(row=0, column=1, padx=5, pady=5)

        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.grid(row=1, column=0, padx=5, pady=5)

        self.entry_amount = tk.Entry(root)
        self.entry_amount.grid(row=1, column=1, padx=5, pady=5)

        self.button_add = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.button_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.label_weekly_expense = tk.Label(root, text="Weekly Expenses:")
        self.label_weekly_expense.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.label_weekly_amount = tk.Label(root, text="")
        self.label_weekly_amount.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.label_monthly_expense = tk.Label(root, text="Monthly Expenses:")
        self.label_monthly_expense.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.label_monthly_amount = tk.Label(root, text="")
        self.label_monthly_amount.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Calculate weekly and monthly expenses
        self.calculate_weekly_monthly_expenses()

    def add_expense(self):
        expense = self.entry_expense.get()
        amount = self.entry_amount.get()

        if expense and amount:
            self.expenses.append((expense, float(amount)))
            self.update_expense_labels()
            self.entry_expense.delete(0, tk.END)
            self.entry_amount.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both expense and amount.")

    def calculate_weekly_monthly_expenses(self):
        # Reset the dictionaries
        self.weekly_expenses = {}
        self.monthly_expenses = {}

        # Get the current date
        today = datetime.now()

        # Calculate the start and end dates for the current week
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Calculate the start and end dates for the current month
        start_of_month = today.replace(day=1)
        end_of_month = (today.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        # Iterate through expenses and calculate weekly and monthly totals
        for expense, amount in self.expenses:
            if start_of_week <= today <= end_of_week:
                self.weekly_expenses[expense] = self.weekly_expenses.get(expense, 0) + amount
            if start_of_month <= today <= end_of_month:
                self.monthly_expenses[expense] = self.monthly_expenses.get(expense, 0) + amount

        # Update the labels
        self.update_expense_labels()

        # Reschedule for the next week
        self.root.after(60000, self.calculate_weekly_monthly_expenses)

    def update_expense_labels(self):
        # Update weekly expenses label
        weekly_total = sum(self.weekly_expenses.values())
        self.label_weekly_amount.config(text=f"${weekly_total:.2f}")

        # Update monthly expenses label
        monthly_total = sum(self.monthly_expenses.values())
        self.label_monthly_amount.config(text=f"${monthly_total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
