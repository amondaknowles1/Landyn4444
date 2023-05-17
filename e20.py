suru=int(input("请输入一个整数:"))
jisu=1
while jisu!=suru-1:
    jisu+=1
    if suru%jisu==0:
        print("不是素数")
        break
    else:
        continue
else:
    print("素数")