#program to calculate weekly pay

#manager
manager_pay=20000

#hourly workers
hourly_worker_pay=300
duty_time=40

#commission workers
commission_workers_fixed_pay=250

#piece workers
piece_worker_pay=200

#Employee code menu
print("SELECT EMPLOYEE CODE\n1) Managers\n2) Hourly worker\n3) Comission worker\n4) Piece worker")
employee_code=int(input("Enter your employee code: "))

#conditions
if employee_code==1:
    print(f"Your weekly pay is ${manager_pay}")
elif employee_code==2:
    total_hours_worked=float(input("Hours worked: "))
    if total_hours_worked<=duty_time:
        print(f"Your weekly pay is ${total_hours_worked*hourly_worker_pay}")
    else:
        total_hours_worked>duty_time
        over_time_wage=(1.5*hourly_worker_pay)
        over_time_hours=(total_hours_worked-duty_time)
        over_time_pay=(over_time_wage*over_time_hours)
        duty_time_pay=(duty_time*hourly_worker_pay)
        print(f"Your weekly pay is ${over_time_pay+duty_time_pay}")
elif employee_code==3:
    gross_weekly_sales=int(input("Enter weekly sales: "))
    print(f"Your weekly pay is ${commission_workers_fixed_pay+(0.057*gross_weekly_sales)}")
elif employee_code==4:
    number_of_items_produced=int(input("Enter Number of items produced: "))
    print(f"Your weekly pay is ${piece_worker_pay*number_of_items_produced}")