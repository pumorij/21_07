
l=[[4,5,3],[6,2,7],[3,2,1]]
res=[]
for i in range (0,len(l[0])):
    sum=0
    for j in range (0,len(l)):
        sum=sum+l[i][j]
    res.append(sum)

print(res)