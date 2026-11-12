n = int(input("Enter a positive integer: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of numbers from 1 to", n, "is:", sum)