def bin_add(a, b):
    return bin(a+b)[2:]
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

dec_sum = a+b
bin_sum = bin_add(a, b)

print(f"{bin_sum} ({a} + {b} = {dec_sum} in decimal or {bin_sum} in binary)")
