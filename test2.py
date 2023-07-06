a = 99
b = 100
c = 250
d = 500

price = .87
price_01 = .80
price_02 = .70
price_03 = .50

message = "Hello new customer,"
company_name = "J&J construction"



if a <= a:
	print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${a * price}.")
	if b <= b:
		print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${b * price_01}.")
	if c <= c:
		print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${c * price_02}.")
	if d <= d:
		print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${d * price_03}.")	
	else:
		print(f"\nYour total cost is ${a * price}.")

#print(f"Hello new customer, welcome to {company_name.title()}! Your total cost is ${a * price}.") 
#print(f"Hello new customer, welcome to {company_name.title()}! Your total cost is ${b * price_01}.")