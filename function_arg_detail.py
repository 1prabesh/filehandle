print(),print(), print()
print('==========positional argument==========')
def foo(a,b,c):
    print(a,b,c)

foo(1,2,3)
print('==========Keyword argument==========')
def num(a,b,c):
    print(a,b,c)

num(a=2,b=6,c=7)

print('=======================================')
def num(a,b,c):
    print(a,b,c)

num(2,b=5,c=9)
print('===================================')

def name(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg,end=" ")
    for key in kwargs:
        print(key,kwargs[key],end=" ")
    
name(1,2,6,7,8,9,model='Ford',Design='Germany')
print()
    
print('===================UNPACKING THE LIST==================')

def foo(a,b,c):
    print(a,b,c)

my_list=[1,2,30] # this also works for tuple and dictionary ( but ** must be given when argumenting dictionary)
foo(*my_list) # this will unpack the list and assign individaul value

print('==================================')
def foo(x):
    x=5
var=6
foo(var)
print(var)  # immutable object cannot be modified but mutable can

print('=================================')
def foo(list):
    thelist.append(20)

thelist=[1,3,5]
foo(thelist)
print(thelist)   # so mutalbe type eg, list can be modifed inside function irrespective to local and global variable

print('===========UNPACKING LIST METHOD-2===============')
number=[1,2,3,4,5,6]
*first, last=number
print(*first)  # unpack all the list from first till second last 
print(last)    # seperate the last term ( 6 ) from list and

# can include other as well a, *b, c, d


print('=================Merging the list=================')

the_list1=[1,2,3] # can include dictionary as well
the_list2=[4,5,6]
merged_list=[*the_list1, *the_list2]
print(merged_list)



print(),print()