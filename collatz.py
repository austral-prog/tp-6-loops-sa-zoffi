def collatz_steps(n):
    count=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count=count+1
    return count


def collatz_sequence(n):
    lst=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        lst.append(n)
    return lst
