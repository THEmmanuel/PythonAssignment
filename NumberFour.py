#Author - THEmmanuel
count = 0
total = 0

# Continue asking the user for input
while True:
    # Asks the user to input an integer
    number = int(input("Please input a number: "))
    total += number

    # Breaks the operation when the user inputs 0
    if number == 0:
        print("Input was ZERO")
        break
    count = count + 1

# Calculates the average of all given integers
average = total / count
print("the average is ", average)

# Returns the sum of all integers
print("The sum of all numbers is ", total)
