s = input()
arr = [0]*len(s)
tmp_r = 0
tmp_l = 0
flg = -1
for i in range(len(s)-1):
  if s[i:i+2] == 'RL':
    if flg != -1:
      arr[flg] += (tmp_l + 1)//2
      arr[flg+1] += tmp_l//2
      tmp_l = 0
    arr[i] = tmp_r//2 + 1
    arr[i+1] = (tmp_r+1)//2 + 1
    tmp_r = 0
    flg = i
  elif s[i] == 'R':
    tmp_r += 1
  elif s[i] == 'L':
    if s[i-1] == 'L':
      tmp_l += 1
if s[-2] == 'L':
  tmp_l += 1
arr[flg] += (tmp_l+1)//2
arr[flg+1] += tmp_l//2
print(*arr)