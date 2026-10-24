# t=(5)
# print(t)
# print(type(t))

# a=(5,"ammy",True,0.3)
# print(t)
# print(type(a))               /multiple datatype can access is single tuple



# t=(10,20,30,40)
# print(t[0])
# print(t[1])
# print(t[1:3])   #slicing
# print(len(t))


# t=(10,20)
# t1=(30,40)         
# print(t+t1) #Concatination
# print(t*3)  #Repetation
# print(10 in t)
# print(20 not in t1)    #membership function


# --------------------
# Tuple Method
# --------------------
# 1.count()
# t=(1,2,2,2,3,4)
# print(t.count(2))


# # 2.index()
# print(t.index(3))




# /// Change element in a tuple by changing it into a list///
# t=(1,2,3,4,5)
# l=list(t)
# print(l)
# l.append(6)
# print(l)
# t=tuple(l)
# print(t)

# -------------------
# #Nested Tuple
# ------------------

# n=(1,(2,3,3),(4,5,6,7,8),9,10)
# print(n[2][4])
# print(n[1][0])
# print(n[2][1])
# print(n[0])
# print(n[1])
# print(n[2])
# print(n[1][0:2])

# -----------------
# Packing And Unpacking
# # --------------------
# stu=("Alice",85,"A")
# name,mark,grade=stu
# print("name",name)
# print("grade",grade)
# print("mark",mark)


# -----------
# Questions
# -----------
#1.
# t=(10,20,30,40)
# print(t[0])
# print(t[3])
# print(t[0:4])

# 2.
# t=(1,2,3,4,5)
# s=list(t)
# s.append(6)
# print(s)
# t=tuple(s)
# print(t)


# 3.
# t=(1,2,3,4,5,6)
# print(min(t))
# print(max(t))

#4.
# t=(1,2,2,3,4,5)
# print(t.count(2))

5.
# t=(1,2,3)


6.
# t1=(1,2,3)
# t2=(4,5,6)
# t1,t2=t2,t1
# print(t1,t2)

7.
# t=(1,2,3,[4,5])
# s=list(t)
# s[3]=[6,7]
# print(s)
# t=tuple(s)
# print(t)

8.
# t =(42,56,47,32,58,12,95,75,2)
# s=list(t)
# s.sort()
# t=tuple(s)
# print(t)

9.
# t=(1,2,3)
# t2=(4,5,6)
# sum=tuple(i+j for i in t for j in t2)
# print(sum)

10.
# t = (1,2,2,3,4,4,5)
# s=set(t)
# t=tuple(s)
# print(t)

11
# t=(1,2,3,4,5,6,7,8,9)
# s=tuple(i for i in t if i%2==0)
# print(s)

