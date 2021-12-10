x=[[8,5,1],[9,3,2],[4,6,3]]
y=[[8,5,3],[9,5,7],[9,4,1]]
b=[]
for i in range(len(x)):
    for j in range(len(x[i])):
        b.append([x[i][j]])
print(b)
s=[]
for i in range(len(y)):
    for j in range(len(y[i])):
        s.append([y[i][j]])
print(s)
k=[]
for i in range(len(x)):
    for j in range(len(x[i])):
        k.append([x[i][j]]+[y[i][j]])
print(k)
#list magic score program