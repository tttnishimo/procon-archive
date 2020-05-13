n = int(input())
ans_a = 0
ans = 0
for i in range(n):
  a,b = map(int,input().split())
  if a > ans_a:
    ans_a = a
    ans = a+b
print(ans)