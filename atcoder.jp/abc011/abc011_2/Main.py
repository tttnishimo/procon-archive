s = input()
for i in range(len(s)):
  if i == 0:
    s = s[0].upper() + s[1:]
  else:
    s = s[:i] + s[i].lower() + s[i+1:]
print(s)