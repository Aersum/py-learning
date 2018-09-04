def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a bancket.\n")
def milk_and_coffee(milk, coffee):
	print(f"Mixing {milk} milk and {coffee} coffee")	
#passing to the function numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#definition of variables
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#passing to the function variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#passing to the function math expressions
print("We acn even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#combining variants of passing
print("And we can combine the two, vriables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

milk_and_coffee(input("Milk amount? "), input("Coffee amount? "))

