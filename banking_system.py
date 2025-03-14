# -*- coding: utf-8 -*-
"""Bank-System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-v04YIeQMYXa-uMhfeJYcOl4ThNvTJ77
"""

import random


class Bank:
    def __init__(self):
        """
        Initializes a Bank instance with dictionaries to manage user accounts and their transactions.
        """
        self.accounts = {}  # Stores user accounts
        self.transactions = {}  # Keeps track of transaction history

def create_account(self, account_holder, initial_balance):
        """
        Creates a new bank account for a user.

        Args:
            account_holder (str): Name of the account holder.
            initial_balance (float): Starting balance for the account.

        Returns:
            BankAccount: The newly created account instance.
        """
        account_number = self.generate_account_number()
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        self.transactions[account_number] = []
        return account

def generate_account_number(self):
        """
        Generates an 8-digit random account number.

        Returns:
            str: A randomly generated account number.
        """
        return "".join(random.choice("0123456789") for _ in range(8))

def get_account(self, account_number):
        """
        Retrieves the account object based on the account number provided.

        Args:
            account_number (str): Account number to search for.

        Returns:
            BankAccount: The account instance if found, otherwise None.
        """
        return self.accounts.get(account_number)

def perform_transaction(self, account_number, transaction_type, amount):
        """
        Processes a deposit or withdrawal transaction for a specified account.

        Args:
            account_number (str): The account number on which to perform the transaction.
            transaction_type (str): Type of transaction (deposit or withdraw).
            amount (float): The amount involved in the transaction.

        Returns:
            str: Message indicating whether the transaction was successful or not.
        """
        account = self.get_account(account_number)
        if not account:
            return "Account not found."

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            return "Invalid transaction type."

        self.transactions[account_number].append((transaction_type, amount))
        return "Transaction successful."

def get_transaction_history(self, account_number):
        """
        Fetches the list of past transactions for a given account.

        Args:
            account_number (str): The account number to retrieve history for.

        Returns:
            list: A list of tuples representing transactions (type, amount), or an empty list if no history exists.
        """
        return self.transactions.get(account_number, [])

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        """
        Initializes a bank account with basic details.

        Args:
            account_number (str): Unique account number.
            account_holder (str): Name of the account holder.
            initial_balance (float): Starting balance in the account.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Adds funds to the account balance.

        Args:
            amount (float): Amount to be deposited.
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Deducts funds from the account balance if sufficient funds are available.

        Args:
            amount (float): Amount to be withdrawn.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: Available balance in the account.
        """
        return self.balance

def main():
    """
    Runs the interactive console-based banking system.
    """
    bank = Bank()

    while True:
        print("\n----------------------Baking System-------------------------")
        print("1. Create Account")
        print("2. Perform Transaction")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = bank.create_account(account_holder, initial_balance)
            print(f"Account created successfully. Account Number: {account.account_number}")

        elif choice == "2":
            account_number = input("Enter account number: ")
            transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
            amount = float(input("Enter transaction amount: "))
            result = bank.perform_transaction(account_number, transaction_type, amount)
            print(result)

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Account Balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            transactions = bank.get_transaction_history(account_number)
            if transactions:
                print("Transaction History:")
                for trans_type, amount in transactions:
                    print(f"{trans_type.capitalize()}: ${amount}")
            else:
                print("Account not found or no transaction history.")

        elif choice == "5":
            print("Exiting the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

