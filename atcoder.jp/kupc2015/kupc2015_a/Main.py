for _ in range(int(input())):
  S=input()
  ans=0
  t=''
  for s in S:
    t+=s
    if 'tokyo' in t or 'kyoto' in t:
      t=''
      ans+=1
  print(ans)