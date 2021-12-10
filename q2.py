a=[1,2,3,45,67,89,]
i=0
b=[]
while(i<len(a)):
    if a[i]%5==0:
        b.append(a[i])
    i=i+1
print(b)