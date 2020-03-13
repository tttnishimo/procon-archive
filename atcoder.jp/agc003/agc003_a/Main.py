ss = input()
n = 1
w = 1
s = 1
e = 1

if "N" in ss:
  n = -1
if "W" in ss:
  w = -1
if "S" in ss:
  s = -1
if "E" in ss:
  e = -1
if n*s + w*e > 0:
  print("Yes")
else:
  print("No")