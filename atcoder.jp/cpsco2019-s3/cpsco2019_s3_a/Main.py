s = input()
for i in range(len(s)):
  if s[i] == 'O':
    s = s[:i] + 'A' + s[i+1:]
  elif s[i] == 'A':
    s = s[:i] + 'O' + s[i+1:]
print(s)