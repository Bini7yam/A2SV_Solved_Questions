t = int(input())

def solve():
    n = int(input())
    s = input()
    ca,cb,cc=0,0,0
    arr = ['aa','aba','aca','abca','acba','abbacca','accabba']
    for t in arr:
        if t in s: return len(t)
    return -1

for _ in range(t):
    print(solve())


#aa
#a*a
#abbabbaccacca
#abcbaca
