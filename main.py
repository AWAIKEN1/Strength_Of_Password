password = input("Enter new password: ")

result = {}

# first condition is password should be 8 characters or longer
# going to have separate if/elif blocks for each of the 3 conditions
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# Second condition: checking if number is in password.
# If one iteration is a digit then it will return True
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["number"] = digit


# Third condition: checking if an uppercase letter is in password.
# isupper() method would return false if we gave it a string with only 1 uppercase letter.
# We want this to be true. Hence have to iterate through it.
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase


# print(result)
if (all(result)):
    print("Strong Password")
else:
    print("Weak Password")
