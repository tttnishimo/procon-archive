x=int(input())
ans=x//11*2
if x%11==0:
  print(ans)
elif x%11<=6:
  print(ans+1)
else:
  print(ans+2)