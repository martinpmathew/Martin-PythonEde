"""
Objectives
improving the student's skills in operating with the getter, setter, and deleter methods;
improving the student's skills in creating their own exceptions.
Scenario
Implement a class representing an account exception,
Implement a class representing a single bank account,
This class should control access to the account number and account balance attributes by implementing the properties:
it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
it should not be possible to delete an account as long as the balance is not zero;
test your class behavior by:
setting the balance to 1000;
trying to set the balance to -200;
trying to set a new value for the account number;
trying to deposit 1.000.000;
trying to delete the account attribute containing a non-zero balance.
"""

class AccountException(Exception):
    """Custom exception for bank account errors."""
    pass

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        # We set the private attributes directly here to bypass 
        # the setter logic during initial creation if needed.
        self._account_number = account_number
        self._balance = initial_balance

    # --- Account Number Property (Read-Only) ---
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        raise AccountException("Account number is immutable and cannot be changed!")

    # --- Balance Property ---
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException("Balance cannot be negative.")
        
        # Check for audit threshold (100,000)
        # We check the difference between the current balance and the new value
        change = abs(value - self._balance)
        if change > 100000:
            print(f"AUDIT ALERT: Large transaction detected! Amount: {change:,.2f}")
        
        self._balance = value

    @balance.deleter
    def balance(self):
        if self._balance != 0:
            raise AccountException("Cannot delete account: Balance is not zero.")
        print("Account balance attribute deleted.")
        del self._balance


# Create account
acc = BankAccount("IBAN12345", 0)

# 1. Setting the balance to 1000
acc.balance = 1000
print(f"Current Balance: {acc.balance}")

# 2. Trying to set the balance to -200
try:
    acc.balance = -200
except AccountException as e:
    print(f"Error: {e}")

# 3. Trying to set a new value for the account number
try:
    acc.account_number = "NEW_NUMBER_99"
except AccountException as e:
    print(f"Error: {e}")

# 4. Trying to deposit 1,000,000
try:
    # Adding 1 million to current balance
    acc.balance += 1000000 
    print(f"New Balance: {acc.balance}")
except AccountException as e:
    print(f"Error: {e}")

# 5. Trying to delete the account attribute with a non-zero balance
try:
    del acc.balance
except AccountException as e:
    print(f"Error: {e}")

# Final Step: Zero it out and then delete
acc.balance = 0
del acc.balance