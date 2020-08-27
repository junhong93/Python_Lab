# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it


# Program to display the Fibonacci sequence up to n-th term

n = 0
n1 = 0
n2 = 1
while n < 51:
    n = n + 1
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(1)
    else:
        print(int((n-1) + (n-2)))
        n = n + 1
