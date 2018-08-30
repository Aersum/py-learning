name = "Zed A. Show"
age = 35 #not lie
my_height = 74 #inches
height = round(my_height * 2.54) #centimeters 
my_weight = 180 #lbs
weight = round(my_weight * 0.453592) #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line tricky, try to get it exactly right
total=age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
