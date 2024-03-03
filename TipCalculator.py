print("Welcome to the tip calculator!")
a=float(input("What was the total bill? $"))
b=int(input("How much tip would you like to give? , 10,12, or 15?"))
c=int(input("How many people to spilt the bill?"))
total_bill_with_tip=float(a +b/100*a)
print(total_bill_with_tip)
total_tip=total_bill_with_tip - a
print(total_tip)
per_person_bill=a/c + total_tip/c
n_per_person_bill=round(per_person_bill,2)
print(f"Each person should pay: ${n_per_person_bill}")




