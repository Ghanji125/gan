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


