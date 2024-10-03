class InsufficientBalanceError(Exception):
    """Custom exception raised when withdrawal amount exceeds the balance."""
    pass


class NegativeAmountError(Exception):
    """Custom exception raised when the entered amount is negative."""
    pass


def main():
    try:
        # Get account balance from the user
        balance = float(input("Enter your account balance: "))

        # Get withdrawal amount from the user
        withdrawal_amount = float(input("Enter the withdrawal amount: "))

        # Raise an exception if the withdrawal amount exceeds the balance
        if withdrawal_amount > balance:
            raise InsufficientBalanceError("Withdrawal amount exceeds the account balance.")

        # Raise an exception if a negative number is entered
        if withdrawal_amount < 0:
            raise NegativeAmountError("Withdrawal amount cannot be negative.")

        # If all checks pass, perform the withdrawal
        balance -= withdrawal_amount
        print(f"Withdrawal successful! New balance: {balance:.2f}")

    except ValueError:
        # Handle non-numeric input
        print("Invalid input! Please enter numeric values.")

