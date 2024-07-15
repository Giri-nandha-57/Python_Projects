import tkinter as tk
from tkinter import messagebox, ttk
import json

root = tk.Tk()
root.title("Personal Expense Tracker")

root.geometry("500x400")

expenses = []

def add_expense():
    amount = amount_entry.get()
    category = category_var.get()
    description = description_entry.get()
    
    if amount and category and description:
        expense = {"amount": amount, "category": category, "description": description}
        expenses.append(expense)
        save_expenses()
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        view_expenses()
    else:
        messagebox.showwarning("Warning", "All fields must be filled out.")

def view_expenses():
    expense_list.delete(0, tk.END)
    for expense in expenses:
        display_text = f"{expense['amount']} - {expense['category']} - {expense['description']}"
        expense_list.insert(tk.END, display_text)

def save_expenses():
    with open('Expense_Tracker/expenses.json', 'w') as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open('Expense_Tracker/expenses.json', 'r') as file:
            global expenses
            expenses = json.load(file)
            view_expenses()
    except FileNotFoundError:
        pass

load_expenses()

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.map('TButton', foreground=[('active', 'blue')], background=[('active', 'lightgrey')])

tk.Label(root, text="Amount:", font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
tk.Label(root, text="Category:", font=('Helvetica', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
tk.Label(root, text="Description:", font=('Helvetica', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='e')

amount_entry = ttk.Entry(root, style='TEntry', width=25)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

categories = ["Food", "Transport", "Entertainment", "Other"]
category_var = tk.StringVar(value=categories[0])
category_menu = ttk.Combobox(root, textvariable=category_var, values=categories, font=('Helvetica', 12), width=23)
category_menu.grid(row=1, column=1, padx=10, pady=10)

description_entry = ttk.Entry(root, style='TEntry', width=25)
description_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = ttk.Button(root, text="Add Expense", command=add_expense, style='TButton')
add_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

expense_list = tk.Listbox(root, width=50, height=10, font=('Helvetica', 12))
expense_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", save_expenses)

root.mainloop()
