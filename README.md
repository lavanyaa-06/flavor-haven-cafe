Flavor Haven Cafe Order System Documentation

Project Title and Overview:
The project is the Flavor Haven Cafe Order System. This is a simple, command-line interface (CLI) application developed using Python 3.

Its primary objective is to accurately mimic the customer ordering process in a small cafe. The system handles displaying the menu, interactively accepting item selections and quantities, validating the user's input for correctness, and calculating the final bill total. It serves as a practical example of fundamental programming concepts like loops, dictionaries, and exception handling.

Key Features:
The application incorporates several core functionalities to manage transactions effectively:

-> Fixed Menu Definition: The available products and their fixed prices are defined and stored in the Menu dictionary.
-> Interactive Ordering Loop: The heart of the system is a continuous loop that accepts item input from the cashier until a specific termination command is given.
-> Running Total Calculation: A variable (amount_total) tracks and displays the cumulative cost of the order after each successful addition, providing real-time feedback.
-> Input Validation: The system is built to prevent common errors through various checks:
It ensures the selected item is actually available on the menu.
It uses try...except blocks to reject non-numeric characters for quantity input.
It enforces that the quantity entered must be a positive integer (greater than zero).
-> Final Bill Generation: The process concludes by summarizing the order and presenting the final calculated cost.

Technologies and Tools Used:
The system relies solely on core components of the Python language:

-> Programming Language: Python 3. All logic is written using standard Python syntax and functions.
-> Data Structure: The Dictionary is crucial for structuring the menu data, allowing for fast and efficient price lookups based on the item name.
-> Environment: The program runs entirely within the Command Line Interface (CLI), utilizing standard input (input()) and output (print()).

Steps to Install & Run the Project:
This is a single-file script requiring no dependencies outside of the standard Python environment.

1. Prerequisites
You must have Python 3 installed on your operating system (Windows, macOS, or Linux).

2. Setup
Save the provided Python code into a file named cafe_order.py.

3. Execution
-> Open Terminal: Launch your command prompt or terminal application.
-> Navigate: Use the cd command to move to the directory where you saved cafe_order.py.
-> Run: Execute the script using the Python interpreter:
Bash
python cafe_order.py
-> Interaction: The program will greet you, display the menu, and then begin prompting for item names.
   
Instructions for Testing:
Testing ensures the system's calculations are accurate and its error handling is robust.

1. Successful Calculation Test:
-> Goal: Verify that items are correctly priced and summed.                                                                -> -> Action: Order one Frappe (Rs90) and two Bagels (Rs150 each).                                                          -> - -> Expected Outcome: The final calculated total upon typing stop must be Rs390 (90 + (2*150)).

3. Invalid Item Test:
-> Goal: Ensure the system rejects items not on the Menu.
-> Action: When prompted, enter Latte or cookie.
-> Expected Outcome: The system should print an error message stating the item is not on the menu and continue the order loop without modifying the total.

4. Invalid Quantity (Non-Numeric) Test:
-> Goal: Test the try...except ValueError block.
-> Action: Order an item (e.g., Churro). When prompted for quantity, enter text like four or X.
-> Expected Outcome: The system must print the "Unsupported quantity" error and prevent the input from being processed, keeping the total unchanged.

5. Invalid Quantity (Zero/Negative) Test:
-> Goal: Test the positive integer validation.
-> Action: Order an item (e.g., Croissant). When prompted, enter 0 or -2.
-> Expected Outcome: The system must print the "Quantity must be a positive number" error and restart the item prompt, maintaining the total.

Flow of Execution:
The logic for the order_cafe() function follows a clear, iterative process.


<img width="390" height="204" alt="Screenshot 2025-11-23 013642" src="https://github.com/user-attachments/assets/5164d6a0-ee92-4549-8dd8-4aa8d9bb758a" />


<img width="393" height="193" alt="Screenshot 2025-11-23 013804" src="https://github.com/user-attachments/assets/71ea4634-adfb-4244-9057-a9b2d4a4a4e6" />


<img width="531" height="200" alt="Screenshot 2025-11-23 013834" src="https://github.com/user-attachments/assets/0ccd9526-2d49-4543-9969-56b64ef020a0" />



<img width="629" height="184" alt="Screenshot 2025-11-23 013902" src="https://github.com/user-attachments/assets/efa597a8-5928-43d8-a0f3-79afe2d90a39" />



<img width="621" height="204" alt="Screenshot 2025-11-23 013931" src="https://github.com/user-attachments/assets/5ead6650-90e7-402e-98e7-a8d0c29b5c91" />



<img width="449" height="158" alt="Screenshot 2025-11-23 014000" src="https://github.com/user-attachments/assets/c951afef-9c6e-46b5-8393-d363ebb9e788" />





   

 
