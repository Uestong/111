print("仝稳的作业")
n = int(input())
friend = set()          # 创建空集合
for i in range(n):
    s = input().split()
    if int(s[0]) != 1:
        friend.update(s)        # 用update方法添加列表到集合里
m = int(input())
all_f = input().split()
f_ed = {}           # 这里要用字典，不能用列表，不然会超时。
flag = True
for i in all_f:
    if i not in friend and i not in f_ed:
        f_ed[i] = 1
        if flag:
            print(i, end="")
        else:
            print("", i, end="")
        flag = False
if flag:
    print("No one is handsome")