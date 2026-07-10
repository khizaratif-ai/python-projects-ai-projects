psw = input("Enter your password: ")
result = {}
digit = False
Upper = False
strength = 0

if len(psw) >= 10:
    result["length"] = True
else:
    result["length"] = False
for char in psw:
    if char.isdigit():
        digit = True
result["digit"] = digit
for char in psw:
    if char.isupper():
        Upper = True
result["uppercase"] = Upper
print(result)

if all(result.values()) == True:
    print("strong password")
else:
    print("weak password")