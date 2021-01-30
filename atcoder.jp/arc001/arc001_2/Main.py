a,b=map(int,input().split())
a=abs(a-b)
ans=a//10
a%=10
if a==0:
  print(ans)
elif a==1 or a==5:
  print(ans+1)
elif a==2 or a==4 or a==6 or a==9:
  print(ans+2)
else:
  print(ans+3)