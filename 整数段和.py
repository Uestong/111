print('仝稳的作业')
A,B = input().split()
A = int(A)
B = int(B)
count = 0
Sum = 0
#输出从A到B的所有整数
for i in range(A,B+1):
    count += 1
    Sum += i
    print('%5d'%i,end='')
    if count % 5 == 0:
        print()
#输出Sum的和
if count % 5 != 0:
    print()
    print('Sum = %d'%Sum)
else:
    print('Sum = %d' % Sum)
