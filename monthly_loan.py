annual_interest_rate = eval(input("Enter the annual interest rate :"))

number_of_years = eval(input("Enter number of years as an :"))

loan_amount = eval(input("Enter  loan amount :"))

monthly_interest_rate = (annual_interest_rate) / 1200

monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 / (1 + monthly_interest_rate)) ** (number_of_years * 12))

total_payment = monthly_payment * number_of_years * 12

# Display Result
print(f"The monthly payment is {monthly_payment}")
print(f"Total Payment will be {total_payment}")

