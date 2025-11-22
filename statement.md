Project Specification: Cafe Order System
1. Problem Statement
The goal of this project is to create a simple, accessible, and resilient mechanism for simulating basic sales transactions. Many introductory programming examples fail to adequately demonstrate robust input handling (validation and error checking) alongside core transactional logic (state management and calculation). This project addresses the need for a minimalistic, self-contained educational resource that clearly illustrates transaction processing and state management using only standard Python libraries.

2. Scope of the Project
The project is strictly limited to developing a Command-Line Interface (CLI) application that simulates the order processing phase of a small cafe.

 Inclusions (In Scope)
Order Transaction Logic: Accurate calculation of item costs and management of the running total.

-> Input Validation: Handling of invalid input types (non-numeric quantities) and invalid data (non-menu items, non-positive quantities).

-> Static Data: The menu and prices are defined internally within a dictionary.

-> User Interface: Text-based input and output within the terminal.

 Exclusions (Out of Scope)
-> Persistence: No use of databases, files, or external storage to save order history or sales data.

-> External Dependencies: No use of third-party libraries; restricted to the Python Standard Library.

-> Advanced Features: No implementation of complex features like discounts, tax calculation, or inventory management.

3. Target Users
This system targets three primary user groups based on their goals:

-> Beginner Python Developers: Individuals learning core programming constructs like dictionaries, while loops, and try/except for error handling.

-> Educators/Students: Instructors and students needing a clean, practical example to demonstrate data flow and transactional integrity.

-> Utility Developers: Programmers seeking a minimal, non-database template for building simple transaction or ledger processors.

4. High-Level Features
The system provides the following primary functionalities to the end-user:

-> Menu Display: Clearly presents the available items and their prices upon application startup.

-> Interactive Ordering Loop: Allows the continuous input of items and quantities until the user enters the predefined exit command.

-> Real-time Cost Calculation: Immediately calculates the cost of the last added item and updates the overall running total.

-> Error Reporting: Provides clear, actionable, and user-friendly feedback when invalid items or quantities are entered.

-> Transaction Summary: Displays the final, calculated total amount upon exiting the ordering loop, concluding the transaction.
