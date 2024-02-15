name=input("Enter your name: ")
hours_worked=int(input("Enter hours worked: "))

PAYRATE=30000
TAXABLE_INCOME_THRESHOLD=500000

#wage computation
wage=(PAYRATE*hours_worked)

#tax computation
if wage>TAXABLE_INCOME_THRESHOLD:
    print(f"\n{name} Your wage is shs {wage} \nYou are eligible to pay tax")
else:
    print(f"\n{name} Your wage is shs {wage} \nYou aren't eligible to pay tax")