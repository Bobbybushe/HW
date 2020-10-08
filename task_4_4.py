spis=[1, 3, 4, 65, 324, 123, 111]
for i in range(1):
    spis.append(spis.pop(0))
print(spis)
#c while
spis_2=[123,3223, 12, 2, 11, 17]
i2=0
while i2<=len(spis_2):
    i2+=1
    spis_2.append((spis_2.pop(0)))
print(spis_2)
