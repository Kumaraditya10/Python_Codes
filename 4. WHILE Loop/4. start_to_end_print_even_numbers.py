# start to end print even numbers

start = int(input("Enter first number = "))
end = int(input("Enter second number = "))
i = start

while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1