#list program python

a=[290,30,48,79,234,]
max1=0
max2=0
max3=0
for i in (a):
    if i > max1:
        max3=max2
        max2=max1
        max1= i
    elif i > max2:
        max3=max2
        max2=i
    elif i > max3:
        max3=i
print(max3)
print(max2)
print(max1)