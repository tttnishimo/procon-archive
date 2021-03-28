s=input()
t=[s[0]]
for i in range(1,len(s)):
  if s[i]<=t[-1]:
    t.append(s[i])
print(len(t))