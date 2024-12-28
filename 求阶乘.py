def factorial(n):
    # 三元运算表达式
    return 1 if n < 2 else n * factorial(n - 1)
# 输入n的值
n = int(input())
print(factorial(n))
# 输出n的阶乘
#仝稳的作业
