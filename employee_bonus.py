salary=int(input("Enter your salary: "))
years_in_service=int(input("Enter years in service: "))

if years_in_service< 6:
    bonus=int(0.05*salary)
    net_bonus=bonus+salary
    print(f"Net bonus amount is {net_bonus}")
elif years_in_service>6 and years_in_service<=10:
     bonus=int(0.08*salary)
     net_bonus=bonus+salary
     print(f"Net bonus amount is {net_bonus}")
elif years_in_service>10:
     bonus=int(0.10*salary)
     net_bonus=bonus+salary
     print(f"Net bonus amount is {net_bonus}")