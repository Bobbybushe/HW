spis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16]
i = 0
k = 0
for i in range(len(spis)):
    if spis[i] % 2 == 0:
        k+=1
print(k)
#с while
spis_2 = [14, 15, 17, 2, 1, 4, 7, 100]
i2 = 0
k2 = 0
while i2 < len(spis_2):
    if spis_2[i2] % 2 == 0:
        k2+= 1
    i2+=1
print(k2)