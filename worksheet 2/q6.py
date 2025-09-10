S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}

# (1)
S1.add(55)
S1.add(66)
print(S1)

# (2)
S1.remove(10)
S1.remove(30)
print(S1)

# (3)
if 40 in S1:
    print("YES")
else:
    print("NO")

# (4)
print(S1 | S2)

# (5)
print(S1 & S2)

# (6)
print(S1 - S2)
