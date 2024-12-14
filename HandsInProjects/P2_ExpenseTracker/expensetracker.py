import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("700x550")

        # Initialize expense data
        self.expenses = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Creates all UI components for the application."""

        # Title
        title_label = tk.Label(
            self.root, text="Expense Tracker", font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

        # Add Expense Frame
        add_frame = tk.Frame(
            self.root, padx=20, pady=10, relief=tk.GROOVE, borderwidth=2
        )
        add_frame.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(add_frame, text="Date (YYYY-MM-DD):").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.date_entry = tk.Entry(add_frame, width=20)
        self.date_entry.grid(row=0, column=1, padx=10)

        tk.Label(add_frame, text="Category:").grid(row=1, column=0, sticky="w", pady=5)
        self.category_entry = tk.Entry(add_frame, width=20)
        self.category_entry.grid(row=1, column=1, padx=10)

        tk.Label(add_frame, text="Amount:").grid(row=2, column=0, sticky="w", pady=5)
        self.amount_entry = tk.Entry(add_frame, width=20)
        self.amount_entry.grid(row=2, column=1, padx=10)

        tk.Label(add_frame, text="Description:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.description_entry = tk.Entry(add_frame, width=50)
        self.description_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        add_button = tk.Button(
            add_frame,
            text="Add Expense",
            command=self.add_expense,
            bg="green",
            fg="white",
        )
        add_button.grid(row=4, column=1, pady=10)

        # Expense List Frame
        list_frame = tk.Frame(
            self.root, padx=20, pady=10, relief=tk.GROOVE, borderwidth=2
        )
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # Scrollable Treeview for expenses
        self.tree = ttk.Treeview(
            list_frame,
            columns=("Date", "Category", "Amount", "Description"),
            show="headings",
        )
        self.tree.heading("Date", text="Date")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Description", text="Description")
        self.tree.column("Date", width=100)
        self.tree.column("Category", width=100)
        self.tree.column("Amount", width=80)
        self.tree.column("Description", width=300)

        tree_scroll = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        self.tree.configure(yscroll=tree_scroll.set)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Total Expenses Frame (Updated)
        total_frame = tk.Frame(
            self.root, padx=20, pady=10, relief=tk.RAISED, borderwidth=2, bg="lightgray"
        )
        total_frame.pack(fill=tk.X, padx=20, pady=5)

        self.total_label = tk.Label(
            total_frame,
            text="Total Expenses: $0.00",
            font=("Arial", 14, "bold"),
            bg="lightgray",
        )
        self.total_label.pack(side=tk.LEFT)

    def add_expense(self):
        """Adds a new expense to the tracker."""
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        # Date validation
        if not self.validate_date(date):
            messagebox.showerror(
                "Input Error", "Please enter a valid date in the format YYYY-MM-DD!"
            )
            return

        # Input validation
        if not category or not amount:
            messagebox.showerror("Input Error", "Please fill in all required fields!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid number!")
            return

        # Add to expense list and clear entries
        self.expenses.append(
            {
                "date": date,
                "category": category,
                "amount": amount,
                "description": description,
            }
        )
        self.tree.insert(
            "", tk.END, values=(date, category, f"${amount:.2f}", description)
        )
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

        # Automatically update the total after adding an expense
        self.calculate_total()

        messagebox.showinfo("Success", "Expense added successfully!")

    def validate_date(self, date):
        """Validates the date format (YYYY-MM-DD) and checks if it is a real date."""
        try:
            # Try to parse the date
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            # If parsing fails, the date is invalid
            return False

    def calculate_total(self):
        """Calculates and displays the total expenses."""
        total = sum(expense["amount"] for expense in self.expenses)
        self.total_label.config(text=f"Total Expenses: ${total:.2f}")


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
