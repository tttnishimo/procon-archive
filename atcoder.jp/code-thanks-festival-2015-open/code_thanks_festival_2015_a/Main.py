a=int(input())
b=int(input())
if a*b>0:
  print(max(abs(a),abs(b))*2)
else:
  print((abs(a)+abs(b))*2)