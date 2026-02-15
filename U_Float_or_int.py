n = input()
if '.' in n:
    integer_part, decimal_part = n.split('.')
    if int(decimal_part) == 0:
        print("int", int(integer_part))
    else:
        print("float", int(integer_part), "0." + decimal_part)
else:
    print("int", int(n))
