s = input()
tmp = ""
for i in range(len(s)):
  if s[i] == "1":
    tmp = tmp + "1"
  elif s[i] == "0":
    tmp = tmp + "0"
  elif s[i] == "B" and tmp =="":
    pass
  else:
    tmp = tmp[:-1]
print(tmp)