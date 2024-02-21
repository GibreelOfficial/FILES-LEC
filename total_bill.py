#user entry
total_bill_value=int(input("Enter the tota bill value: "))

#discount computation
if total_bill_value>=7500<12000:
    discount=(0.05*total_bill_value)
    new_bill=total_bill_value-discount
    print(f"your bill is {new_bill}")
elif total_bill_value>12000:
    discount=(0.07*total_bill_value)
    new_bill=total_bill_value-discount
    print(f"your bill is {new_bill}")
    