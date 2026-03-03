from collections import Counter

def solve():
    s,t = input(),input()
    cs = Counter(s)
    cnt = 0
    rmn = []
    for c in t:
        if c in cs and cs[c]:
            cs[c]-=1
            cnt += 1
        else: rmn.append(c)
    if cnt - len(s): return 'Impossible'
    rmn.sort()
    ns = len(s)
    nt = len(rmn)
    i_s = i_t = 0
    res = ''
    while i_s < ns and i_t < nt:
        if s[i_s] <= rmn[i_t]:
            res += s[i_s]
            i_s += 1
        else:
            res += rmn[i_t]
            i_t += 1
    while i_s < ns:
        res += s[i_s]
        i_s += 1
    while i_t < nt:
        res += rmn[i_t]
        i_t += 1
    return res

for _ in range(int(input())):
    print(solve())
