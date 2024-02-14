# a program to determine selling price and profit margin

#given data
cost_price=int(input("Cost price: "))
transport_cost=int(input("Transport cost: "))

#computation
selling_price=cost_price+(0.05*cost_price)+(0.02*transport_cost)
profit_margin=(selling_price-cost_price)

#output
print(f"The selling price is {selling_price}\nThe profit margin is {profit_margin}")