print( "If-Else statement")

x = 10
y = 5
print("If-Else Statement:")
if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

#If-Elif-Else statement"
number = 0

print("\nIf-Elif-Else Statement:")
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

print("While loop")
count = 0
while count < 5:
    print("\nWhile Loop Iteration:", count + 1)
    print("Count is still less than 5")
    count += 1

# For loop
print("\nFor Loop:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Looping through a string
print("\nLooping Through a String:")
for char in "Hello":
    print(char)

# Using range() in for loop
print("\nUsing range() in For Loop:")
for i in range(1, 6):
    print(i)

# Break statement
print("\nBreak Statement:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Continue statement
print("\nContinue Statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
