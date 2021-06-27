A,B,C,D=map(int,input().split())
if C*D-B<=0:
  print(-1)
else:
  print(-(-A//(C*D-B)))