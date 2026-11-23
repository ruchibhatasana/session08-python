
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
