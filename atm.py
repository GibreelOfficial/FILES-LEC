# user data
PIN=str(123)
account_balance=100000
transaction_selection="0"

#Messages
invalid_pin="Invalid PIN !!! try again"
account_balance_insufficient="Insufficient balance"

#user verification & transaction
pin_entry=input("Enter your pin: ")
if PIN==pin_entry:
    print("SELECT TRANSACTION TYPE\n1) Deposit\n2) Withdraw\n3) Check balance")
    transaction_selection=int(input("Enter transaction selction: "))
    if transaction_selection ==1:
        deposit=int(input("Enter Deposit amount: "))
        if PIN==pin_entry:
            account_balance=(deposit+account_balance)
            print(f"Your new balance is {account_balance}")
        else:
            print(invalid_pin)
    elif transaction_selection == 2:
        withdraw_amount=int(input("Enter withdraw amount: "))
        if withdraw_amount>account_balance:
            print(account_balance_insufficient)
        else:
            pin_entry=input("Enter your pin: ")
            if PIN==pin_entry:
                account_balance=(account_balance-withdraw_amount)
                print(f"You have successfully withdrawn {withdraw_amount}\nYour remaining balance is {account_balance}")
            else:
                print(invalid_pin)
    elif transaction_selection==3:
        pin_entry=input("Enter your pin: ")
        if PIN==pin_entry:
            print(f"Your account balace is {account_balance}")
        else:
            print(invalid_pin)
        
else:
    print(invalid_pin)

