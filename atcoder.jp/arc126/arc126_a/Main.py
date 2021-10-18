for _ in range(int(input())):
  a,b,c=map(int,input().split())
  b//=2
  ans=0
  if b<=c:
    ans+=b
    c-=b
    b=0
  else:
    ans+=c
    b-=c
    c=0
    if b*2<=a:
      ans+=b
      a-=b*2
      b=0
    else:
      ans+=a//2
      a=0
  if c//2<=a:
    ans+=c//2
    a-=c//2
    c=c%2
    if c==1 and a>2:
      ans+=1
      a-=3
    ans+=a//5
    a=0
  else:
    ans+=a
    a=0
  print(ans)