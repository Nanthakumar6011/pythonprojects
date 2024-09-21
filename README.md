Description of the Bank Password and Transaction System
This project is a simple Python-based banking system that allows users to deposit, withdraw, and check their bank balance by validating their credentials such as username, password, and UPI ID. The system simulates a basic bank operation with some input validation and conditional checks.

Features:
User Authentication:

Users are prompted to enter their username and password to access the system.
The password is verified based on a predefined user database (un_pass dictionary).
Deposit Functionality:

Users can deposit money into their account.
The amount entered is validated, and after a successful deposit, the new balance is updated and displayed.
Withdrawal Functionality:

Users can withdraw money from their account.
Before withdrawal, the system checks if the user has sufficient funds.
If the user has enough balance, the withdrawal is processed, and the updated balance is displayed.
Balance Check:

Users can check their current balance.
The system displays the balance after validating the user's UPI ID.
UPI Validation:

To ensure secure transactions, users need to enter their UPI ID for deposit, withdrawal, or balance check. The UPI ID is verified against the predefined list of valid UPI IDs (un_upi dictionary).
How It Works:
The program uses predefined dictionaries for user data (un_amt for balances, un_pass for passwords, and un_upi for UPI IDs).
Users interact with the system through a simple menu that offers:
Deposit
Withdraw
Check Balance
Exit
Based on the user’s choice, the program will perform the corresponding operation after validating the inputs.
The loop continues until the user selects the "Exit" option, terminating the session.
User Flow:
Login: The user provides a valid username and password. If these credentials match, they are granted access.
Deposit: The user can deposit an amount by providing the correct UPI ID. The system updates the user's balance.
Withdraw: The user can withdraw an amount if they have sufficient funds. After providing the correct UPI ID, the system deducts the amount and updates the balance.
Check Balance: The user can check their current balance by verifying their UPI ID.
Exit: The session ends when the user chooses to exit.
Key Concepts:
Dictionaries: The program uses dictionaries to store user data (balances, passwords, and UPI IDs).
Input Validation: Ensures that only valid inputs (username, password, UPI ID) are accepted before performing operations.
Conditional Logic: Determines if a transaction can proceed based on conditions like balance availability or valid UPI ID.

