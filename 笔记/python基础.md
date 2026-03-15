### 迭代器
1. 可迭代对象：实现了__iter__()方法的对象
2. 迭代器对象：实现了__iter__()和__next__()方法的对象称为迭代器对象
__iter__() 方法返回一个迭代器对象 __next__()方法从迭代器中返回下一个值，如果没有可返回值了，抛出StopIteration异常。可以使用next()函数来触发

```python
class MyIterator:
    def __init__(self, my_iterable):
        self.my_iterable = my_iterable
        self.index = 0  # 用于跟踪当前的位置

    def __iter__(self):
        return self  # 一般迭代器类的__iter__方法都返回self，因为自己就是迭代器对象

    def __next__(self):
        if self.index >= len(self.my_iterable.data_list):
            raise StopIteration  # 如果没有更多元素，则抛出StopIteration异常
        result = self.my_iterable.data_list[self.index]
        self.index += 1
        return result
    
my_list = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

# 等价于
numbers = [1, 2, 3, 4, 5] # numbers数组是一个可迭代对象，python中list，dict，tuple，set都是可迭代对象
numbers_iterator = iter(numbers) # 返回一个numbers专属的迭代器对象
while True:
    try:
        # 调用next获取下一个元素
        item = next(iterator)
        print(item)
    except StopIteration:
        # 没有更多元素时退出循环
        break
```

### 生成器
使用了 yield 的函数被称为生成器（generator）
yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器

函数执行到yield时会被返回
返回的是啥：当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回
和return的区别是啥：可以逐步产生并返回值(调用一次next()返回一次)，不用一次性返回所有结果。

生成器是迭代器，因此可以被for循环
例子：
```python
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

for num in f:
    print(num)
```

### 函数
不定长参数(魔法参数)
1. *args把传入的多余参数以元组的形式整合起来
2. **kwargs以字典的形式整合数据，所以需要制定key和value
匿名函数lambda：lambda [arg1 [,arg2,.....argn]]:expression
expression是对传入参数的操作，也是返回值

全局变量在函数外部定义，可以在整个文件中访问。
局部变量在函数内部定义，只能在函数内访问。
使用 global 可以在函数中修改全局变量。
使用 nonlocal 可以在嵌套函数中修改外部函数的变量。

### 装饰器
装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
装饰器的语法使用 @decorator_name 来应用在函数或方法上
格式：
```python
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
        
        result = original_function(*args, **kwargs)
        
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
        
        return result
    return wrapper

# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现
```

装饰器中的wrapper函数和原函数接收的参数一致，所以写成*args, **kwargs即可接收各种类型的参数，从而适配各种函数
装饰器也可以接收额外参数，例如：
```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```
Python 提供了一些内置的装饰器，例如：

@staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。
@classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）
@property: 将方法转换为属性，使其可以像属性一样访问

### 数据结构
https://www.runoob.com/python3/python3-data-structure.html

### 模块
将方法，类封装在一个py文件中，外部文件可以通过import引用
模块的搜索路径：当前目录->环境变量 PYTHONPATH 指定的目录->Python 标准库目录
每个模块都有一个 __name__ 属性。如果模块是被直接运行，__name__ 的值为 __main__。如果模块是被导入的，__name__ 的值为模块名。
所以可以：
```python
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

包：目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

### 异常处理
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
finally 语句无论是否发生异常都将执行最后的代码，在整个流程的最后
raise [Exception [, args [, traceback]]]

### 面向对象
常用类的方法
super():调用父类的方法
__init__():构造函数，在生成对象时调用
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值

### 正则表达式 re

### 协程与异步IO
python 用asyncio模拟协程 和线程不同，多个任务始终在一个线程，只是await一段IO(比如调用网络请求，llm api)的时候event loop切换到下一个可执行的任务，执行之后再执行当前任务
基本的执行流程：
```python
async def async_hello_world(i):
    await asyncio.sleep(i*5)
    print(f'1 current {i}', time.time() - now)
    print("Hello, world!")
    with open(f'./{i}.txt', 'w', encoding='utf-8') as f:
        f.write(f"Hello, world!{i}")

    return i

async def main():
    tasks=[]
    for i in range(1, 4):
        tasks.append(async_hello_world(i))
    results= await asyncio.gather(*tasks)
    print('results', results)
    print(type(results)) # list
    # await asyncio.gather(async_hello_world(), async_hello_world(), async_hello_world())

now = time.time()
# run 3 async_hello_world() coroutine concurrently
asyncio.run(main())
```
可以使用这个方法一次进行多次LLM调用，但要限制每秒或每分钟调用多少次api
如果把单次api调用改成一个多agent系统或者一个工作流，能可以吗？


注意代码规范
学会为函数写注释
学会为函数参数指定类型 利用
```python
from typing import Optional, List, Dict, Callable
```
Optional表示可选参数，使用后需要在函数内提供具体的条件控制
比如如果是None怎么处理，给出了实际值时该怎么处理

