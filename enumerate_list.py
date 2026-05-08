def enumerate_list(lst):
    nlist=[]
    index=0
    for valor in lst:
        if valor!="":
            nlist.append(str(index)+". "+ valor)
            index=index+1
    return nlist


def enumerate_backwards(lst):
    nlist=[]
    index=0
    for valor in lst:
        if valor!="":
            nlist.append(str(index)+". "+valor[::-1])
            index=index+1
    return nlist