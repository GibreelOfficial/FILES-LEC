#user entry
total_bill_value=int(input("Enter the total bill value: "))

#discount computation
if total_bill_value>=7500 <12000:
    discount=(0.05*total_bill_value)
    bill_after_discount=total_bill_value-discount
    print(f"your bill is {bill_after_discount}")
else :
    total_bill_value>=12000
    discount=(0.07*total_bill_value)
    bill_after_discount=total_bill_value-discount
    print(f"your bill is {bill_after_discount}")
    