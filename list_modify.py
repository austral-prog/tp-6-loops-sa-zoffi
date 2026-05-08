def put(value, lst):
    found_index=-1
    i=0
    while i<len(lst) and found_index==-1:
        if lst[i]=="":
            lst[i]=value
            found_index=i
        i=i+1
    return found_index


def remove(value, lst):
    elim=0
    i=0
    while i<len(lst):
        if lst[i]==value:
            lst[i]=""
            elim=elim+1
        i=i+1
    return elim