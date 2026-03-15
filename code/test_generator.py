import math
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

# for num in f:
#     print(num)
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()
    
pi=f'{math.pi:.3f}'
print(pi)

# 13. global、nonlocal（声明变量作用域）
x = 10


def global_test():
    global x
    x = 5
    return x


def nonlocal_test():
    count = 0

    def test2():
        nonlocal count
        count += 1
        return count

    return test2


num1 = global_test()
print(num1)
print(x)
print("---分割线---")
val = nonlocal_test()
print(val())
print(val())
print(val())