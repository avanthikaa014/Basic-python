# s={1,2,3,4,5,6}
# print(s)

# s={1,2,3,4,4,5,6,6.}       #/ NO DUPLICATION ,it return only unique values/
# print(s)

# a={'a',1,0,True,False,"hi"}
# print(a)   #///set is unorderd,true and false will be treated as 1,0//



#Add an element to the set
# s={1,2,3,4}
# s.add(6)
# print(s)


#set in muttable so we can add and remove elements
  

#Remove element from a set 
# s={1,2,3,4,5}
# s.remove(4)
# print(s)


# -----------------
# Union
# -----------------
# s={1,2,3,4}
# p={5,6,7,8}
# x=s.union(p)
# print(x)
# print(s|p)


# # ------------
# # Intersection
# # -------------
# s={1,2,3,4,5}
# p={3,4,5,6,7}
# x=s.intersection(p)
# print(x)
# print(s&p)

# -------------
# Difference
# ------------
# s={10,20,30,40,50}
# p={30,40,50,60,70}
# x=s.difference(p)
# print(x)
# print(p-s)

# ------------
# Symmetric Difference
# -------------
# s={1,2,3,4,5,6,7}
# p={2,34,5,6,6}
# x=s.symmetric_difference(p)
# print(x)
# print(s^p)


# ------------------
# Intersection Update
# ------------------
# s={1,2,3,4,5,6}
# p={3,4,5,6,7}
# s.intersection_update(p)
# s &= p
# print(s)


# ------------------------
# Differece Update
# ----------------------
# s={1,2,3,4,5,6}
# p={3,4,5,6,7,8,9}
# s.difference_update(p)
# print(s)
# p-=s
# print(p)

# -------------------
# Symmetric Difference Update
# ----------------------
# s={1,2,3,4,5,6,7}
# p={2,34,5,6,6}
# s.symmetric_difference_update(p)
# print(s)



# ---------------------
# issubset,issuperset,isdisjoint
# --------------------
# s={1,2,3,4,5,6,7,8}
# odd={1,3,5,7}
# even={2,4,6,8}
# print(s.issubset(odd))
# print(odd.issubset(s))
# print(even.issubset(s))
# print(s.issuperset(odd))
# print(odd.issuperset(s))
# print(s.isdisjoint(odd))
# print(odd.isdisjoint(even))
# print(even.isdisjoint(s))

# -----------------
# discard
# -----------------
# odd={1,3,5,7,9}
# odd.discard(3)
# print(odd)
# odd.discard(4)
# print(odd.discard(4))


# ------
# copy
# ----------
# odd={1,3,5,7,9}
# x=odd.copy()
# print(x)


# # -------------
# # pop
# # ---------
# odd={1,3,5,7,9}
# x=odd.pop()
# print(x)



# ------------
# update
# ----------
# odd={1,3,5,7,9}
# even={2,4,6,8}
# odd.update(even)
# print(odd)
# a={1,2,3}
# b=[3,4,5]
# a.update(b)
# print(a)



# ---------------------
# Questions
# ---------------------
1
# fruits={"apple","cherry","banana"}
# print(fruits)
# fruits.add("orange")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits.discard("banana")
# print(fruits)
# print("apple" in fruits)
# print(len(fruits))

2
# a = {1,2,3,4} 
# b = {3,4,5,6}
# s=a.union(b)
# print(s)
# t=a.intersection(b)
# print(t)
# x=a.difference(b)
# y=b.difference(a)
# print(x)
# print(y)
# x=a.symmetric_difference(b)
# print(x)

3.
# l=[1,2,2,3,4,4,5]
# s=set(l)
# print(s)
# l=list(s)
# print(l)

4.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.add(40)
# set1.add(50)
# print(set1)
# print(set1.issubset(set2))
# print(set1.issuperset(set2))

18.
# s1={1,2}
# s2={3,4}
# s3={5,6}
# print(s1|s2|s3)