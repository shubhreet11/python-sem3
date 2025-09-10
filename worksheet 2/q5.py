D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

D[8] = 8.8
print(D)

del D[2]
print(D)

if 6 in D:
    print("YES")
else:
    print("NO")

c = 0
for k in D:
    c = c + 1
print("COUNT:", c)

s = 0
for k in D:
    s = s + D[k]
print("SUM:", s)

D[3] = 7.1
print(D)

D.clear()
print(D)
