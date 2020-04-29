s_1=list(map(int, input().split()))
s_2=list(map(int, input().split()))
s_3=list(map(int, input().split()))
s_4=list(map(int, input().split()))
flg = 0
for i in range(3):
  if s_1[i] == s_1[i+1] or s_2[i] == s_2[i+1] or s_3[i] == s_3[i+1] or s_4[i] == s_4[i+1]:
    flg = 1
  if s_1[i] == s_2[i] or s_2[i] == s_3[i] or s_3[i] == s_4[i]:
    flg = 1
if s_1[3] == s_2[3] or s_2[3] == s_3[3] or s_3[3] == s_4[3]:
  flg = 1
if flg == 1:
  print('CONTINUE')
else:
  print('GAMEOVER')