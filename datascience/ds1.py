# 1. Creating Strings
name = "Ron"
greetings = 'Hello, World'

print(name)
print(greetings)
print("---------------")
# 2. Multi-line Strings

sentence = """Welcome back
to my
Youtube Channel"""

print(sentence)
print("---------------")

# 3. Concatatenation (String + Variable String)
lname = "Capiral"

print("Hi my name is " + name + " Thankyou!")
print(greetings + " My name is " + lname)
print("---------------")

# 4. String Indexing and Slicing

word = "Python"

print(word[0])  # 1st letter
print(word[1])  # 2nd letter
print(word[2])
print(word[3])
print(word[-2])  # last 2nd letter since its negative
print(word[-1])  # last 1st letter

print(word[0:4])  # 0 is for starting and 2 is for before it
print(word[-4:-1])
# summary, the 1st number is the current placement, and also 2nd 2nd number if its negative, but if its positive, before the placement of it
