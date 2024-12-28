'''
产生随机数  random.randint(start,end)
可以猜多次，直到才对了位置
如果猜错了给出提示
猜大了还是猜小了
'''
import random
ran = random.randint(1,100)
count = 0
print('猜数字游戏：')
while True:
    #进入猜数字环节 while循环
    guess = int(input('请输入您要猜的数字：'))
    count = count + 1
    if guess == ran:
        print('恭喜你猜对了')
        break
    elif guess > ran:
         print('猜大了')
    else :
        print('猜小了')
print('你一共猜了%d'% count)
#仝稳的作业