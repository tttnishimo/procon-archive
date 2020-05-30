s=input()
ans=''
for i in range(len(s)):
  if s[i] == '?':
    ans += 'D'
  else:
    ans += s[i]
print(ans)