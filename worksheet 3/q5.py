def unique_list(L):
    nl = []
    for x in L:
        if x not in nl:
            nl.append(x)
    return nl

print(unique_list([1,2,2,3,4,4,5]))
