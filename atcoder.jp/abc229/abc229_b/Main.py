S1,S2=map(str,input().split())
for i in range(min(len(S1),len(S2))):
  if int(S1[-i-1])+int(S2[-i-1])>9:
    print('Hard')
    exit()
print('Easy')