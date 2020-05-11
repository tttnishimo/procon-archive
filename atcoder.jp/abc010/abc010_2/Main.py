n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
  if i == 1 or i == 3 or i == 7 or i == 9:
    pass
  elif i == 2 or i == 4 or i == 8:
    ans += 1
  elif i == 5:
    ans += 2
  else:
    ans += 3
print(ans)