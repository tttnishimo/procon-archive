arr = list(map(str, input().split()))
n = int(input())
for i in range(n):
  s = input()
  for j in range(len(arr)):
    flg = 1
    if len(arr[j]) == len(s):
      for k in range(len(arr[j])):
        if s[k] != arr[j][k] and s[k] != '*':
          flg = 0
      if flg == 1:
        arr[j] = '*' * len(s)
print(*arr)
