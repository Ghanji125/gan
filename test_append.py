#### Markdown notebook

https://www.jianshu.com/p/8c1b2b39deb0



#Sort   list.sort()  vs sorted(lsit)
lst = [2,1,5,3,4]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


#Sort   list.sort()  vs sorted(lsit)
lst = [2,1,5,3,4]
new_lst = sorted(lst)
print(lst)
print(new_lst)

lst = sorted("String123698745")
print(lst)
type(lst)

string = "".join(sorted("String123698745"))
print(string)
type(string)

#assign vs copy
a = [1,2,3,4,5]
b = a #assign
a[1] =55
a
b


#assign vs copy
a = [1,2,3,4,5]
b =  a.copy()
c = a[:]
d = list(a)
a[1] =55
a
b
c
d


#dictionary  == %hash  {key:value,...}
#set  == {key,key,...}   #immutable;can not be indexed
empty_dict_define = {}
empty_set_define = set()
even_set = {5,2,3,4,5,6,1}
even_set
for i in even_set:
    print(i)
    
    
# bool
and (&) or (|) not (!)  ^(亦或: 0^1 = 1^0 = 1 ; 0^0 = 1^1 = 0)


num_set = {2,3,5,7,9}
even_set = {5,7,8,9,10}
num_set & even_set   #都有的
num_set | even_set   #只要之中有的
num_set - even_set   #后一个中没有的
# num_set + even_set    #TypeError: unsupported operand type(s) for +: 'set' and 'set'
num_set ^ even_set   #不共有的


uu = {"a","b","b"}
uuu = {"1","a","b","c"}
uu & uuu    # <==>  uu and uuu
uu | uuu    # <==> uu or uuu
uu - uuu
uu ^ uuu
uu not in uuu

### Convert into List | Tuple

list("asdfg")
list(("asdfg","asdfgh"))
list({"asdfg"})
list({5:"asdfg",2:"asdfgh"})            # dict2list just keep the key!!! Can not be ordered, but can use "sorted()" function
list({5:"asdfg",2:"asdfgh"}.values())   # dict2list to keep the value, need to add ".values()"!!!
tuple("asdfg")
tuple(("asdfg","asdfgh"))
tuple({"asdfg"})
tuple({5:"asdfg",2:"asdfgh"})            # dict2tuple just keep the key!!! Can not be ordered, but can use "sorted()" function
tuple({5:"asdfg",2:"asdfgh"}.values())   # dict2tuple to keep the value, need to add ".values()"!!!


### Convert into Dictionary

dict("a","b","c")        #TypeError: dict expected at most 1 arguments, got 3
dict(("a","b","c"))      #ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(["a","b","c"])      #ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(["abc","bc","cd"])  #ValueError: dictionary update sequence element #0 has length 3; 2 is required

dict(("ab","bc","cd"))
dict(["ab","bc","cd"])
dict({"ab","bc","cd"})
dict((["ab","ba"],"bc","cd"))
dict((["ab","ba"],(1,2),"bc","cd"))

s1 = "abcdefg"
s2 = "hijklmn"
zip(s1,s2)
list(zip(s1,s2))
dict(list(zip(s1,s2)))

s1 = "abcdefg"
s2 = "hijklmn"
s34 = list(zip(s1,s2))
s34
s3,s4 = zip(*s34)    #unzip: * is a splat operator, it is used to unpack argument list; foo(*[1,2,3]) == foo(1,2,3)
s3
type(s3)
s4

type(zip(s1,s2))

### Mutable & Immutable
#### Immutalbe
- bool : Boolean value
- int : integer (arbitrary magnitude)
- float : floating point number
- tuple : immutable sequence of objects
- str : character string
- frozenset : immutable form of set class
- dict : associative mapping (aka dictionary)

#### Mutalbe  (Could not be dict-key)
- list : mutable sequence of objects
- set : unorder set of distinct objects

> 1.   这是第一行列表项。
> 2.   这是第二行列表项。
>
> 给出一些例子代码：
> 
>     return shell_exec("echo $input | $markdown_script");

https://github.com/Ghanji125/gan  ==  pw

source = '<img src="https://res.gufengmh8.com/images/comic/419/836199/1551978809CU3CJnz-U7JEK8KN.jpg" data-index="1" style="display: inline-block;"><p class="img_info">(1/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978808k4Mvx4JFMlbGAGIb.jpg" data-index="2" style="display: inline-block;"><p class="img_info">(2/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/15519788073yeACXAyZNMn89ga.jpg" data-index="3" style="display: inline-block;"><p class="img_info">(3/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978805mkbez5LKaVTP3ejt.jpg" data-index="4" style="display: inline-block;"><p class="img_info">(4/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978803ZHowd-6dHwjjcn6L.jpg" data-index="5" style="display: inline-block;"><p class="img_info">(5/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978802etTK3J3mcZTamtMK.jpg" data-index="6" style="display: inline-block;"><p class="img_info">(6/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/15519788027rsMyPmnFfFOvBJo.jpg" data-index="7" style="display: inline-block;"><p class="img_info">(7/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/15519788016FBSbNXOVrXj20eB.jpg" data-index="8" style="display: inline-block;"><p class="img_info">(8/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978800OAejdlZKYuv-rhH4.jpg" data-index="9" style="display: inline-block;"><p class="img_info">(9/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978799xXAYZ7I0HoV99h6Z.jpg" data-index="10" style="display: inline-block;"><p class="img_info">(10/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978799RoLi6DOUheJ8HGoZ.jpg" data-index="11" style="display: inline-block;"><p class="img_info">(11/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978796IKt7LLbdOnmKwb20.jpg" data-index="12" style="display: inline-block;"><p class="img_info">(12/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978795cQ6FP_uEzZbeR1jj.jpg" data-index="13" style="display: inline-block;"><p class="img_info">(13/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/15519787941oMNu4uaPKq4hS2V.jpg" data-index="14" style="display: inline-block;"><p class="img_info">(14/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978793y-VuWNllPGVYESwZ.jpg" data-index="15" style="display: inline-block;"><p class="img_info">(15/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978792CQGoK42XSFm_friW.jpg" data-index="16" style="display: inline-block;"><p class="img_info">(16/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/1551978790X_C6xv8Br5hnzeCh.jpg" data-index="17" style="display: inline-block;"><p class="img_info">(17/18)</p><img src="https://res.gufengmh8.com/images/comic/419/836199/15519787907tC9DvhFEp6Z2xdM.jpg" data-index="18" style="display: inline-block;"><p class="img_info">(18/18)</p></div>'
print(source)
source.find("gasgagw##$24egwegewg")  # if the string doesnt contained objects, return -1

while -1:
    print("-1 is TRUE")
    break
#-1 is TRUE


site_start = source.find("https")
site_stop = source.find('"',site_start)
source[site_start:site_stop]
#'https://res.gufengmh8.com/images/comic/419/836199/1551978809CU3CJnz-U7JEK8KN.jpg'


site_start = source.find("https")
site_stop = source.find('"',site_start)
website = []
link = source[site_start:site_stop]
website.append(link)
while True:
    site_start = source.find("https",site_stop)
    site_stop = source.find('"',site_start)
    if site_start == -1:
        break
    link = source[site_start:site_stop]
    website.append(link)
    
for i in website:
    print(i)
 

#len(source.split('<p class="img_info">')) #19
img_list = source.split('<p class="img_info">')
#img_list[1][10:]
#img_list[10][11:]
img_list_trim = [img_list[0]]
for i in range(1,18):
    if i < 10:
        img_list_trim.append(img_list[i][10:])
    else:
        img_list_trim.append(img_list[i][11:])
for each in img_list_trim:
    print (each)
#<img src="https://res.gufengmh8.com/images/comic/419/836199/1551978809CU3CJnz-U7JEK8KN.jpg" data-index="1" style="display: inline-block;">

#method 2
import re
#pattern = re.compile(r'\d+')   # 查找数字
#result1 = pattern.findall('runoob 123 google 456')
#result2 = pattern.findall('run88oob123google456', 0, 10)
#['123', '456']
#['88', '12']
pattern = re.compile(r'<img src="')
print(type(re.findall(pattern,source)))
print(type(re.finditer(pattern,source)))
#<class 'list'>
#<class 'callable_iterator'>

dc = {5:"a",1:"b",9:"q"}
k = sorted(list(dc))
v = list(dc[i] for i in k)
new_dc = dict(list(zip(k,v)))
new_dc

import matplotlib.pyplot as plt
import random

def roll_dice():
    return random.randint(1,6)

times = 10000
output_result = [0]*6    #[0,0,0,0,0,0]
for i in range(times):
    point = roll_dice()
    output_result[point-1] +=1
for p,c in enumerate(output_result):
    print("point {} appears {} times!".format(p+1,c))
    

times = 10000
output_result1 = [0]*6    #[0,0,0,0,0,0]
output_result2 = [0]*6    #[0,0,0,0,0,0]
total_points = dict(zip(list(range(2,13)),[0]*12))    #{2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in range(times):
    point1 = roll_dice()
    point2 = roll_dice()
    output_result1[point1-1] += 1
    output_result2[point2-1] += 1
    total_points[point1+point2] += 1
    
for p,c in enumerate(output_result1):
    print("Dice1: point {} appears {} times!".format(p+1,c))
print()

for p,c in enumerate(output_result2):
    print("Dice2: point {} appears {} times!".format(p+1,c))
print()
    
for k,v in total_points.items():
    print("Total points {} appears {} times!".format(k,v))
total_points.values()
#plt.hist(,bins=range(2,13),edgecolor="white",line)
#plt.show()

x = sorted(total_points.keys())
print(x)
y = list(total_points[i] for i in x)
print(y)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set(xlabel="X label", ylabel="Y label", title="Title")
ax.grid()
plt.show()


#1. 注释乱码问题
#在代码的最上面添加：
# -*- coding: utf-8 -*-

#2. 无法识别中文字体
#通过运行以下代码查看系统中可以用的中文字体：
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)

output = subprocess.check_output(
    'fc-list :lang=zh -f "%{family}\n"', shell=True)
# print '*' * 10, '系统可用的中文字体', '*' * 10
# print output
zh_fonts = set(f.split(',', 1)[0] for f in output.split('\n'))
available = mat_fonts & zh_fonts

print '*' * 10, '可用的字体', '*' * 10
for f in available:
    print f

#加入以下语句：
from pylab import *
mpl.rcParams['font.sans-serif'] = ['Droid Sans Fallback']
#注：Droid Sans Fallback 为查询得到的系统中的中文字体

#3. 画图时候“-”号显示为方块问题
#加入以下语句：
mpl.rcParams['axes.unicode_minus'] = False
#解决保存图像是负号'-'显示为方块的问题

reference:  http://www.cnblogs.com/wei-li/archive/2012/05/23/2506940.html#oo 
            http://old.sebug.net/paper/books/scipydoc/index.html#id2



def estimate_pi_1(times):
    pi_estimate = 0
    flag = 0

    #1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ....

    for i in range(1,times):
        if i%2:
            if flag == 0:
                pi_estimate += 1/i
                flag = -1
            else:
                pi_estimate -= 1/i
                flag = 0            
    print(pi_estimate*4)
estimate_pi_1(1000000)

import random
def estimate_pi_2(times):
    point_in_circle = 0
    for i in range(times):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            point_in_circle += 1
    pi_estimate = point_in_circle / times
    print(pi_estimate*4)
estimate_pi_2(1000000)

## Unit Converter

km/m/dm/cm/mm/um/nm/in/ft/yd/mile/nmile

1里=150丈

1丈=10尺
 
1尺=10寸
 
1寸=10分
 
1分=10厘
 
1厘=10毫

>
100	厘米(cm)
0.001	千米(km)
1000	毫米(mm)
10	分米(dm)
1000000	微米(um)
1000000000	纳米(nm)
1000000000000	皮米(pm)
1.0570e-16	光年(ly)
6.6846e-12	天文单位(AU)
39.3700787	英寸(in)
39.3700787	inch(in)
0.0006214	英里(mi)
3.2808399	英尺(ft)
3	尺
1.0936133	码(yd)
0.00054	海里(nmi)
0.5468066	英寻(fm)
0.004971	弗隆(fur)
0.002	里
0.3	丈
30	寸
300	分
3000	厘
30000	毫


convert_factors = {"m":1,"cm":100,"km":0.001,"mm":1000,"dm":10,"um":1000000,"nm":1000000000,"pm":1000000000000,
                   "ly":1.0570e-16,"AU":6.6846e-12,"in":39.3700787,"mi":0.0006214,"ft":3.2808399,"yd":1.0936133,
                  "nmi":0.00054,"fm":0.5468066,"fur":0.004971,"里":0.002,"丈":0.3,"尺":3,"寸":30,"分":300,"厘":3000,"毫":30000}
amount = 40
from_unit = "ft"
to_unit = "cm"

factor2base_from_unit = convert_factors[from_unit]
factor2base_to_unit = convert_factors[to_unit]
equal2base = amount / factor2base_from_unit
base2target = equal2base * factor2base_to_unit
print("{} {} equal to {} {}".format(amount,from_unit,base2target,to_unit))

convert_factors = {"m":1,"cm":100,"km":0.001,"mm":1000,"dm":10,"um":1000000,"nm":1000000000,"pm":1000000000000,
                   "ly":1.0570e-16,"AU":6.6846e-12,"in":39.3700787,"mi":0.0006214,"ft":3.2808399,"yd":1.0936133,
                  "nmi":0.00054,"fm":0.5468066,"fur":0.004971,"里":0.002,"丈":0.3,"尺":3,"寸":30,"分":300,"厘":3000,"毫":30000}
def convert_tool(amount,from_unit,to_unit):
    factor2base_from_unit = convert_factors[from_unit]
    factor2base_to_unit = convert_factors[to_unit]
    equal2base = amount / factor2base_from_unit
    base2target = equal2base * factor2base_to_unit
    print("{} {} = {} {}".format(amount,from_unit,base2target,to_unit))

amount = float(input("Input the number to be converted:"))
from_unit = input("Choose the initial unit:")
to_unit = input("Choose the target unit:")
convert_tool(amount,from_unit,to_unit)




