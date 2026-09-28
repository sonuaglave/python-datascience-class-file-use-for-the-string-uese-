# isalnum() checks whether a string contains only letters and/or numbers.
# It allows:

# ✅ A–Z
# ✅ a–z
# ✅ 0–9

# It does not allow:

# ❌ Space
# ❌ @
# ❌ #
# ❌ -
# ❌ _

# username = "Sudarshan123"

# print(username.isalnum())



product_code = input("Enter product code: ")

if product_code.isalnum():
    print("Valid product code")
else:
    print("Product code should contain only letters and numbers")
    
    