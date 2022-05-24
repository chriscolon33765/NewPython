



print("Welcome to the tip calculator!")
bill_amount = float(input("What was your total bill? $\n"))
tip_amount = int(input("What percentage of tip would you like to leave? 10, 12 or 15? \n"))
split_amount = int(input("How many people are splitting this bill? \n"))
bill_with_tip = tip_amount / 100 * bill_amount + bill_amount
bill_per_person = bill_with_tip / split_amount
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")





