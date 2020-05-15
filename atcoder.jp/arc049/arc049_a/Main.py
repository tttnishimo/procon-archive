s=input()
a=list(map(int, input().split()))
ans = ''
for i in range(len(s)):
  if i in a:
    ans += '"'
  ans += s[i]
if a[-1] == len(s):
  ans += '"'
print(ans)