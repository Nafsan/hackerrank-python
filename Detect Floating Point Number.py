# for _ in range(int(input())):
#     string = input()
#     plus = string.count('+')
#     minus = string.count('-')
#     plus_minus = plus + minus
#     dot = string.count('.')
#     dot_index = string.find('.')
#     flag = 0
#     if plus_minus > 1:
#         flag = 1
#     elif string.isalpha() is True:
#         flag = 1
#     elif dot_index == len(string) - 1 or dot > 1 or dot < 1:
#         flag = 1
#     elif plus_minus == 0 or string[0] == '+' or string[0] == '-':
#         if dot == 1:
#             string = string.replace('.', '')
#         for i in range(plus_minus, len(string)):
#             if string[i].isnumeric() is True:
#                 flag = 0
#             else:
#                 flag = 1
#                 break
#     if flag == 0:
#         print(True)
#     else:
#         print(False)

for _ in range(int(input())):
    s = input()
    try:
        value = float(s)
        flag = 0
    except ValueError:
        flag = 1
    if flag ==0 and s.count('.') == 0:
        flag = 1
    if flag == 0:
        print(True)
    else:
        print(False)
