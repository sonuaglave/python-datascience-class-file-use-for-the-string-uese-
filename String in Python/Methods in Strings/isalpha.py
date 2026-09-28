# isalpha() checks whether a string contains only letters (A–Z or a–z).
name = input("Enter your name: ")

if name.isalpha():
    print("Valid name")
else:
    print("Name should contain only letters")