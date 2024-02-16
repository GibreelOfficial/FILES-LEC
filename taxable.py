name=input("Enter your name: ")
hours_worked=int(input("Enter hours worked: "))

PAYRATE=30000
TAXABLE_INCOME_THRESHOLD=500000

#wage computation
wage=(PAYRATE*hours_worked)

#tax computation
if wage>TAXABLE_INCOME_THRESHOLD:
    tax=(0.1*wage)
    net_income=(wage-tax)
    print(f"Your Gross income is {wage}\nTax = {tax}\nNet income after tax= {net_income}")
else:
    print(f"Your Net income is {wage}")
 