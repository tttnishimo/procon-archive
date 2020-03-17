n,k,m = map(int, input().split())
a = list(map(int, input().split()))
tmp = m * n - sum(a)
if tmp > k:
    print(-1)
elif tmp < 0:
    print(0)
else:
    print(tmp)