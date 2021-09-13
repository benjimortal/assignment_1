def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

a = 45
b = 345

print(f'The sum of {a} is:', sum_of_digits(45))
print(f'The sum of {b} is:', sum_of_digits(345))


