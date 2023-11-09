import math  # Import the 'math' module for mathematical calculations

def main():
    print("Welcome to the Finance Calculator!")

    while True:
        print("\nWhich calculation do you wish to make:")
        print("\n1. Investment")
        print("2. Bond")
        choice = input("\nEnter '1' for Investment or '2' for Bond: ")


        if choice == '1':
            # Investment calculation
            investment_input = input("\nEnter the amount of money you are depositing: R")
            investment_input = investment_input.replace(" ", "")  # Remove spaces
            investment_amount = float(investment_input)  # Convert the input to a floating-point number

            interest_input = input("\nEnter the interest rate (%): ")
            interest_input = interest_input.replace(" ", "") # Remove spaces
            interest_rate = float(interest_input) / 100  # Convert the interest rate to a decimal

            years_input = input("\nEnter the number of years you plan on investing for: ")
            years_input = years_input.replace(" ", "") # Remove spaces
            years = int(years_input)  # Convert the number of years to an integer
            interest_type = input("\nWhich interest do you prefer:\n1. Simple interest\n2. Compound interest\n\nEnter '1' or '2': ").lower()

            if interest_type == '1':
                # Simple interest calculation
                final_amount = investment_amount * (1 + interest_rate * years)
            elif interest_type == '2':
                # Compound interest calculation
                final_amount = investment_amount * math.pow((1 + interest_rate), years)
            else:
                print("Invalid interest type. Please enter 'simple' or 'compound'.")
                continue  # Start over if the interest type is invalid

            print(f"Your investment will be worth: R{final_amount:.2f}")


        elif choice == '2':
            # Bond calculation
            present_value = float(input("Enter the present value of the house: R"))
            annual_interest_rate = float(input("Enter the annual interest rate: ")) / 100  # Convert interest rate to decimal
            numberOfYears = int(input("Enter the number of years for bond repayment: "))

            monthly_interest_rate = annual_interest_rate / 12  # Calculate the monthly interest rate
            repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -(numberOfYears*12)))

            print(f"Your monthly bond repayment will be: R{repayment:.2f}")

        else:
            print("Invalid choice. Please enter '1' for Investment or '2' for Bond.")
            continue  # Start over if the choice is invalid

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the Finance Calculator!")
            break  # Exit the program if the user doesn't want to perform another calculation

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
