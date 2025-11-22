Project Title: Python Cafe Order
1. Overview of the Project:
The Python Cafe Order CLI is a minimal, self-contained application designed to simulate the core transactional logic of a simple Point-of-Sale (POS) system within the command line. Developed using procedural programming principles, it provides a clear example of how to manage a transaction state (the running total) and implement robust input validation using only the Python Standard Library. This project is an ideal learning tool for beginners focusing on control flow and error handling.
2. Features
The system is defined by its focus on functional integrity and simplicity:

Static Menu: The menu and prices are stored in a dedicated global dictionary (Menu).

Continuous Transaction Loop: Uses a while True loop to continuously accept orders until the user enters the 'stop' command.

Real-time Cost Management: The amount_total is updated immediately after each successful item entry, providing a running total.

Robust Input Validation:

Checks if the ordered item exists in the menu.

Uses a try-except ValueError block to ensure the quantity entered is a valid integer.

Ensures the quantity is a positive number (> 0).
3. Technologies/Tools Used
Component: Language, Data structure, I/O, Logic
Detail: Python 3.x, Dictionary (Menu), input() / print(), try...except
Purpose: Core programming language, Static data store for items and prices, Command-Line Interface (CLI) interaction, Error handling for non-numeric input.
4. Steps to Install & Run the Project
Since this project has zero external dependencies, installation is minimal.

Prerequisites
Python 3.x must be installed on your operating system.

Running the Application
-> Clone the Repository: (https://github.com/lavanyaa-06/flavor-haven-cafe)

Bash

git clone https://github.com/lavanyaa-06/python-cafe-order-cli.git
cd python-cafe-order-cli
-> Execute the Script:

Bash

python cafe_order.py
5. Instructions for Testing
To ensure the application is running correctly and its validation logic is sound, perform the following scenarios:

Successful Order Test: Order items that are on the menu and enter positive quantities. Type "stop" to finish. The final bill should correctly equal the sum of the prices.

Invalid Item Test: Type an item name that is not on the menu (e.g., "Muffin"). The system should print an error message and allow you to continue.

Invalid Quantity Test: Order a valid item, but enter zero (0), a negative number (e.g., -2), or text (e.g., "two") for the quantity. The system must print an error message and not crash.




<img width="390" height="204" alt="Screenshot 2025-11-23 013642" src="https://github.com/user-attachments/assets/5164d6a0-ee92-4549-8dd8-4aa8d9bb758a" />


<img width="393" height="193" alt="Screenshot 2025-11-23 013804" src="https://github.com/user-attachments/assets/71ea4634-adfb-4244-9057-a9b2d4a4a4e6" />


<img width="531" height="200" alt="Screenshot 2025-11-23 013834" src="https://github.com/user-attachments/assets/0ccd9526-2d49-4543-9969-56b64ef020a0" />



<img width="629" height="184" alt="Screenshot 2025-11-23 013902" src="https://github.com/user-attachments/assets/efa597a8-5928-43d8-a0f3-79afe2d90a39" />



<img width="621" height="204" alt="Screenshot 2025-11-23 013931" src="https://github.com/user-attachments/assets/5ead6650-90e7-402e-98e7-a8d0c29b5c91" />



<img width="449" height="158" alt="Screenshot 2025-11-23 014000" src="https://github.com/user-attachments/assets/c951afef-9c6e-46b5-8393-d363ebb9e788" />





   

 
