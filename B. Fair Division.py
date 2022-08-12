len, t, ans = [], [], []
for i in range(0, int(input())):
    len.append(int(input()))
    t.append([int(x) for x in input().split()])

for i, j in enumerate(t):
    if(sum(j)%2 == 0):
        e = j.count(2)
        o = j.count(1)
        l = len[i]
        if((e%2 ==1 and o%2 == 0 and o != 0) or (e%2 == 0 and o%2 == 0)):
            ans.append("YES")
        else:
            ans.append("NO")

    else:
        ans.append("NO")

print(*ans, sep="\n")