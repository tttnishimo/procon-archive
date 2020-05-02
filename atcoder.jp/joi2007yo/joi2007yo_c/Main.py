s = input()
al = 'ZYXWVUTSRQPONMLKJIHGFEDCBAZYX'
for i in range(len(s)):
  s = s[:i] + al[al.index(s[i])+3] + s[i+1:]
print(s)