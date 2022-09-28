"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
middle = len(numbers)//2

if len(numbers) % 2 != 0:
    median = (numbers[middle])
else:
    median = (numbers[middle-1] + numbers[middle])/2

print(median)
