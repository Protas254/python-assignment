
num_1 = int(input("Enter first value: "))
num_2 = int(input("Enter Second value: "))
op = input("Enter operation to perform[-,*,/, +, %]: ")

if op == '+':
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
    
elif  op == '-':
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result}")

elif op == '*':
    result = num_1 * num_2
    print(f"{num_1} X {num_2} = {result}")

elif op == '/':
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result}")

else:
    result = num_1 % num_2
    print(f"{num_1} % {num_2} = {result}")