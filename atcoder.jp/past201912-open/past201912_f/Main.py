s = input()
tmp = 0
flg = 0
arr = []
res = ''
for i in range(len(s)):
  if s[i].isupper() and flg == 0:
    tmp = i
    flg = 1
  elif s[i].isupper() and flg == 1:
    arr.append(s[tmp:i+1].lower())
    flg = 0
arr.sort()
for i in range(len(arr)):
  arr[i] = arr[i][0].upper()+arr[i][1:]
  arr[i] = arr[i][:-1] + arr[i][-1].upper()
  res += arr[i]
print(res)