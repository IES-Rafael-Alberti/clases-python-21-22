ej = [("bli", "eal"),
      ("dckd c", "earain"),
      ("dabtodder", "iloopooso"),
      ("aoaproobreslasc", "mmifestodaosas "),
     ]

for t,u in ej:
    d = min(len(t), len(u))
    s, c, r = 1, 0, ""
    while c < d:
        r += t[c:c+s] + u[c:c+s]
        c += s
        s += 1

    print(r)  