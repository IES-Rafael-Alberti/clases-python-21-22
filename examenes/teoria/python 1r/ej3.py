t = input("_____t1_____: ")
u = input("_____t2_____: ")

d = min(len(t), len(u))
s, c, r = 1, 0, ""
while c < d:
    r += t[c:c+s] + u[c:c+s]
    c += s
    s += 1

print(r)  