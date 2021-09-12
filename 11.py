x=(int(input('Please enter the first positive digit:\n')))
y =(int(input('Please enter the second positive digit:\n')))

gcd = lambda m,n: m if not n else gcd(n,m%n)
print(f'The greatest common divisor of {x}, and {y} is:',gcd(x, y))