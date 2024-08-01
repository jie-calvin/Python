def MergeSort(llist):      #归并排序
    length=len(llist)
    
    if length<=1:
        return llist
    
    x=length//2
    list_left=MergeSort(llist[:x])
    list_right=MergeSort(llist[x:])

    q,p,list_s=0,0,list()
    while q<len(list_left) and p<len(list_right):
        if list_left[q] <= list_right[p]:
            list_s.append(list_left[q])
            q+=1
        else:
            list_s.append(list_right[p])
            p+=1
            
    list_s+=list_left[q:]
    list_s+=list_right[p:]
    return list_s

w=int(input("请输入w值："))
n=int(input("请输入点的个数："))
point=[[0]*n]*n
for i in range(n):
    point[i]=input("输入点的坐标（用,隔开）：").split(",")
    point[i]=[int(j) for j in point[i]]
point_x=[]
for i in range(len(point)):
    point_x.append(point[i][0])
point_x=MergeSort(point_x)
x0=-1
cnt=0
for i in range(len(point_x)):
    if point_x[i]>x0:
        cnt+=1
        x0=point_x[i]+w
print(cnt)
