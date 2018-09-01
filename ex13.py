from sys import argv
#read thr WYSS section for how to run this
script, name, surname, age = argv

print("The script is called:", script)
print(f"So, {name} {surname}. You're {age} years old.")
vehicle = input("Tell me what is your favorite vehicle? ")
print("{} is good thing".format(vehicle))
