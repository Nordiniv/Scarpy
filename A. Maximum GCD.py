from math import gcd
ns , mgcd = [], []
t = int(input())
for i in range(0, t if t<=100 else 100):
    ns.append(int(input()))
    mgcd.append(1)

for i, n in enumerate(ns):
    gcd_ = []
    for b in range(int(n/2), n+1, 1):
        for a in range(1, int(n/2)+1, 1):
            gcd_.append(gcd(a, b))
    mgcd[i] = max(gcd_)
    del gcd_

print(*mgcd, sep = "\n")