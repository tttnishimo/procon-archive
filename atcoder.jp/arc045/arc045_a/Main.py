s = input()
ans = []
for i in range(len(s)):
  if s[i] == 'L':
    ans.append('<')
  elif s[i] == 'R':
    ans.append('>')
  elif s[i] == 'A':
    ans.append('A')
print(*ans)