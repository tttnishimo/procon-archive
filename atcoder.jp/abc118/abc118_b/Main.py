n,m = map(int, input().split())
arr = [0]*(m+1)
for i in range(n):
  s = list(map(int, input().split()))
  for j in range(1,s[0]+1):
    arr[s[j]] += 1
print(arr.count(n))