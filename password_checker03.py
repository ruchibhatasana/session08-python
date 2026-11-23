
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

masked_password = password[:2] + "*" * (len(password) - 4) + password[-2:]

print("Masked Password:", masked_password)


# OUTPUT 1:
# Enter your password: Tops@2026
# Password Length: 9
# First Character: T
# Last Character: 6
# Password Backwards: 6202@spoT
# Password Analysis:
# Digits: 4
# Uppercase Letters: 1
# Lowercase Letters: 3
# Special Characters: 1
# Password Strength: Strong
# Masked Password: To*****26


# OUTPUT 2:
# Enter your password: tops2026
# Password Length: 8
# First Character: t
# Last Character: 6
# Password Backwards: 6202spot
# Password Analysis:
# Digits: 4
# Uppercase Letters: 0
# Lowercase Letters: 4
# Special Characters: 0
# Password Strength: Medium
# Masked Password: to****26


# OUTPUT 3:
# Enter your password: abcde
# Password Length: 5
# First Character: a
# Last Character: e
# Password Backwards: edcba
# Password Analysis:
# Digits: 0
# Uppercase Letters: 0
# Lowercase Letters: 5
# Special Characters: 0
# Password Strength: Weak
# Masked Password: ab*de
