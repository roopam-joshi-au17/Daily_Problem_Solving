print("WELCOME TO TIP CALCULATOR")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give ? 10,12 or 15? "))
people=int(input("How many people to split the bill ? "))
tip_percentage=tip/100
tip_amount=bill*tip_percentage
total_bill= tip_amount +bill
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"Each person shoulkd have pay: ${final_amount}")
