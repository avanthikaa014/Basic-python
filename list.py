# l=[1,2,3,4,5]
# print(l)

# n=list((1,3,4,5))
# print(n)


# -----------------
# LIST OPERATOR
# -----------------

# 1.CONCATENATION
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# s=l1+l2
#  print(s)
# print(l1+l2)

# 2.REPITATION
# l1=[1,2,3,4]
# s=4*l1
# print(s)
# print(4*l1)

# 3.MEMBERSHIP 
# l=[1,2,3,4,5]
# print(2 in l)
# print(5 not in l)

#string to list
# n="hello my name is avanti"
# l=list(n)
# print(l)

#Slicing of list 
# n=["apple","banana","guva","pineapple"]
# print(n[0])
# print(n[0:4])
# print(n[-1])
# print(n[::-1])

# ----------------------------
# List Iteration
# ----------------------------
# l=[100,200,300,400]
# for i in l:
#     print(i)


# for j in range (len(l)):
#     print(j)  #index printing
 # print(l[j]) #item printing
# -----------------------------------


# ------------------------------------
# LIST METHODE
# ----------------------------------------

# Adding method
# -----------------

#1.append
# -----------------
# l=[1,2,3,4,5]
# l.append(6)
# print(l)
# l.append(["apple","orange"])        #//add the list into one index
# print(l)
# l.append("end")
# print(l) 

#2.Insert
# ----------------
# l=[1,2,3,4,5]
# l.insert(2,7)
# print(l)
# l=["ammu","achu","allu"]
# l.insert(3,"nichu")
# print(l)

#3.Extend
# ----------------
# l1=[1,2,3,4,5]
# l2=[6,7,8,9]
# # l1.extend(l2)
# # print(l1)
# # l1.extend((4,5))
# # print(l1)
# l1.extend(("end")) #//insert single character into single index
# print(l1)


#Removing method
# -------------------

#1.Remove - list.remove(item)
# l=[10,20,30,40]
# l.remove(20)
# print(l)

#2.pop - list.pop(index)
# l=[1,2,3,4,5]
# l.pop(3)
# print(l)

# l.pop(0)
# print(l)

# l.pop()
# print(l)

# 3.clear
# l=[1,2,3]
# l.clear

#SEARCHING
# -------------------------------

#index() - list.index(item,start,end)
#-------------------------------------
# l = [250,650,100,500,100,200,300,400,500]

# print(l.index(100))
# print(l.index(300,0,4))
# print(l.index(400,0,2)) # if unknown index mentions an error occurs

#count() 
#------------------
# print(l.count(100))
# print(l.count(450)) #if unknown item mentions it return 0
#---------------------------------------------------------------

#SORTING METHODS
#-----------------------------

#sort() - ascending order
#----------------------------
# l.sort()
# print(l)
# l.sort(reverse=True)   #descending order
# print(l)

# a=["apple","orange","kiwi","banana"]
# a.sort(key=len,reverse=True)              #sort string based on length
# print(a)
# a.sort(key=len)
# print(a)

#reverse()- reverse of string order
#--------------------------------------
# l.reverse()
# print(l)
#------------------------------------------------------------

#copy() - copy list
#-------------------------

# a = l.copy()
# print("list is ",a)





# ----------------------------------------
# LIST OF LIST
# ----------------------------------


# l=[[1,2,3],[4,5,6],[7,8,9]]
# print(l)
# print(len(l))
# for i in l:
#     for j in l:
#         print(j, end=" ")
#     print()



# a=[10,20,30,[100,200,[5000,6000],300,400,500],40,50]
# print(a[3][0])
# print(a[3][2])
# print(a[3][2][1])
# print(a[3][2].append(7000))

# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[9,8,7],[6,5,4],[3,2,1]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range (len(a)):
#     for j in range (len(a[0])):
#         result[i][j]=a[i][j]+b[i][j]

# print(result)


# ----------------------------------------- 
#MATRIX ADDITION
# -----------------------------------------
# matrix1=[]
# row1=int(input("enter no of row:"))
# column1=int(input("enter no of clom:"))
# for i in range(row1):
#     sub1=[]
#     for j in range(column1):
#         user1=int(input("enter the items:"))
#         sub1.append(user1)
#     matrix1.append(sub1)    
# print(matrix1)
# for i in matrix1:
#     for j in i:
#         print(j,end=" ")
#     print()    

# matrix2=[]
# row2=int(input("enter no of row:"))
# column2=int(input("enter no of clom:"))
# for i in range(row2):
#     sub2=[]
#     for j in range(column2):
#         user2=int(input("enter the items:"))
#         sub2.append(user2)
#     matrix2.append(sub2)    
# print(matrix2)
# for i in matrix2:
#     for j in i:
#         print(j,end=" ")
#     print()        

# result=[]
# sub=[]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1)):
#         x=matrix1[i][j]+matrix2[i][j]
#         sub.append(x)
#     result.append(sub)
# print(result)
# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print()


# -----------------------------------------------
# MATRIX MULTIPLICATION
# -----------------------------------------------
# matrix1=[]
# row1=int(input("enter no of row:"))
# column1=int(input("enter no of clom:"))
# for i in range(row1):
#     sub1=[]
#     for j in range(column1):
#         user1=int(input("enter the items:"))
#         sub1.append(user1)
#     matrix1.append(sub1)    
# print(matrix1)
# for i in matrix1:
#     for j in i:
#         print(j,end=" ")
#     print()    

# matrix2=[]
# row2=int(input("enter no of row:"))
# column2=int(input("enter no of clom:"))
# for i in range(row2):
#     sub2=[]
#     for j in range(column2):
#         user2=int(input("enter the items:"))
#         sub2.append(user2)
#     matrix2.append(sub2)    
# print(matrix2)
# for i in matrix2:
#     for j in i:
#         print(j,end=" ")
#     print()        

# result=[]
# for i in range(row1):
#     row=[]
#     for j in range(column2):
#         sum=0
#         for k in range(column1):
#             sum+=matrix1[i][k]*matrix2[k][j]
#         row.append(sum)
#     result.append(row)
# print("product of matrix")    
# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print()    




# ------------------------------------------------------  
# TRANSPORS
# ------------------------------------------------------
# matrix1=[]
# row1=int(input("enter no of row:"))
# column1=int(input("enter no of clom:"))
# for i in range(row1):
#     sub1=[]
#     for j in range(column1):
#         user1=int(input("enter the items:"))
#         sub1.append(user1)
#     matrix1.append(sub1)    
# print(matrix1)
# for i in matrix1:
#     for j in i:
#         print(j,end=" ")
#     print()    

# matrix2=[]
# row2=int(input("enter no of row:"))
# column2=int(input("enter no of clom:"))
# for i in range(row2):
#     sub2=[]
#     for j in range(column2):
#         user2=int(input("enter the items:"))
#         sub2.append(user2)
#     matrix2.append(sub2)    
# print(matrix2)
# for i in matrix2:
#     for j in i:
#         print(j,end=" ")
#     print()   
# transpose=[]         
# for j in range(column1):
#     row=[]
#     for i in range(row1):
#         row.append(matrix1)
#     transpose.append(row)  
# print("Transposed Matrix:")
# for i in transpose:
#     for j in i:
#         print(j,end=" ")
#     print()
