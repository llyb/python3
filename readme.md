### 一、变量

* print中用加号连接字符串和变量
* python中的变量直接定义赋值即可

```python
character_name = "John"
character_age = "35"

print("There was a man named " + character_name + "and he is " + character_age + "years old.")
```

### 二、字符串

* "" 表示字符串，换行在里面使用"\n"，特殊字符要进行转义，同样可以使用[]取值

```python
# 一些字符串处理函数
phrase = "Giraffe Academy"
print(phrase + " is cool")

print(phrase.lower())
len(phrase) # 求字符串长度
phrase.index('fesrf') #该字符串在原串中第一次出现的位置，如果没有会报错
# 注意并没有改变phrase的值，即phrase和原来的值还是一样的
phrase.upper() # 将字符串转换乘大写字母
phrase.lower() # 将字符串转换乘小写字母
phrase.replace(phrase, "elephant") # 用后面的字符串替换前面的字符串
```

### 三、数字

```python
# 和c++不同，python中的取模没有负数

# 数字转化成字符串
my_num = 5
print(str(my_num) + " is my favorite number")
# 取绝对值
abs(my_num)
# 指数
pow(底数，指数)
# 比较大小
max(), min()
# 四舍五入函数，注意同样不会改变原数的值
round(my_num)
# 引入头文件，和c++中的math基本一致
from math import *
```

### 四、输入

```python
# 使用inpiut得到的所有东西都是字符串类型，根据不同的需要进行相应的转化
name = input("Enter your name: ") # input里面写入提示信息
print("Hello " + name + "!")
# 注意用input读到的东西都是字符串
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) # 使用数字要进行强制类型转换
print(result)
```

### 五、数组(map)

```python
friends = ["Kevin", "Karen", "Jack"]
#数组的访问方式
print(friends)
print(friends[0])
# 数组的最后一个元素的索引也可以用-1表示，同理-2就是倒数第二个 ...
print(friends[-1] + friends[-2]) # Jack Karen
print(friends[1:]) # 打印索引从1到最后的所有元素 Jack Karen
print(friends[1:2]) # 注意这是一个左闭右开的区间，我们只会打印1号元素，friends[1:1]为空

#数组的修改
friends = ["Kevin", "Karen", "Jack"]
friends[0] = "Mike"
print(friends[0]) # Mike

mp = ["hh", 1, False]
print(mp)
```

```python
# 数组的API
# 1、extend，在数组后面添加一个数组
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
friends.extend(lucky_numbers)
# 添加数组 friends.extend([1, 5, 5]) ["Kevin", "Karen", "Jim", "Oscar", "Tim", 1, 5, 5]
# 添加字符串 friends.extend("a b") ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim', 'a', ' ', 'b']
print(friends) # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim', 4, 8, 15, 16, 23, 42]
# 2、append，在数组最后添加一个元素
friends.append("creed")
print(friends) # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim', 'creed']
# 3、在数组中间添加一个元素
.insert(起始位置，放入的元素) 其余的元素将被往后推
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
friends.insert(1, "kelly")
print(friends) # ['Kevin', 'kelly', 'Karen', 'Jim', 'Oscar', 'Tim']
# 4、删除元素
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
friends.remove("Jim") # 删除指定元素，不能输入下标
friends.clear() # 清空数组
friends.pop() # 删除最后一个元素
print(friends)
# 5、查询元素下标和数量
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim" ,"Jim", "Jim",]
print(friends.index("Kevin")) # 0 ，若是不存在则报错
print(friends.count("Jim")) # 3
# 6、排序(按照字典序排列)
lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.sort()
print(lucky_numbers) # [4, 8, 15, 16, 23, 42]
# 7、翻转数组
lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers) # [42, 23, 16, 15, 8, 4]
# 8、数组复制
lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers1 = lucky_numbers.copy()
print(lucky_numbers1) # [4, 8, 15, 16, 23, 42]
# 9、数组长度
print(len(lucky_numbers)) # 6
```

### 六、Tuple (pair)

* 类似于c++中的pair，但是值不能被修改

  ```python
  coordinates = (4, 5)
  print(str(coordinates[0]) + "," + str(coordinates[1])) # 4,5
  # 可以与数组嵌套
  a = [(1, 1), (2, 2), (3, 3)]
  ```

### 七、函数

```python
def say_hi(): # 注意要加冒号
    print("Hello User") # 函数内部的内容都要有缩进

say_hi()
# 函数传参
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")

# 返回值
def cube(num):
    return num ** 3

print(cube(3)) # 27
```

### 八、判断语句

```python
is_male = True
is_tall = True
is_collage = False

if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall): # 相当于!
    print("You are a short male")
elif not(is_male) or not(is_tall):
    print("You are a female or short")
else:
    print("You are a failure")
```

```python

def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if "dog" == "dog": # 可以进行字符串比较
    print("a")
if(a != b): # 可以直接写 ！
    print("a")

print(maxnum(3, 4, 5))

# 判断某个字母是否在某个字符串中：
if(a in "abcde"):
```

### 九、字典(哈希表)

```python
# 创建方式
monthConversions = { # 使用大括号创建字典
    # 存储键值对,注意键必须是唯一的
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
    1: "a" # 可以用来存储不同类型的数据，类似于js中的对象
}

# 访问方式
print(monthConversions["Jan"]) # 里面输入一个不存在的值会报错
print(monthConversions.get('Feb', "not a valid key")) # 里面输入一个不存在的值默认会输出None,后面的参数可以改变不合法的输入的输出结果

```

### 十、循环

1. while循环

   ```python
   # 和c++一致
   n = int(input("输入一个整数："))
   
   while n > 0:
       print(n)
       n = n - 1
   ```

2. for循环

   ```python
   for i in "a b c":
       print(i) # 会将每个字符单独打印出来
   
   friends = ["Jim", "Karen", "Kevin"]
   for i in friends:
       print(i) # Jim Karen Kevin
   for i in range(3,10):
       print(i) # 左闭右开区间，如果只有一个参数默认左端点为0
   # 类似于c++中的遍历方式
   friends = ["Jim", "Karen", "Kevin"]
   for i in range(len(friends)):
       print(friends[i])
   ```

   

### 十一、二维数组

```python
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# 两种遍历方式
for i in range(len(number_grid)):
    for j in range(len(number_grid[i])):
        print(number_grid[i][j])

for i in number_grid:
    for j in i:
        print(j)
```

### 十二、注释

```python
# 这是一行注释

# 三个单引号
'''
这是多行注释
这是注释
这是注释
'''
```

### 十三、Try / Catch语句

```python
try:
    a = 10 / 0
    number = int(input("Enter a number："))
# 针对不同的情况做出不同的处理，否则就会出现做出宽泛的处理导致不太合法的情况
except ZeroDivisionError as err: # 将错误存储为一个变量打印出来
    print(err)
except ValueError:
    print("Invalid input")
except: # 注意这里不能加as
    print("other error")
```

### 十四、读写文件

```python
# r为只读模式，w为只写模式，r+为读写模式,a(append)为将当前内容附加到文件后面
# readable()可以判断该文件是否可读
file = open("C:\\Users\\86150\\Desktop\\text.txt","r") # 打开文件
# read 会将文件中的所有内容读出来
print(file.read())
# readline 读取一行同时将光标下移
print(file.readline())
# readlines会将文件中的所有东西放到数组中，一行为其中的一个元素
printf(file.readlines()[0]) # 打印第一行的内容
# for循环读取
for line in a.readlines():
    print(line)
file.close() # 及时关闭文件
```

```python
file = open("C:\\Users\\86150\\Desktop\\text.txt","a") # 追加内容

file.write("\n111 a 44")

file.close()

# w为覆盖所有内容并写入，如果当前文件不存在则将新建一个新的文件
file = open("a.html","w") # 甚至可以创建一个html文件

file.write("<h1>This is a page!</h1>")

file.close()
```

### 十五、模块

* 类似于c++中的include

  ```python
  # py文件之间的相互使用
  # app.py
  import random
  
  feet_in_male = 5280
  meters_in_kilometer = 1000
  beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]
  
  def get_file_ext(filename):
      return filename[filename.index(".") + 1:] # 得到文件的拓展名
  
  def roll_dice(num):
      return random.randint(1, num) # 随机数,里面填写的是范围
  
  # main.py
  import app # 只需要将想要使用的py文件的名字引用过来就行
  
  print(app.roll_dice(10))
  ```

  

* 使用pip安装python的第三方库，别人实现好的文件

  ```
  pip install ... # 在cmd中安装，安装好后会放到外部库中的lib中的site-packages中
  import ...
  # 然后就能使用里面的函数、变量等所有内容
  pip uninstall python-...
  ```

  

### 十六、类和对象

```python
# Student.py
class Student:
    # 构造函数
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# main.py
from Student import Student # 从Student文件中引入Student类

student1 = Student("Make", "computer", 4.9, True)

print(student1.name)
```

* 类函数

  ```python
  class Student:
      # 构造函数
      def __init__(self, name, major, gpa, is_on_probation):
          self.name = name
          self.major = major
          self.gpa = gpa
          self.is_on_probation = is_on_probation
  
      def in_honor_roll(self):
          if self.gpa >= 3.5:
              return True
          else:
              return False
  
  ```

  

### 十七、继承

```python
# chef.py
class Chef:

    a = 0

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a bbq ribs")
        
# ChineseChef.py
from Chef import Chef

class ChineseChef(Chef): # 能使用Chef中所有的成员
    def make_fried_rice(self):
        print("The chinese makes rice")
        
 # main.py
from Chef import Chef
from ChineseChef import ChineseChef
from abc import ABC,abstractmethod

mychef = Chef()
mychef.make_chicken()

mychinesechef = ChineseChef()
mychinesechef.make_chicken()
```

