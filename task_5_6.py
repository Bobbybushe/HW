mass=[9,1,2,3,1,4,5,6,1,7,8,9]
k=0
for i in range(len(mass)-1):
    if mass[i]<mass[i+1]:
        k+=1
print('участков монотонного возрастания =',k)