from functools import reduce

a = [55, 878, 596, 601, 170, 624, 904, 988, 98, 529, 646, 692, 556, 127, 794, 488]

result = reduce(lambda x, y: x+y, a)
print(f'The sum of list is: \n{result}')


