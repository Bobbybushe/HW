arr=bytearray([1,24,3,4,5,6,7,19,9,30,154,12,13,18,12,16,1,18,4])
z=arr[0]
for i in range(len(arr)):
    if z<arr[i]:
        z=arr[i]
for i in range(len(arr)):
    if arr[i]%2==0:
        arr[i]=z
print(list(arr))