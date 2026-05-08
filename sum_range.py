def sum_to_n(n):
    suma = 0
    for num in range(1, n + 1):
        suma += num
    return suma


def sum_evens(n):
    suma = 0
    for num in range(2, n + 1,2):
        suma += num
    return suma

def factorial(n):
    fact=1
    for num in range(1,n+1):
        fact=fact*num
    return fact