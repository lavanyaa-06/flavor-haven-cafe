Project Overview:
This Python script, cafe_order.py, implements a basic Command-Line Interface (CLI) point-of-sale (POS) system for a small cafe. It enables a user to select items from a fixed menu, specify quantities, and calculates the running total until the order is concluded. This project serves as a clear demonstration of core Python programming concepts.

 Core Features:
Fixed Menu System: A static Python dictionary defines all available items and their corresponding prices.

Continuous Ordering: A main while loop allows customers to continuously add items to their order until a specific exit command ('stop') is entered.

Robust Input Validation:

The script validates that the item entered by the user is present in the menu.

It uses a try...except ValueError block to ensure the quantity entered is a valid, positive integer, preventing program crashes from invalid input.

Real-time Total: The accumulated cost is calculated and displayed to the user after every successful item addition, providing a running total.

 How to Run:
Prerequisites
You must have Python 3.x installed on your operating system.

Execution Steps
Clone the Repository:

Bash

git clone https://github.com/lavanyaa-06/flavor-haven-cafe.git
cd flavor-haven-cafe
Run the Script:

Bash

python cafe_order.py
Example Session
The program prompts for input and provides feedback after each entry.

Welcome to Flavor Haven!
...
Enter 'STOP' to complete the order.

-> Enter item name: Croissant
  -> Quantity for Croissant: 3
  Item added. Cost: Rs210
Current Outstanding Total: Rs210

-> Enter item name: stop

Order Complete!
Final Bill Total: Rs210
 Core Logic Description:
The ordering process is encapsulated within the main function (order_cafe or run_ordering_process), following these steps:

Initialization: The variable amount_total is set to zero (0).

Order Loop: An infinite while True loop initiates to continuously accept new orders.

Exit Condition: The loop is explicitly broken when the user enters 'stop'.

Menu Check: The user's input for the item name is validated against the keys of the static Menu dictionary.

Quantity Handling: If the item is valid, the user is prompted for the quantity (serving).

Error Prevention: A try-except structure manages any ValueError that may occur if the quantity input is not an integer, and ensures the quantity is greater than zero.

Calculation: If all checks pass, the item cost (Menu[item] * serving) is computed and added to the amount_total.

Output: The script prints the updated running total after processing each input.

Termination: Upon breaking the loop, a final summary message is printed, concluding the transaction.

 Contribution Guidelines:
We welcome suggestions and contributions! Please feel free to open an issue or submit a pull request for bug fixes or new features, such as:

Integration of sales tax.

Persistent storage for sales data.

Adding user-defined discounts.

Developed by [lavanyaa-06]# flavor-haven-cafe
A Python POS simulator featuring item validation, quantity handling, and continuous total calculation via command line.
