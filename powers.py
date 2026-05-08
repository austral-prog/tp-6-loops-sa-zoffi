

def power(base, exp):
    resul=1
    for num in range(exp):
        resul*=base
    return resul
def sum_of_powers(base, max_exp):
    total = 0
    for num in range(max_exp+1):
        total=total+power(base,num)
    return total
