s = input()
alnum = alpha = digit = lower = upper = False
for i in range(len(s)):
    if s[i].isalnum() is True:
        alnum = True
    if s[i].isalpha() is True:
        alpha = True
    if s[i].isdigit() is True:
        digit = True
    if s[i].islower() is True:
        lower = True
    if s[i].isupper() is True:
        upper = True

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)
