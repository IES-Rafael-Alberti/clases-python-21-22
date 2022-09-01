ej = ["plingñtua",
      "clelactico",
      "tsiñn tuña",
      "pcpcpcpcpcdcppcbibbcbbcobsbbc tbocbdbcobcpbcodcbercocsco"]
v = "aeiou"
c = "tbpcñ"

#t = input("_____t1_____: ")
for t in ej:
    r = ""
    for m in t:
        e = m in v
        p = v.find(m)
        r += m
        r = r.replace(c[p] * e, "")

    print(r) 