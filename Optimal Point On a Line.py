input()
a = [int(i) for i in input().split()]
a.sort(reverse=True)
n = len(a)
print(a[n//2])
