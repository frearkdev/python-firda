# Opdracht 2
print(f"Aantal bananen: {3+3}") # - Calculates 3+3 and prints it in a sentence

# Opdracht 3
print(f"{3+5*8-3}") # - Calculates 3+5*8-3

# Opdracht 4 - Creating Variables

x = 20
y = "Freark"
print(x) # - Prints x integer
print(y) # - Prints x text

# Opdracht 4 - Get The Type
print(type(x)) # - Prints type of x
print(type(y)) # - Prints type of y

# Opdracht 4 - Multi Words Variable Names
myVariableName = "Freark"

print(myVariableName) # - Prints myVariableName text

my_variable_name = "Freark" # - Alternative way of writing multi word variable names

print(my_variable_name) # - Prints my_variable_name text

MyVariableName = "Freark" # - Alternative way of writing multi word variable names

print(MyVariableName) # - Prints MyVariableName text

# Opdracht 4 - Assign Multiple Values
a, b, c = "Orange", "Banana", "Cherry"

print(a) # - Prints orange
print(b) # - Prints Banana
print(c) # - Prints Cherry

# Opdracht 4 - Unpack a Collection
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x) # - Prints Apple
print(y) # - Prints Banana
print(z) # - Prints Cherry

# Opdracht 4 - Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # - Prints Python is awesome

# Opdracht 5 - User Input
print("Wat is je naam?")
name = input() # - Gets user input and stores it in variable name
print(f"Hallo {name}, leuk je te ontmoeten!") # - Prints Hallo {name},

# Opdracht 5 Extra - Validate Input

y = True
while y == True:
  x = input("Enter a number:") # - Gets user input and stores it in variable x
  try:
    x = float(x); # - Tries to convert x to a float
    y = False # - If successful, sets y to False to exit the loop
  except:
    print("Wrong input, please try again.") # - If unsuccessful, prints error message and loops again

print("Thank you!") # - Prints Thank you!