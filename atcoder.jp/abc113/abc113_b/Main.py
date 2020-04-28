n = int(input())
t,a = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
  arr[i] = abs(t - arr[i] * 0.006 - a)
print(arr.index(min(arr))+1)