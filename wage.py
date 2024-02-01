employee_name= input("Enter your name: ")
PAYRATE=30000
hours_worked= input("Enter hours worked: ")

#computation
wage=(PAYRATE*int(hours_worked))
allowance=(0.05*wage)
gross_wage=(wage+allowance)
tax=(0.05*gross_wage)
net_wage=(gross_wage-tax)


print(f"\nyour wage is: {int(wage)}\nYour allowance is: {int(allowance)}\nYour gross wage is: {int(gross_wage)}\nYour tax is: {int(tax)}\nYour net wage is: {int(net_wage)}")