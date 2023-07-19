def solution(roman):
    s, last_number = 0, 0 # s - конечное переделанное число
    slovar_alf = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    slovar_value = [1, 5, 10, 50, 100, 500, 1000]
    for i in roman:
        s+=slovar_value[slovar_alf.index(i)]
        if slovar_value[slovar_alf.index(i)]>last_number:
            s=s-2*last_number
        last_number=slovar_value[slovar_alf.index(i)]
    return s

with open('24-2z')as f:
    s=f.readline()
    s=s.split()
    k,m=1,-10 #k - это длина последовательности,m- будем отдавать туда максимальную длину последовательности
    for x in range(0,len(s)-1):
        if solution(s[x])<solution(s[x+1]):
            k+=1
            m=max(m,k)
        else:
            k=1
print(m)
