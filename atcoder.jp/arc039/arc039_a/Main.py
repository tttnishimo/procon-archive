a,b = map(int, input().split())
print(max(a - b, int('9' + str(a)[1:]) - b, int(str(a)[0] + '9' + str(a)[2]) - b, int(str(a)[:2] + '9') - b, a - int('1' + str(b)[1:]), a - int(str(b)[0] + '0' + str(b)[2]), a - int(str(b)[:2] + '0')))
