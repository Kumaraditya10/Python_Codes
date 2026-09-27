# print start to end, numbers which are divisble by 3 and 4

start = int(input("Enter first number = "))
end = int(input("Enter second number = "))

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
    i += 1