S=input()
A=[0]*26**2
for i in range(len(S)-1):
  A[(ord(S[i])-97)*26+ord(S[i+1])-97]+=1
a=A.index(max(A))
print(chr(a//26+97)+chr(a%26+97))