s1=list(map(str,input().split()))
s2=list(map(str,input().split()))
if s1[0] == s2[0]:
  print(abs(int(s1[1]) - int(s2[1]))//15)
else:
  print((int(s1[1]) + int(s2[1]))//15)