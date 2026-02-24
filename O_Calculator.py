expression = input()
for i in range(len(expression)):
    if expression[i] in "+-*/":
        operator_index = i
        operator = expression[i]
        break
A = int(expression[:operator_index])
B = int(expression[operator_index + 1:])
if operator == '+':
    result = A + B
elif operator == '-':
    result = A - B
elif operator == '*':
    result = A * B
elif operator == '/':
    result = A // B 

print(result)