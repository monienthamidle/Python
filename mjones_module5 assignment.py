message = "Hello new customer,"
company_name = "J&J construction"

#when you change square_foot it will run the below if statements and execute them, based on square_foot the appropriate print function will be printed.
square_foot = 90


if square_foot >= 500:
	price = .50
	print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${square_foot * price}.")
elif square_foot >= 250:
	price = .70
	print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${square_foot * price}.")
elif square_foot >= 100:
	price = .80
	print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${square_foot * price}.")

else:
	print(f"\nHello new customer, welcome to {company_name.title()}! Your total cost is ${square_foot * 0.87}.")


#This price is based on your {square_foot} square feet with a ${price} discount.
#print(f"Hello new customer, welcome to {company_name.title()}! Your total cost is ${price * square_foot}.") 


# module 3 need to continue to add onto project 
		