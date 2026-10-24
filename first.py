# print("avanthika anil")
# print("hehhehehe")
# s=22
# print("age is",s)
# a="ammu"
# c=65.3
# d=False
# print(a)
# print(c)
# print(d)
# print(type(a))
# print(type(c))
# print(type(d))
# print(type(s))
#OPERATORS
#Arithematic Operator 
#1.Addition
# a=4
# b=3
# print(a+b)
# #2.Sub
# c=6
# d=5
# print(c-d)
# #3.Mul
# e=8
# f=8
# print(e*f)
# #4.Div
# g=3
# h=9
# print(g/h)
# #5.Mod/reminder
# t=30
# s=20
# print(t%s)
# #6.Floor
# y=27664
# x=1000
# print(y//x)
# #7.Exponent
# i=3
# j=2
# print(i**j)
# #Comparison Operator
# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# #Assignment Operator
# a=10
# b=2
# a+=b
# print(a)
# a-=b
# print(a)
# a*=b
# print(a)
# a/=b
# print(a)
# a//=b
# print(a)
# a**=b
# print(a)
#Logical Operator
# a=True
# b=True
# print(a and b)
# print(a or b)
# print( not a )
# print( not b)
# a=False
# b= True
# print(a and b)
# print(a or b)
# print (not a)
# print (not b)
#Membership Operator
# a= "Avanthika"
# print('a' in a)
# print('A' not in a)
# print('x'in a)
# print('V' in a)
# l=["avanthi","Ammu",'minsha']
# print('Ammu'in l)
# print('appu'in l)
# print('avanthi'not in l)
#Identity Operator
# a=1
# b=2
# print(a is b)
# print( a is not b)
# a=[1,2,3,4]
# b=[7,1,2,3]
# print(a is b)
# print(a is not b)



#2.Conditional Statment
#if
# age=43
# if age>=18:
#     print("eligible to vote")
#if else
# age=17
# if age>=18:
#     print("eligible to vote")   
# else:
# #     print("not eligible" )     
# mark=67
# if mark>=50:
#     print("pass")
# else:
#     print("fail")    
# num=int(input("enter a number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")    
# number=int(input("enter a number"))
# if number>=0:
#     print("number is positive")
# else:
#     print("number is Negative")  
# mark=int(input("enter the mark")) 
# if mark>=90:
#     print("grade is A")
# elif mark>=80:
#     print("grade is B")     
# elif mark>=70:
#     print("grade is C")    
# elif mark>= 50:
#     print("grade is D")    
# else:
#     print("fail")
#NESTED IF
# mark=int(input("enter the mark")) 
# if mark>=50:
#     if mark>=90:
#         print("grade is A")
#     elif mark>=80:
#         print("grade is B")     
#     elif mark>=70:
#         print("grade is C")    
#     elif mark>= 50:
#         print("grade is D")    
# else:
#     print("fail")
# number=int(input("enter a number"))
# if number>0:
#     if number%2==0:
#         print("number is even")
#     else:
#         print("number is odd")    
# else:
#     print("number is neg")
        
# 
# 
# sal=int(input("enter the salary"))
# exp=int(input("no of year worked"))
# if exp>5:
#     bon=sal*0.05*12
#     print("bon is",bon)
# else:
#     print("no bonus")
# 
# 
# clas=int(input("total class"))
# attend=int(input("number of class attend"))
# per=attend/clas*100
# print(per)
# if per>75:
#     print("allow for exam ")
# else:
#     print("not allowed")    


# age=int(input('enter the age:'))
# sex=input('enter the sex:')
# martial=input('Are you married:')
# if sex=="female":
#     print("work at urban areas")
# elif sex=="male":
#     if age>20 and age<40:
#         print("work anywhere")
#     elif age>40 and age<60:
#         print("work at urban areas")    
#     else:
#         print("error")        

# a=int(input('enter the first age'))
# b=int(input('enter the second age'))
# c=int(input('enter the third age'))
# if a>b and a>c:
#     print('a is large')
#     if b<c:
#         print("b is smaller")
#     else:
#         print("c is smaller")    
# elif b>a and b>c:
#     print('b is large')   
#     if a<c:
#         print('a is smaller') 
#     else:
#         print('c is smaller')    
# elif c>a and c>b:
#     print('c is larger')
#     if b<a:
#         print('b is smaller')
#     else:
#         print('a is smaller')    
       



# num=int(input('enter a number'))
# if num%2==0 and num%5==0:
#     print("possible")
# elif num%2==0:
#     print("possible")   

# elif num%5==0:
#     print('possible')
# else:
#     print('not possible')  

#REVERSE
# n=int(input("emter a 4 digit number"))
# d1=n%10
# d2=(n//10)%10
# d3=(n//100)%10
# d4=n//1000
# r=d1*1000+d2*100+d3*10+d4
# print("reversed number is",r)

#SWAP
# a=int(input('enter 1st number'))
# b=int(input('enter second number'))
# print("before a",a,"b",b)
# a,b=b,a
# print("after swap a",a,"b",b)


#ATM BANK
# bal=int(input("enter the balance"))
# wid=int(input("enter the amount to be withdraw"))
# if wid<=bal:
#     if wid%100==0:
#         print('transaction successful')
#     else:
#         print("enter amount in multiple of 100")
# else:
#     print("insufficent balance")        

#LOAN
# sal=int(input("enter the salary:"))
# credit=int(input("enter the credit score:"))
# loan=int(input("Enter the loan amount needed:"))
# if sal>=30000:
#     if credit>=700:
#         if loan<=20*sal:
#             print("loan approved")
#         else:
#             print("amount too high")    
#     else:
#         print("improve credit score")        
# else:
#     print("low income")
     
    
#ONLINE FOOD ORDER
# type=input("v OR non veg")
# if type=="v":
#     item=input("paneer,vegbiriyani")
#     count=int(input("enter the quantity"))
# else:
#     item=input("fish,chicken ")
#     count=int(input("enter the quantity")   ) 
# paneer=600 
# vegbiriyani=250
# fish=350
# chicken=450
# if item=="paneer":
#     bill=paneer*count
# elif item=="veg biriyani" :
#     bill=vegbiriyani*count
# elif item=="fish" :
#     bill=fish*count   
# else:
#     bill=chicken*count     
# if bill>=1000:
#     dis=bill//10
#     print("discount is ",dis)     
# else:
#     print("no discount")




#4.LOOP IN PYTHON
#1. WHILE  
 
# i=0
# while i<5:
#     print("hello amz")
#     i+=1

# i=1
# while i<=10:
#     print(i)
#     i+=1

# num=int(input("enter the number"))
# i=1
# while i<=num:
#     print(i)
#     i+=1


# i=1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("loop ended")    

# i=0
# while i<5:
#     print("hello")
#     if i==3:
#         break
#     i+=1


# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i+=1

# i=5
# while i<=100:
#     print(i)
#     i+=5

# n=int(input("enter the limit"))
# i=1
# while i<=n:
#     print(i)
#     i+=2

#continue statment
# i=1
# while i<=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1

#pass
# i=0
# while i<5:
#     if i==5:
#         pass
#     print(i)
#     i+=1


# i=1
# n=1
# while i<=10:
#     n=n*i
#     i+=1
# print(n)
   

#Exc
#1
# i=1
# while i<=20:
#     if i==10:
#         break
#     print(i)
#     i+=1

#2
# i=1
# while i<=20:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

#3
# i=1
# while i<=10:
#     n=int(input("enter the numbers"))
#     if n<0:
#         break
#     print(i)
#     i+=1

#4
# i=10
# while i>=1:
#     print(i)
#     i-=1

#5
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

#6
# i=1
# while i<=20:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

#7
# n=int(input("enter the number:"))
# i=1
# s=1
# while i<=10:
#     s=i*n
#     print(s)
#     i+=1
   
#PRIME NUMBER
# n=int(input("enter a number"))
# i=2
# while i<=n:
#     if n%i==0:
#      print("not prime")
#      break
#     i+=1
# else:
#      print("prime")

#PALINDROME
# n=int(input("enter a number to be check:"))
# rev=0
# temp=n
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if temp==rev:
#     print("number is palindrome")
# else:
#     print("not palindrome")        

#2.FOR LOOP
# for i in range (1,23):
#  print(i)
      
# for i in range (2,11,2):
#  print(i)
 
#break
# for i in range(1,10):
#     if i==5:
#         break
#     else:
#         print(i)
# else:
#     print("looop endddddd")    


#Continue
# for i in range(1,10):
#     if i==5:
#         continue
#     else:
#         print(i)


#Reverse a string
# n=input("enter a string")
# reverse=""
# for char in n:
#     reverse=char+reverse
# if reverse==n:
#         print("string is palindrome")
# else:
#         print("string is not plindrme")    
# print("reverse is:",reverse)    



#Multiplication
# n=int(input("enter a number"))
# s=1
# for i in range(1,11):
#     s=i*n
#     print(i,"*",n,"=",s)
      


# n=int(input("enter a number"))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

# n=int(input("enter number"))
# count=0
# sum=0
# while n>0:
#     d=n%10
#     sum+=d
#     n=n//10
# print(sum)


# n=int(input("enter number"))
# pro=1
# while n>0:
#     d=n%10
#     pro*=d
#     n=n//10
# print(pro) 


# n=int(input("enter the number"))
# count=0
# sum=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)  
# temp=n
# while n>0:
#     d=n%10
#     sum+=d**count    
#     n=n//10
# print(sum)
# if temp==sum:
#     print("number is amstrong")
# else:
#     print("not amstrong")    

   

# n=int(input("enter number"))
# f=1
# while n>0:
#     f=f*n
#     n-=1
# print("factorial is",f)    



# n=input("enter a string")
# reverse=""
# for char in n:
#     reverse=char+reverse

# print(reverse)    


# #fibinoce series
# n=int(input("enter the limit"))
# a=0
# b=1
# print(a,b)
# for i in range(1,n):
    
#      c=a+b
#      a=b
#      b=c
#      i+=1
#      print(c)
         
    

     

# n=int(input("enter the number"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")    


# n=int(input("enter the start number"))
# m=int(input("enter the end number"))
# for i in range(n,m):
#     if i%2==0:
#         print(i)
#         i+=1
    



    #NESTED FOR LOOP
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)


# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")    
#     print()
  
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")    
#     print()

# for i in range(1,5):
#     for j in range(0,i):
#         print("*",end=" ")    
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")    
#     print()

 



#////STRINGS///////


#OPERATOR in String


# a="welcome"
# b="everyone"
# print(a,""+b)
       
# a="welcome"
# b="everyone"
# print(b*4)


# a="welcome"
# b="everyone"
# print("e"not in a)
# print("w" in b)    
# print("l" in a)

 #Index in string


# str="avanthika"
# print(str[6])
# print(str[0])
# print(str[-4])
# print(str[-7])

  #Slicing
# str="avanthika anil"
# print(str[0:9:2])
# print(str[:7])
# print(str[4:])
# print(str[0:11])



# str="datascience"
# print(str[::2])
# print(str[::-1])#//REVERESE OF string//#
# print(str[-1::-1])



# str="Programming in python"
# print(str[0:5])
# print(str[-4::])
# print(str[1:-1])
# print(str[2::2])
# print(str[1::2])
# print(str[::-1])


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")  
#     for k in range(i*2-1): 
#             print("*",end=" ")  
#     print()

# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")  
#     for k in range(i*2-1): 
#             print("*",end=" ")  
#     print()



# for i in range(5):
#     for j in range(i+1):
#         print(2*i,end=" ")    
#     print()


# for i in range(1,6):
#     for j in range(i):
#         if i%2==0:
             
#             print(2,end=" ")   
#         else:
#              print(1,end=" ") 
                 
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()       

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print() 
    
# for i in range(6):
#     for j in range(i+1):
#         print(i*2,end=" ")
#     print() 



# str="data science"
# # print(str[0],str[-1])
# l=len(str)
# print(str[l//2])
# print(str[::-1])
# pal=str[::-1]
# if pal==str:
# #     print("its palindrome")
# # else: 
# #     print("not pal")
# # print(str[1:-1])/
#     if str[i]=="a" or str[i]=="e"or str[i]=="i" or str[i]=="o" or str[i]=="u":
#         count+=1
# print(count)  
# print(str[-1::-2])
# str="datascience helloooo"
# l=len(str)
# count=0
# for i in range(l):
#    if str[i]==" ": 
#       count+=1
# print(count)
# if l==0:
#     print("empty")
# else:
    # print("not empty")  
# print(str[:l//2])
# print(str[l//2::])




#CASE CONVERSION METHOD

# s="heEellpp meEe"
# 1.#upper()
# # print(s.upper())
# 2#lower()
# # print(s.lower())
# 3.#capitalize()
# # print(s.capitalize())
# # 4.title()
# # print(s.title())
# # 5.swapcase()
# # print(s.swapcase())



#VALIDATION OR CHECKING METHODE
# s="23456"
# # 1.isupper()
# print(s.isupper())
# #2.islower()
# print(s.islower())
# #3.istitle
# print(s.istitle())
# #4.isalpha()
# print(s.isalpha())
# #4.alnum()
# print(s.isalnum())
# #6.isspace
# print(s.isspace())
# #7.isdigit()
# print(s.isdigit())
# #8.isnumeric()
# print(s.isnumeric())
# #9.isdecimal
# print(s.isnumeric())



#SEARCH AND VALIDATION METHOD

# s="avanthi hellooo"
# # 1.find()
# print(s.find("d"))
# #2.index()
# print(s.index("h"))
# #3.rindex()
# print(s.rindex("h"))
# #4.rfind()
# print(s.rfind("t"))
# #5.count()
# print(s.count("m"))
# #6.startswith
# print(s.startswith("hello"))
# #7.endswith
# print(s.endswith("llooo"))


 
   #Modification And Replace  
# 1.#replace
# s="helpppppme  from  everything"
# print(s.replace("e","a"))
# 2.strip
# print(s.strip())
#3.lstrip
# print(s.lstrip())
#4.rstrip
# print(s.rstrip())
#5.split
# print(s.split(" "))
#6.rsplit
# print(s.rsplit(",",2))
# l=["apple","banana","guva"]
# print("  ".join(l))/





      #Alignment function Or Padding Function 

# s="\n"
# # 1.ljust
# print(s.ljust(14,"*"))
# #2.rjust
# print(s.rjust(12,"*"))
#3.center
# print(s.center(12,"*"))
#4.zfill
# print(s.zfill(9))    
# 5.isascci
# print(s.isascii())
# 6.isprintable
# print(s.isprintable())   //for escape character(\n,\t,\b)