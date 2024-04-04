expense_limit = 4
while True:
    individual_name = str(input("\nEnter individual's name. \n"))

    average_expend = 0
    total_expend = 0
    expense_count = 1
    while expense_count <= expense_limit:
        expense = str(input("Enter the expense: "))
        expenditure = int(input(f"Enter {expense} cost: "))

        total_expend += expenditure
        expense_count +=1
        average_expend = total_expend/expense_limit
    print(f"Hello, {individual_name} your Total expediture is $ {total_expend}  and your average expenditure is $ {average_expend}\n")

    user_feedbk = str(input("Do you have more individuals to enter? y/n: \n"))
    if user_feedbk.lower() == "y":
        continue
    else:
        break     