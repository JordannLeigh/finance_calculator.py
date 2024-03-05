import math

# Create a calculator program that allows users to calculate investments or bonds
print("\nInvestment  - To calculate the amount of interest you'll earn on your investment.")
print("Bond        - To calculate the amount you'll have to pay on a home loan.")

# Ask user to select either bond or investment - keep asking for input until condition is met
while True:
    new_input = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
    if new_input.lower() == "bond" or new_input.lower() == "investment":
        print("You have selected:", new_input.lower())
        print(f"\nLet's calculate your {new_input.lower()}")
        break
    else:
        print("Error, invalid input.")
        continue

# If investment, ask user to input relevant info and select a form of interest
# Calculate and output answer based on inputs and interest selection
if new_input.lower() == "investment":
    while True:
        try:
            print("\nPlease do not include any special characters in this answer!")
            p = int(input("Initial deposit amount: "))
            r = float(input("Interest rate: ")) / 100 # Divide by 100 to convert % to decimal
            t = int(input("Investment duration in years: "))
            break
        except ValueError:
            print("Error: Please enter a valid integer with no special characters.")

    while True:
        interest_type = input("\nPlease type either 'simple' or 'compound' to select your interest type: ")
        if interest_type.lower() == "simple":
            result_s = round(p * (1 + r * t), 2) # Round to two decimal places
            print(f"\nYour total amount after interest: £{result_s}.\nThank you for using our service.")
            break
        elif interest_type.lower() == "compound":
            result_c = round(p * math.pow((1 + r), t), 2) # Round to two decimal places
            print(f"\nYour total amount after interest: £{result_c}.\nThank you for using our service.")
            break
        else:
            print("Error, invalid input.")

# If bond, ask user to input relevant info
# Calculate and output answer based on inputs
elif new_input.lower() == "bond":
    while True:
        try:
            print("\nPlease do not include any special characters in this answer!")
            p = int(input("Present value of the house: "))
            i = float(input("Interest rate: ")) / 100 / 12 # Convert annual interest to monthly
            n = int(input("Repayment duration in months: "))
            break
        except ValueError:
            print("Error: Please enter a valid integer with no special characters.")

    try:
        result_b = round((i * p) / (1 - (1 + i) ** (-n)), 2) # Round to two decimal places
        print(f"\nYour monthly bond payments will be: £{result_b}.\nThank you for using our service.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
