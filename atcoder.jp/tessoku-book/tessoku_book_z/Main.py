ans=['Yes']*300001
for i in range(2,300001):
  for j in range(2,300000//i+1):
    ans[i*j]='No'
for _ in range(int(input())):
  print(ans[int(input())])