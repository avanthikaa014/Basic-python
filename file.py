# Creating a File And Read the File
# f=open("ds.txt","w")
# f.write("\nyou going to be okay")
# f.close()


# Reading File
# f=open("ds.txt","r")
# print(f.read())
# f.close()


# f=open("ds.txt","a")
# f.write("\nyou are bravwst person \nalso you can do anything that u want ")
# f.close()

# Reading File
# f=open("ds.txt","r")
# print(f.readlines())
# f.close()


# f=open("ds.txt","r")
# print(f.tell())
# print(f.read(5))

# f=open("ds.txt","a")
# f.write("hai")
# print(f.tell())
# f.close()

# f=open("ds.txt","w")
# f.write("[apple,banan,orange]")
# f=open("ds.txt","r")
# print(f.read())
# f.close()

# f=open("ds.txt","w")
# for i in range (1,100):
#     f.write(str(i)+"\n")
# f.close()

# f=open("ds.txt","w")
# f.write("hello avanthika")
# f.close()
# f=open("ds.txt","r")
# count=0
# for i in f.read():
#     if i !=" " and i!="\n":
#         count+=1
# print(count)    
# f.close()    


# f=open("ds.txt","r")  
# count=0
# for i in f.readlines():
#    count+=1
#    print(i)
# print(count)      
# f.close()

# f=open("ds.txt","w")
# for i in range(1,11):
#     f.write(str(i))
#     f.write("* 5 =")
#     f.write(str(i*5)+"\n")
# f.close()    


# f=open("ds.txt","a")
# for i in range(1,11):
#     f.write(str(i))
#     f.write("* 10 =")
#     f.write(str(i*10)+"\n")
# f.close()    


# import os
# os.remove("ds.txt")
# os.rmdir("folder name")

# import shutil
# shutil.rmtree("filename")


# with open("ds.txt","w")as f:
#     f.write("hello my  name is avanthika""\n")
#     f.write("iam 22 year old""\n")
#     f.write("going very well")    
# with open("ds.txt","r")as f:
#     print(f.read())



# def mark_attendance():

#     emp_id = input("Enter Employee ID : ")

#     name = input("Enter Employee Name : ")
#     date = input("Enter date : ")

#     status = input("Enter Attendance (Present   // Absent ) : ")

#     f = open("attendance.txt","a")

#     f.write(emp_id)

#     f.write("  ")

#     f.write(name)

#     f.write("  ")

#     f.write(status)

#     f.write("  ")

#     f.write(date)

#     f.write("\n")


#     f.close()



# def view_attendance():
#    f = open("attendance.txt","r")
#    for i in f.readlines():
#       print(i)
#    f.close()



# def attendance_summary():
#     f = open("attendance.txt","r")
#     a=0
#     p=0
#     for i in f.readlines():
#         s=[]
#         s=i.split(" ")
#         if "absent" in s:
#             a+=1
#         else :
#             p+=1
#     print("No of Absent :  ",a)
#     print("No of Present : ",p)
#     f.close()



# while True :
#   print("\n   Attendance   ")
#   print("1. Mark Attendance")
#   print("2. View Attendance Records ")
#   print("3. Attendance Summary ")
#   print("4. Exit ")
#   choice = int(input("Enter Choice : "))
#   if choice == 1 :
#    mark_attendance()
#   elif choice == 2 :
#    view_attendance()
#   elif choice == 3 :
#    attendance_summary()
#   else :
#    print("Thank You for Visiting ")
#   break