s=input()
a=['Nil','Un','Bi','Tri','Quad','Pent','Hex','Sept','Oct','Enn']
b=['nil','un','bi','tri','quad','pent','hex','sept','oct','enn']
c=['nilium','unium','bium','trium','quadium','pentium','hexium','septium','octium','ennium']
t=a[int(s[0])]+b[int(s[1])]+c[int(s[2])]
t=t.replace('nnn','nn')
print(t)