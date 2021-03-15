s=input()
for i in range(len(s)):
  if (i%2==0 and s[i]==s[i].lower()) or (i%2==1 and s[i]==s[i].upper()):
    pass
  else:
    print('No')
    exit()
print('Yes')