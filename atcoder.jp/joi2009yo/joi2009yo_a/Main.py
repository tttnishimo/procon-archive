a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a_tmp = a[3]*3600 + a[4]*60 + a[5] - a[0]*3600 - a[1]*60 - a[2]
b_tmp = b[3]*3600 + b[4]*60 + b[5] - b[0]*3600 - b[1]*60 - b[2]
c_tmp = c[3]*3600 + c[4]*60 + c[5] - c[0]*3600 - c[1]*60 - c[2]
print(a_tmp//3600, a_tmp%3600//60, a_tmp%60)
print(b_tmp//3600, b_tmp%3600//60, b_tmp%60)
print(c_tmp//3600, c_tmp%3600//60, c_tmp%60)