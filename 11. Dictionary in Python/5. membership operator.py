student = {
    "name": "Rahul",
    "age": 25,
    "gender": "Male",
    "city": "Bhopal",
}

k = input("Enter key = ")

if k in student:
    print(student[k])
else:
    print("Key does not exists")