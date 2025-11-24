Menu = {"Croissant": 70, "Frappe": 90, "Americano": 80, "Churro": 100, "Bagel": 150}

order = {} 

def order_cafe():
    amount_total = 0
    print(" Welcome to Flavor Haven! ")
    print("\n--- MENU ---")
    for item, price in Menu.items():
        print(f"| {item:<10} : Rs{price:>3} |")
    print("------------")
    print("Type 'stop' to finalize your order.")

    while True:
        user_input = input("\nWhat would you like to order? ")
        
        if user_input.lower() == 'stop':
            break
        elif user_input in Menu:
            try:
                serving = int(input(f"How many {user_input}s do you want? "))
                
                if serving > 0:
                    price = Menu[user_input] * serving
                    amount_total += price
                    print(f" Added {serving} **{user_input}** to your order.")
                    print(f"Item Cost: Rs{price}")
                else:
                    print(" Quantity must be a positive number.")
            except ValueError:
                print(" Unsupported quantity. Please enter a valid number.") 
        else:
            print(f" Oops, '{user_input}' is not on the menu. Please select from the list.")
            
        print(f"**Current Total:** Rs{amount_total}") 

    print("\n--- BILL ---")
    print(f"Your final total is: **Rs{amount_total}**")
    print("Thank you for dining with us! \nWe hope to see you again soon!\nHave a great day!")

if __name__ == "__main__":
    order_cafe()
