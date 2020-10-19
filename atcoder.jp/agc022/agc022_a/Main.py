s=input()
al='abcdefghijklmnopqrstuvwxyz'
if len(s)<=25:
  al=list(al)
  for i in range(len(s)):
    al.remove(s[i])
  print(s+al[0])
elif s=='zyxwvutsrqponmlkjihgfedcba':
  print(-1)
else:
  flg=-1
  tmp=[]
  for i in range(25,-1,-1):
    if flg<al.index(s[i]):
      flg=al.index(s[i])
      tmp.append(flg)
    else:
      tmp.sort()
      for j in range(len(tmp)):
        if tmp[j]>al.index(s[i]):
          ans=tmp[j]
          break
      print(s[:i]+al[ans])
      break