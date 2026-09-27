# start and end by user
# start to end print using while loop 

start = int(input("Enter first number = "))
end = int(input("Enter second number = "))
i = start

while i <= end:
    print(i, end=" ")
    i += 1
    
print(f"After while loop, start value is {start}")