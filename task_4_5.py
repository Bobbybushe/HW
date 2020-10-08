st=[1,1]
step=input('Введите длинну списка чисел')
i=0
for i in range(int(step)):
    st.append(st[i]+st[i+1])
print(st)