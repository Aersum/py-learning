#number of cars
cars=100
#number of people you can put in one car
space_in_a_car=4.0
#number of drivers
drivers=30
#number of passengers
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car=passengers / cars_driven

print("There are", cars,"cars avaible")
print("There are only",drivers,"drivers avaible.")
print("There will be",cars_not_driven,"empty cars today")
print("We caan transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car")
