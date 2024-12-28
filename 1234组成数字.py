tar = [1, 2, 3, 4]
count = 0  # 结果计数
for i in range(len(tar)):
    x = str(tar.pop(i))  # 取出百位数字
    for j in range(len(tar)):
        y = str(tar.pop(j))  # 取出十位数字
        for k in range(len(tar)):
            print(x + y + str(tar[k]), end='  ')  #将百位十位和个位拼接，得到一个结果
            count += 1  #结果计数+1
        tar.insert(j, int(y))  # 将拿出的十位数字放回原始列表，防止影响下次循环
    tar.insert(i, int(x))  # 将拿出的百位数字放回原始列表，防止影响下次循环
    print('')  # 百位相同的结果显示为一行，百位数字改变的时候换行
print('最终结果为：%s个' % count)