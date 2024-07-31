def sumscore(ops):
    sums=[]
    score=0
    for i in range(len(ops)):
        if len(ops[i])>1:
            num=""
            if ops[i][0]=="-":
                num+="-"
            elif not("0"<=ops[i][0]<="9"):
                return "输入有误操作"
            for j in range(1,len(ops[i])):
                if "0"<=ops[i][j]<="9":
                    num+=ops[i][j]
                else:
                    return "输入有误操作"
            sums.append(int(num))
        elif "0"<=ops[i]<="9":
            sums.append(int(ops[i]))
        elif ops[i]=="+":
            sums.append(sums[-1]+sums[-2])
        elif ops[i]=="D":
            sums.append(2*sums[-1])
        elif ops[i]=="C":
            sums.pop(-1)
        else:
            return "输入有误操作"
        print("每次操作后的数组：",sums)
    for i in range(len(sums)):
        score+=sums[i]
    return score
x=True
ops=[]
print("输入off为输入完成")
while x:
    a=str(input("请输入操作:"))
    if a=="off":
        x=False
    elif a=="":
        print("请勿输入空格")
    else:
        ops.append(a)
    print("已输入的操作：",ops)
score=sumscore(ops)
print("--------最后的总分是",score)
