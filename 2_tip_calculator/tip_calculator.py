print("Welcome to the Tip Calculator.")
bill_amount = float(input("How much was your bill? $"))
tip_amount = int(input("What percentage tip would you like to give? %"))
amount_of_people = int(input("How many people to split the bill? "))
total = ((tip_amount) / 100 * (bill_amount) + (bill_amount) / (amount_of_people))
final_amount = round(total, 2)
print(f"Each person should pay: ${(final_amount)}")