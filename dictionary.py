
#//Dictionary mainly denoted as key value pairs//

# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# print(a)
# a["age"]=23   #//we can change the element ny calling the key
# print(a)


# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# for i in a:
#     print(a[i])

# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# a["mark"]=56
# print(a)
# print(a.values())
# print(a.keys())
# print(a.items())
# for i in a.items():
#     print(a.values())
# for key,value in a.items():
#     print(key,value)  


# ---------------
# Get function
# --------------
# print(a.get("name"))
# print(a.get("course"))
# print(a.get("place"))

# ---------
# clear
# --------
# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# a["mark"]=56
# # print(a)
# a.clear()
# print(a)

# ------------
# copy
# -----------
# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# a["mark"]=56
# x=a.copy()
# print(x)


# ----------
# pop
# ----------
# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# a["mark"]=56
# x=a.pop("course")
# print(x)
# print(a)


# ---------
# pop item
# ---------
# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# a["mark"]=56
# a.popitem()
# print(a)



# --------------
# update
# --------------
# a={
#     "anu":[20,"A"],
#     "manu":[23,"A+"]
# }
# a.update({
#     "anu":[22,"A+"],
#     "mins":[24,"A+"]
# })
# print(a)



# ----------------
# fromkeys
# -------------------
# x=["a",'b','c',"d"]
# z=dict.fromkeys(x,5)
# print(z)
# x=["a",'b','c',"d"]
# y=(1,2,3,4) 
# z=dict.fromkeys(y,x)
# print(z)



# ----------------
# setdefault
# ----------------
# a={"name":"ammu",
#    'age':22,
#    "course":"datascience"}
# print(a)
# x=a.setdefault("grade","B")
# print(a)



# -------------
# Questions
# ------------

1.
# y= [1,2,3]
# x=["ten","twenty","thirty"]    
# z=dict.fromkeys(x,y)
# print(z)

# 2.
# employees =["Kelly","Emma"]
# d= {"designantion": "Developer" , "Salary" :8000}
# z=dict.fromkeys(employees,d)
# print(z)

3.
# d={"ammu":{18,"A","kochi"},
#    "anu":{19,"B","calicut"},
#     "amz":{20,"A","kannur"}      
       
#    }
# print(d)

4.
# Dict1 ={"name" : "Ammu",
# 	"age": 20,
# 	"mark" : 86}
# Dict2 = {"Place" : "Kochi",
# "Course" : "Python",
# "Grade" : "A"}
# Dict1.update(Dict2)
# print(Dict1)


5.#///SWAP QUESTION///#
# a={"a":1,"b":2,"c":3}
# x={value:key for key,value in a.items()}
# print(x)

6.
# x={i:i**2 for i in range(1,11)}
# print(x)


7.
# x={i:i**2 for i in range(1,21) if i%2==0}
# print(x)


8.
# x={i:i**3 for i in range(1,11)}
# print(x)

9.
# l=["ammu","anu","sree"]
# x={i:len(i) for i in l}
# print(x)