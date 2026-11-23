
password = input("Enter your password: ")

print("Password Length:", len(password))
print("First Character:", password[0])
print("Last Character:", password[-1])
print("Password Backwards:", password[::-1])

digits = 0
uppercase = 0
lowercase = 0
special = 0

for char in password:
    if char.isdigit():
        digits += 1
    elif char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    else:
        special += 1

print("\nPassword Analysis:")
print("Digits:", digits)
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Special Characters:", special)

if len(password) >= 8 and digits >= 1 and uppercase >= 1 and lowercase >= 1 and special >= 1:
    strength = "Strong"
elif len(password) >= 6 and digits >= 1 and (uppercase >= 1 or lowercase >= 1):
    strength = "Medium"
else:
    strength = "Weak"

print("Password Strength:", strength)
