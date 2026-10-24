# class Student:
#     name="Ammmu"
#     age=22
# s1=Student()
# S2=Student()
# print(s1.name)
# print(s1.age)    

# class Student:
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
# s1=Student("Alice",20)
# s2=Student("Anu",22)   
# print("Name:",s1.name) 
# print("age:",s1.age)      
# print(s2.name)


# class Employee:
#       def __init__(self,name,age,salary):
#             self.name=name
#             self.age=age
#             self.salary=salary
#       def display_employee_details(self):
#             print("Name:",self.name) 
#             print("age:",self.age) 
#             print(f"salary:",self.salary)
# e1=Employee("ammu",22,30000)  
# e2=Employee("sree",22,10000) 
# e1.display_employee_details()
# e2.display_employee_details()


# class Cars:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self)   :
#         print("brand:",self.brand) 
#         print("model:",self.model)
# c1=Cars("suzuki","swift")       
# c2=Cars("honda","city") 
# c1.display()
# c2.display()

# class Addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         sum=self.a+self.b    
#         print("sum is",sum)
# num=Addition(20,30)     
# num.add()   

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b  
#     def sub(self):
#             return self.a-self.b  
#     def mul(self):
#             return self.a*self.b  
#     def div(self):
#             return self.a/self.b  


# num=Calculator(20,30)     
# print("addition",num.add() )
# print("substraction",num.sub())
# print("multiplication",num.mul())    
# print("division",num.div())  
          
#inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking") 
# d1=Dog()
# d1.eat()   #//inherited method from Animal class//
# d1.bark()  # //Dog's own method         



# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
# class Mark(Student):
#     def __init__(self, name, rollno,maths,science):
#         super().__init__(name, rollno)
#         self.maths=maths
#         self.science=science

#     def display(self):
#          print("Name:",self.name) 
#          print("rollno:",self.rollno) 
#          print("maths:",self.maths) 
#          print("science:",self.science) 
# s=Mark("ammu",23,67,86)    
# s.display()     



#Multilevel inheritance
# class Grandparent:
#     def grand_info(self):
#         print("iam grand parent wher is my child")
# class Parent(Grandparent):
#     def parent_infoe(self):
#         print("iam parent where is my child")
# class Child(Parent):
#     def child_info(self):
#         print("iam the child wher is my parents")
# c=Child()
# c.parent_infoe ()   
# c.grand_info()
# c.child_info()


#Multiple Inheritance
# class Grandparent:
#     def grand_info(self):
#         print("iam grand parent wher is my child")
# class Parent(Grandparent):
#     def parent_infoe(self):
#         print("iam parent where is my child")
# class Child(Parent,Grandparent):
#     def child_info(self):
#         print("iam the child wher is my parents")
# c=Child()
# c.parent_infoe ()   
# c.grand_info()
# c.child_info()        


#MRO METHOD RESOLUTION ORDER
# class A:
#     def show(self):
#         print("Class A")
# class B(A):
#     def show(self):
#         print("Class B")
# class C(A):
#     def show(self):
#         print("Class C")
# class D (B,C):
#     pass
# print(D.__mro__)
# obj=D()
# obj.show()
# print(obj.show())



#Heirarichal Inheritence
# class parent:
#     def show(self):
#         print("iam the parent wher is my child")
# class child1(parent):
#     def show(self):
#         print("iam child 1")      
# class child2(parent): 
#     def show(self):
#         print("iam child 2")   

# c1=child1()  
# c2=child2()         
# c1.show()  
# c2.show()




# class Bank:
#     def details(self):
#         print("SBI")
# class Account(Bank):
#     def account_type(self):
#         print("savings account")        
# class Customer(Account):
#     def cust_info(self):
#         print("name is Ammu")          
#         print("age is 23") 
# obj=Customer()     
# obj.cust_info()   
# obj.account_type()
# obj.details()


# class Vehicle:
#     def info(self):
#         print("iam a vehicle")
# class Car(Vehicle):
#     def carinfo(self):
#         print("iam a car")   
# class electric(Car):
#     def battery(self):
#         print("i run on electricity")    
# obj=electric()
# obj.battery()
# obj.carinfo()
# obj.info()



# class Person :
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,rollno):
#         super().__init__(name)
#         self.rollno=rollno
# class Marks(Student):
#     def __init__(self,name,rollno,m1,m2,m3):
#         super().__init__(name,rollno) 
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def display(self):
#         print("Name : ",self.name)
#         print("RollNO : ",self.rollno)
#         print("Mark1 : ",self.m1)
#         print("Mark2 : ",self.m2)
#         print("Mark3 : ",self.m3)
#         print("Total :",self.m1+self.m2+self.m3)
# obj=Marks("Ammu",63,87,89,90)
# obj.display()


# class Company:
#     def company(self):
#         print("TATA")
# class Department(Company):
#     def depinfo(self):
#         print("Accounting dep")
# class Employee(Department):
#     def empinfo(self):
#         print("Name:Avanthika") 
#         print("Company ID:23")   
# obj=Employee()  
# obj.empinfo()
# obj.depinfo()
# obj.company()          


# class Item:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
# class Cart(Item):
#     def __init__(self, name, price,quantity):
#         super().__init__(name, price) 
#         self.quantity=quantity  
#         self.total=self.quantity*self.price
# class Cust(Cart):
#     def __init__(self, name, price, quantity,ctname):
#         super().__init__(name, price, quantity)
#         self.ctname=ctname
#     def display(self):  
#         print("name",self.name)
#         print("customer name",self.ctname)
#         print("price",self.price)
#         print("quatity",self.quantity)
#         print("total",self.total)
#         if self.total>5000:
#             self.s=self.total-((self.total/100)*20)
#             print("20 per discount",self.s)
#         elif self.total>2000:
#             self.s=self.total-((self.total/100)*10)
#             print("10 per discount",self.s)
#         else:
#             print("No Discount")    
# obj=Cust("apple",2000,4,"ammu")
# obj.display()


# class Vehicle:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
# class Cart(Vehicle):
#     def __init__(self, name, price,type):
#         super().__init__(name, price)
#         self.type=type
#         if self.type=="SUV":
#             self.excharge=100 
#         elif self.type=="Sedan":
#             self.excharge=60
#         else:
#             print("No car found")      
# class Rentcar(Cart):
#     def __init__(self, name, price, type,days):
#         super().__init__(name, price, type)
#         self.days=days 
#         self.total=(self.price*self.days)+self.excharge
#     def display(self):
#          print("name",self.name)   
#          print("Price",self.price)
#          print("Type:",self.type)
#          print("Days:",self.days)
#          print("extra charge",self.excharge)
#          print("Total Charge",self.total)
# obj=Rentcar("Inova",2000,"SUV",2)
# obj.display()         


        
# class Person:
#     def __init__(self,name,RollNo):
#         self.name=name
#         self.RollNo=RollNo
# class Exam(Person):
#     def __init__(self, name, RollNo,m1,m2,m3,m4,m5):
#         super().__init__(name, RollNo) 
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.m4=m4
#         self.m5=m5   
# class Result(Exam):
#     def __init__(self, name, RollNo,m1,m2,m3,m4,m5):
#         super().__init__(name, RollNo,m1,m2,m3,m4,m5) 
#         self.total=self.m1+self.m2+self.m3+self.m4+self.m5
#         self.avg=(self.total)/5
#         if self.total>90:
#             self.grade="A"
#         elif self.total>=80:
#             self.grade="B"  
#         elif self.total>=50:
#             self.grade="C"  
#         elif self.total<40:
#             self.grade="Fail"      
#     def display(self):
#          print("name",self.name)   
#          print("Roll",self.RollNo)
#          print("total",self.total)
#          print("Average",self.avg)
#          print("Grade",self.grade)
# obj=Result("AMMU",23,20,16,17,15,18)
# obj.display()         



#   ABSTRACTION
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape): 
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2    
# class Rect(Shape): 
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
# c1=Circle(5)    
# print("area is",c1.area())
# R1=Rect(5,6)
# print("arrea is",R1.area())
          


# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def __init__(self,cash):
#         self.cash=cash
#     def pay(self):
#         print(self.cash,"paid through UPI")
# class Card(Payment):
#     def __init__(self,cash):
#         self.cash=cash
#     def pay(self):
#         print(self.cash,"paid through card")  
# c=Card(500)           
# c.pay() 
# u=UPI(700)
# u.pay()




#ENCAPSULATION
#Acess Modifiers
# class Person:
#     def __init__(self,name,age):
#         self.name=name              ///PRIVATE VARIABLES
#         self.__age=age
# p1=Person("ammu",23)
# print(p1.name )
# print(p1.__age)       



# class Person:
#     def __init__(self,name,age):
#         self.name=name              //PROTECTED VARIABLES
#         self._age=age              
# p1=Person("ammu",23)
# print(p1.name )
# print(p1._age)    



#POLYMORPHISM
#run time polymorphism
# class Animal:
#     def makesound(self):
#         pass
# class Dog(Animal):
#     def makesound(self):
#         print("Woof!")
# class cat(Animal):
#     def makesound(self):
#         print("Meow")
# a=cat()    
# b=Dog()
# a.makesound()
# b.makesound()

#compile time Polymorphism
# class calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c    
# c=calculator()  
# print(c.add(2,4))  //this will call the second method,which except the three arguments
# and will raise the type error   
# print(c.add(3,2,4))  //this will call the second method and return 9


#Operator Overloading
# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other)  :
#         return Number(self.value+other.value)  
# n=Number(6)
# m=Number(7)   
# result=n+m 
# print(result.value )




# class BankAc:
#     def __init__(self,pbal):
#         self.__pbal=pbal
#     def deposite(self,dep):
#          self.__pbal+=dep
#          print("your amount",dep,"has been deposited succecsfully . And your current blance is :",self.__pbal)
#     def withdraw(self,wid):
#          if wid>self.__pbal:
#             print("your account has insufficient balance")
#          else:
#             self.__pbal-=wid
#             print("you current balance is",self.__pbal)    
# obj=BankAc(50000)    
# obj.deposite(20000)     
# obj.withdraw(60000)   



# class Car:
#     def start(self):
#         print("start with kaey")
# class Lap:
#     def start(self):
#         print("start with power Button")        

# a=Car()
# b=Lap()
# a.start()
# b.start()



# class Student:
#     def info(self):
#         print("Iam a Student")
# class Teacher:
#     def info(self):
#         print('Iam a Teacher')        
# class Principle:
#     def info(self):
#         print("iam The Princi")
# def displayinfo(objects):
#     for obj in objects:
#         obj.info() 
# people=[Student(),Teacher(),Principle()]     
# displayinfo(people)    

# class Employee:
#     def calsalary(self):
#         print("salary")
# class Manager(Employee):
#     def calsalary(self):
#        print("salary is 25k")

# class developer(Employee):
#     def calsalary(self):
#         print("salary is 35k")   


# m=Manager()
# d=developer()
# m.calsalary()
# d.calsalary()        

    
# class Patient:
#     def __init__(self,pid,pname,age):
#         self.pid=pid
#          self.pname=pname
#         self.age=age
#     def display(self) :   
#      print("Patient Name:",self.pname)
#      print("Patient Id:",self.pid)
#      print("patient age:",self.age)
# class Doctor:
#     def __init__(self,id,dname,speciality):
#         self.id=id
#         self.dname=dname  
#         self.speciality=speciality
#     def display(self) :   
#          print("DOC Name:",self.dname)
#          print("Doc Id:",self.id)
#          print("specialized:",self.speciality)     
# class Appoinment:
#     def __init__(self,date,time):
#         pass        
