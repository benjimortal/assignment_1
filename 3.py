#3.	Write a Python function of to recursively calculate the sum
Data = [1, 2, [3,4], [5,6]]

def fact_list_sum(data):
    total = 0
    for x in data:
        if type([]) == type(x):
            total = total + fact_list_sum(x)
        else:
            total = total + x
    return total

print(f'The result after calculating the sum with recursion: \n{fact_list_sum(Data)}')