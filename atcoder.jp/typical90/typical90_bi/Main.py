deck=[]
for _ in range(int(input())):
  t,x=map(int,input().split())
  if t==1:
    deck.insert(0,x)
  elif t==2:
    deck.append(x)
  else:
    print(deck[x-1])