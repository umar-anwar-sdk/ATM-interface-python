import tkinter as tk
from tkinter import messagebox, simpledialog


class Account:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000  # Starting balance for demonstration purposes
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            messagebox.showerror("Error", "Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            messagebox.showerror("Error", "Insufficient funds!")

    def get_transaction_history(self):
        return self.transaction_history


class ATMGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Umar Bank ATM")

        self.atm = None
        self.create_login_screen()

    def create_login_screen(self):
        self.master.geometry("800x400")

        self.label_user_id = tk.Label(self.master, text="User ID:")
        self.label_user_id.pack()

        self.entry_user_id = tk.Entry(self.master)
        self.entry_user_id.pack()

        self.label_pin = tk.Label(self.master, text="PIN:")
        self.label_pin.pack()

        self.entry_pin = tk.Entry(self.master, show="*")
        self.entry_pin.pack()

        self.button_login = tk.Button(self.master, text="Login", command=self.login)
        self.button_login.pack()

    def create_atm_screen(self):
        self.master.geometry("800x600")

        self.label_balance = tk.Label(self.master, text="Balance: $0")
        self.label_balance.pack(pady=10)

        self.button_history = tk.Button(self.master, text="Transaction History", command=self.show_history,
                                        padx=10, pady=5, bg="lightblue", fg="black")
        self.button_history.pack(pady=10)

        self.button_withdraw = tk.Button(self.master, text="Withdraw", command=self.withdraw,
                                         padx=10, pady=5, bg="orange", fg="black")
        self.button_withdraw.pack(pady=10)

        self.button_deposit = tk.Button(self.master, text="Deposit", command=self.deposit,
                                        padx=10, pady=5, bg="green", fg="black")
        self.button_deposit.pack(pady=10)

        self.button_transfer = tk.Button(self.master, text="Transfer", command=self.transfer,
                                         padx=10, pady=5, bg="purple", fg="white")
        self.button_transfer.pack(pady=10)

        self.button_quit = tk.Button(self.master, text="Quit", command=self.master.destroy,
                                     padx=10, pady=5, bg="red", fg="white")
        self.button_quit.pack(pady=10)
    def login(self):
        user_id = self.entry_user_id.get()
        pin = self.entry_pin.get()

        # Assume a user with user_id "123" and pin "456" for demonstration purposes
        if user_id == "123" and pin == "456":
            self.atm = Account(user_id, pin)
            self.create_atm_screen()
            messagebox.showinfo("Login Successful", "Welcome to the Umar Bank!")
        else:
            messagebox.showerror("Login Failed", "Invalid user ID or PIN. Please try again.")

    def show_history(self):
        if self.atm:
            history = "\n".join(self.atm.get_transaction_history())
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showerror("Error", "Please login first.")

    def withdraw(self):
        if self.atm:
            amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
            if amount is not None:
                self.atm.withdraw(amount)
                self.update_balance_label()
        else:
            messagebox.showerror("Error", "Please login first.")

    def deposit(self):
        if self.atm:
            amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
            if amount is not None:
                self.atm.deposit(amount)
                self.update_balance_label()
        else:
            messagebox.showerror("Error", "Please login first.")

    def transfer(self):
        if self.atm:
            recipient_id = simpledialog.askstring("Transfer", "Enter recipient's User ID:")
            amount = simpledialog.askfloat("Transfer", "Enter transfer amount:")

            # For simplicity, assume recipient has the same pin as the user for demonstration purposes
            recipient = Account(recipient_id, self.atm.pin)

            self.atm.transfer(recipient, amount)
            self.update_balance_label()
        else:
            messagebox.showerror("Error", "Please login first.")

    def update_balance_label(self):
        if self.atm:
            self.label_balance.config(text=f"Balance: ${self.atm.balance}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
