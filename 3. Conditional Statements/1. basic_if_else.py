age = int(input("Enter your age = "))

if age >= 18:
    print("You can vote")
    print("You are elligible")
    print("You are responcible voter")
else:
    print("You can not vote")
    

physics = int(input("Enter your physics marks = "))
chem = int(input("Enter your chem marks = "))

if physics > 33 and chem > 33:
    print("Pass")
else:
    print("Fail")