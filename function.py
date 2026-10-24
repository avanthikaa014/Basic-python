# def display():
#     print("hello")
# display()    

# def user(name):
#     print("hello",name)
# user("ammu")    

# def add(a,b,c):
#     print(a+b+c)
# add(2,4,6)    



#when user input is given

# def display(name,course):
#     print(name,"is studying",course)
# n=input("enter the name:")    
# c=input("enter the course:")
# display(n,c)


#default value for parameter
# def display(name,course="ds"):
#     print(name ,"is study",course)
# display("ammu","python")
# display("anu") \

# def add(a,b):
#     return a+b
# result=add(20,34)
# print(result)


#positional arguments
# def substract(a,b):
#     print(a-b)
# substract(5,3)    
# substract(2,6)


#arbitrary arguments
# def display(*a):
#     print(a)
# display(1,2,3,4,5,6)   // #return as a tuple


# def display(*a):                     #arbitrary arguments allow us to pass any number of positional argument
#     s=sum(a)
#     print("sum:",s)
# display(1,2,3,4,5)    

# #keyword argument        /// #we can specify parameter name while calling the function//
# def display(a,b,c):
#     print(a,b,c)
# display(a=10,c=30,b=20)    

#returning multiple values
# def cal(a,b):
#     sum=a+b
#     diff=a-b
#     return sum,diff
# s,d=cal(10,20)
# print("Sum is :",s)
# print("Diff is : ",d)

# def student():
#     name=input("Enter name : ")
#     age=int(input("Enter Age : "))
#     cource=input("Enter Course : ")
#     return name,age,cource
# n,a,c=student()
# print("Name is ",n,"Age ",a,"Course ",c)


# def large(a,b):
#     if a>b :
#         return a
#     else :
#         return b
# n1=int(input("Enter First Number : "))
# n2=int(input("Enter Second Number : "))
# print("Largest is ",max(n1,n2))


# def vowels(s):   #vowels
#     v="aeiou"
#     c=0
#     for i in s: 
#         if i in v:
#             c+=1
#     return c
# s=input("Enter String : ")
# print("No of vowels : ",vowels(s))

# def oddeven(n):   #odd even 
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("Enter number : "))
# print(n ,"is ",oddeven(n))

# def rev(s):   #reverse a string
#     char=""
#     for i in s:
#         char=i+char
#     return char
# s=input("Enter String : ")
# print("reverse is :",rev(s))

# def rev(s):   #reverse a string
#     return s[::-1]
# s=input("Enter String : ")
# print("reverse is :",rev(s))


# def add(n):    #sum of list
#     return sum(n)
# l=[]
# n=int(input("Enter limit :"))
# for i in range(n):
#     user=int(input("Enter Element : "))
#     l.append(user)
# print("Sum is : ",add(l))


 
#Scope Of Variables

# def display():
#     x=10
#     print("inside fun",x)
# display()
# print("outside fun",x)    

#when variable name is same
# x=40
# def display():
#     x=4
#     print("inside the fn:",x)
# display() 
# print("outside the fn",x)


# x=40
# def display():
#     global x
#     x=4
#     print("inside the fn:",x)
# display()
# print("outside the fn",x)



# pass by value
# def modify(x):
#     x=x+5
#     print("inside function:",x)
# x=10
# modify(x)    
# print("outside fun:",x)



# pass by reference
# def modify(lst):
#     l.append(10)
#     print("inside function",l)
# l=[1,2,3,4]    
# modify(l)
# print("outside fun:",l)

    
# Recursion
# def display(x):
#     if x==0:
#         return x
#     else:
#         return x+display(x-1)
# n=int(input("enter a number"))    
# print("cumilative sum is:",display(n))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# x=int(input("enter a number"))    
# print("factorial is",factorial(x))

# def display(n):
#     if n==0:
#         return 0
#     else:
#         print(n)
#         display (n-1)
# x=int(input("enter a number"))   
# display(x)    



# def display(lst):
#     sum=0
#     for i in l:
#         sum+=i
#     return sum
# l=[1,2,3,4]
# print("the sum is",display(l))

# l=[1,2,3,4]
# def display(lst):
#     s=[(i,i**2) for i in lst]
#     print(s)
# display(l)    


# def prime(n):
#     if n%1==0 and n%n==0:
#         return "prime"
#     else:
#         return "not prime" 
# num=int(input("enter a number"))    
# print(prime(num))



# def lar(list):  
#     s=sorted(list)
#     return s[-1]
# l=[3,2,4,1,5,8,7,6]
# print("the largest is",lar(l))



# def cmn(list1,list2):
#         s=set(list1)
#         p=set(list2)
#         return s.intersection(p)
# l1=[2,3,4,5]
# l2=[1,4,5,6,7]
# print("common elements are",cmn(l1,l2))


# def eve(lst):
#     for i in lst:
#         if i%2==0:
#           return i
# l=[1,2,3,4,5,6,7,8]       
# print("even numbers are",eve(l)) 















#lambda function
# ------------------
# //lambda function is mainly used when we need a short funtion just once
#  can give any no of arguments,but a single expression
#  dont have to specifyy a fn name//

# lambda arguments:expression
# -------------------------------------

# square of numbers
# x=lambda a:a**2
# n=int(input("enter a number:"))
# print(x(n))

# x=lambda a,b:a+b
# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# print("sum is",x(n1,n2))


# x=lambda a,b:a if a>b else b
# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# print("large is:",x(n1,n2))

# x=lambda a: "even" if a%2==0 else "odd"
# n1=int(input("enter first number"))
# print("number is",x(n1))


#higher order build in functions
# filter()
# map()
# reduce()

# filter():selecting elements from an iterable based
# on condition
# filter(function,iterable)
# lst=[1,2,3,4,5,6,7,8]
# x=filter(lambda a: a%2==0,lst)
# print(list(x))


# map():used to apply a funtion to every item
# in a sequence(list,tuple,set)
#map(function,iterble)
# lst=[1,2,3,4,5,6,7,8,9,10]
# x=map(lambda a:a**2,lst)
# print(list(x))



# reduce()
# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9]
# x=reduce(lambda a,b:a+b,l)
# print(x)


# def sum(n):
#     if n==0:
#         return n
#     else:
#         return n+(n-1)
# n=int(input("enter a limit"))    
# print(sum(n))


#fibonacci series
# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# def printfib(n):
#     for i in range(n):
#         print(fib(i)," ")
# n=int(input("enter the limit:"))    
# print("fib series upto ",n,"terms:")    
# printfib(n)




# def exp(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*exp(x,n-1)
# n=int(input("enter the number"))
# x=int(input("enter the exp"))
# print(exp(n,x))



# def rev(x):
#     if len(x)==0:
#         return x
#     else:
#         return x[-1]+rev(x[:-1])
# n=input("enter a string")    
# print("reverse is",rev(n))


# def dig(n):
#       if n<=9:
#             return 1
#       else:
#             return 1+dig(n//10)
# n=int(input("enter the number"))    
# print(dig(n)) 

# def sumlist(l):
#     if len(l)==0:
#         return 0
#     else:
#         return l[0]+sumlist(l[1:])
# n=[1,2,4,3,5 ]    
# print(sumlist(n))




# def rev(x):
#     if len(x)==0:
#         return x
#     else:
#         return x[-1]+rev(x[:-1])
# n=input("enter a string")    
# print("reverse is",rev(n))
# if rev(n)==n:
#     print("string is palindrome")
# else:
#     print("not palindrome")



# x=lambda a,b:a+b
# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# print("sum is",x(n1,n2))


# x=lambda a:a[-1]
# n=input("enter the string")
# print("last char is",x(n))

# x=lambda n:n*3
# l=[1,2,3,4,5]
# for i in l:
#     print(x(i))

# x=lambda n:"string start with A" if n[0]=="A" else "not start with A"
# n=input("enter the string:")
# print(x(n))


# x=lambda a,b:a**b
# n=int(input("enter a number"))
# m=int(input("enter the exp"))
# print(x(n,m))

# x=lambda a,b:"a is larger"if len(a)>len(b) else"b is larger"
# a=input("enter 1st string")
# b=input("enter 2nd string")
# print(x(a,b))

# s=input("enter a string:")
# l=s.split(" ")
# x=filter(lambda n:len(n)>4,l)
# print(list(x))

# l=[1,5,6,11,17,7,18]
# x=filter(lambda n:n>10,l)
# print(list(x))

# n=input("enter the string:")
# l=n.split(" ")
# x=filter(lambda n:n[0]=="p",l)
# print((list(x)))

# def prime(n):
#     c=0
#     m=int(n)
#     for i in range(2,m):
#         if m%i==0:
#             c+=1
#     if c==0:
#         return n
#     else:
#         return 0       
# l=[1,2,3,4,5,6,7,8,9,11,13,24]
# x=filter(prime,l)
# print(list(x))


# n=input("enter a string")
# l=n.split(" ")
# x=map(lambda a:a.upper(),l)
# print(list(x))


# l=[1,2,3,4,5]
# x=map(lambda a:(a * 1.8) + 32,l)
# print(list(x))

# n=input("enter a string")
# l=n.split(" ")
# x=map(lambda a:a+"_done",l)
# print(list(x))


# l1=[1,2,3,4]
# l2=[2,3,4,4]
# x=map(lambda a,b:a+b,l1,l2)
# print(list(x))


# from functools import reduce
# l=[1,2,3,4]
# x=reduce(lambda a,b:a+b,l)
# print(x)

# n=input("enter a string")
# l=n.split(" ")
# x=reduce(lambda a,b:a+b,l)
# print(x)