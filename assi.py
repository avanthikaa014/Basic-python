def Mark_attendence():
    empid = input("enter the employe id:")
    name = input("enter employee name:")
    date = input("enter the date:")
    status = input("present/absent:")
    f=open("a.txt","a")
    f.write(empid)   
    f.write(" ")
    f.write(name)
    f.write(" ")
    f.write(status)
    f.write(" ")
    f.write(date)
    f.write("\n")
    f.close()
def View():
    f=open("a.txt","r")    
    for i in f.readlines():
        print(i)
    f.close()    
def Sum():
     f=open("a.txt","r")
     abs=0
     pre=0
     for i in f.readlines():
         set=[]
         set=i.split(" ")
         if "present" in set:
             pre+=1
         else:
             abs+=1 
     print("no of present",pre) 
     print("no of absect",abs)       
     f.close()
while True:
    print("\tATTENDENCE\t")
    print("1.MARK ATTENDENCE")   
    print("2.VIEW ATT")   
    print("3.SUMMARY")  
    print("4.EXIT")  
    choice=int(input("enter the choice:"))
    if choice==1:
        Mark_attendence()
    elif choice==2:
        View()
    elif choice==3:
        Sum()
    else:
        print("THANK YOU")      
    break   
print("hello")
    