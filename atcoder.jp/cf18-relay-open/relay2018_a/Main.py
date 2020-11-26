n=int(input())
w=['Sun','Sat','Fri','Thu','Wed','Tue','Mon']
for _ in range(n):
  print(w[w.index(input())-1])