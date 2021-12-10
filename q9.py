a=[2,4,5,7,8,2]
i=0
even_list=[]
odd_list=[]
while (i<len(a)):
    if a[i]%2==0:
        even_list.append(a[i])
    else:
        odd_list.append(a[i])
    i=i+1
print(even_list)
print(odd_list)
#list even odd number program