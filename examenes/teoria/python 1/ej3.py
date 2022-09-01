v = "aeiou"
c = "tbpcñ"

t = input("_____t1_____: ")

r = ""
for m in t:
    e = m in v
    p = v.find(m)
    r += m
    r = r.replace(c[p] * e, "")

print(r) 