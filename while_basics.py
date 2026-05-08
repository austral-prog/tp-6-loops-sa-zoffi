def countdown(n):
    lst=[]
    while n>=0:
        lst.append(n)
        n=n-1
    return lst

def double_until(limit):
    lst=[]
    n=1
    while n<=limit:
        lst.append(n)
        n=n*2
    return lst