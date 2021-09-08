minutes = eval(input("Enter time in minutes:  "))

years = minutes // (365 * 60 * 24)

days = minutes // (24 * 60)

remaining_days = days % 365

print(f"{minutes} is equal to {years} years and {remaining_days} days")

