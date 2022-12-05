import math # This is needed for checking square root

print("Hello World!")
print("It is time to do some Math!")
print("Note that this is Case-Sensetive.")
print(" ")

def withWhat_isnt_possible(): # This functions gets called if the withWhat variable isnt possible
    print("Either this feature isnt implemented or you wrote it wrong.")
    print("Console Calculator made by dotzSimplicity")
    print("This program has automatically exited.")
    exit()

def is_withWhat_square_root(): # This function r
    print(math.sqrt(num1))
    print("Console Calculator made by dotzSimplicity")
    exit()

possibleMath = ["Plus", "Times", "Division", "Minus", "Square Root"] # A List needed for a later.

num1 = int(input("First Number Please: ")) # Gets the First Number

withWhat = input("Plus, Times, Division or Minus, Square Root? ")

if withWhat != possibleMath: #This checks if withWhat is possible
    withWhat_isnt_possible()

if withWhat is "Square Root": #This checks if withWhat is "Square Root"
    is_withWhat_square_root()

num2 = int(input("Second Number Please: ")) # Gets the second number

if withWhat == "Plus":
    print(num1 + num2)
elif withWhat == "Times":
    print(num1 * num2)
elif withWhat == "Division":
    print(num1 / num2)
elif withWhat == "Minus":
    print(num1 - num2)

print("Console Calculator made by dotzSimplicity")


