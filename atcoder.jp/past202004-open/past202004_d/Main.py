s=input()
ans={}
al='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
  if al[i] in s:
    ans[al[i]]=1
    ans['.']=1
  for j in range(26):
    if al[i]+al[j] in s:
      ans[al[i]+al[j]]=1
      ans[al[i]+'.']=1
      ans['.'+al[j]]=1
      ans['.'+'.']=1
    for k in range(26):
      if al[i]+al[j]+al[k] in s:
        ans[al[i]+al[j]+al[k]]=1
        ans[al[i]+'.'+'.']=1
        ans[al[i]+'.'+al[k]]=1
        ans[al[i]+al[j]+'.']=1
        ans['.'+'.'+'.']=1
        ans['.'+al[j]+'.']=1
        ans['.'+'.'+al[k]]=1
        ans['.'+al[j]+al[k]]=1
print(len(ans))