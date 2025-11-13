"""
Challenge 1: About Me
Instructions:
1. Create variables for your name, age, and favorite hobby.
2. Use an f-string to print something like:
3. Add 1 to your age in the print statement (to show your age next year).
"""
name = "Ron"
age = 22
hobby = 'Playing Games'

print(f"Hi! I'm {name}, I am {age} years old, and I love {hobby}")
"""
Challenge 2: Simple Calculator
Instructions:
1. Ask the user for two numbers (using input()).
2. Print their sum, difference, product, and average
"""
firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))
sum = firstnum + secondnum
diff = firstnum - secondnum
prod = firstnum * secondnum
ave = float((firstnum + secondnum) / 2)

print(f"Sum: {sum}")
print(f"Difference: {diff}")
print(f"Product: {prod}")
print(f"Average: {ave}")
"""
Challenge 3: String Magic
Instructions:
1. Create a string variable with the text "Python is fun!"
2. Print:
- The text in uppercase
- The first 6 letters only
- The text with "fun" replaced by "awesome"
"""
