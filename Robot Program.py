t = int(input())

def f0(k, s):
    cnt = 0
    for i in range(len(s)):
        cnt += s[i]=='R'
        cnt -= s[i]=='L'
        if not cnt:
            return k // (i+1)
    return 0
for _ in range(t):
    n, x, k = [int(i) for i in input().split()]
    s = input()
    res = 0
    for c in s:
        x += c=='R'
        x -= c=='L'
        k -= 1
        if not x:
            res = 1 + f0(k,s)
            break
        if not k: break
    print(res)
