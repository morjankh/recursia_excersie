def fibonacci(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2) 


print(fibonacci(6))  


def find_subsets(lst):
    if not lst:
        return [[]] 
    else:
        subsets = find_subsets(lst[1:])  
        return subsets + [subset + [lst[0]] for subset in subsets]


print(find_subsets([1, 2])) 