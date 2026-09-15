s = 0
q = 0
for i in range(1,501):
    if i % 3 == 0 and i % 2 != 0:
        print(i)
        s += i
        q += 1
print(s)
print(q)