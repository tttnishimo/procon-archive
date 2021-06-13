A,B,C=map(int,input().split())
coin=0
for i in range(C):
  coin+=A
  if i%7==6:
    coin+=B
  if coin>=C:
    print(i+1)
    exit()