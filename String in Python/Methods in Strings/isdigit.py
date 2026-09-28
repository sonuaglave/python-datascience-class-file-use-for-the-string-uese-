# isdigit() checks whether a string contains only digits.

mobile = "9876543210"

print(mobile.isdigit())


pin = input("Enter your PIN: ")

if pin.isdigit():
    print("PIN contains only numbers")
else:
    print("PIN should contain only digits")