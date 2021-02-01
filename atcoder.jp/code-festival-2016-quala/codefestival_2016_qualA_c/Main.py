s=input()
k=int(input())
al='abcdefghijklmnopqrstuvwxyz'
a=[(26-al.index(s[i]))%26 for i in range(len(s))]
for i in range(len(s)):
  if a[i]<=k:
    k-=a[i]
    s=s[:i]+'a'+s[i+1:]
s=s[:-1]+al[al.index(s[-1])+k%26]
print(s)