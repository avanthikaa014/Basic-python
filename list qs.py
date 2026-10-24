# Questions

# l=[1,2,3]
# # l.append(4)
# # print(l)

# l.remove(3)
# print(l)

# l=[6,3,2,5,1]
# l.sort()
# print(l)

# l=[2,4,5,6,]
# s=len(l)
# print(s)


# l=[1,2,3,4]
# l.sort(reverse=True)
# print(l)

# l=[10,20,30,40]
# print(l[3])

# l1=[1,2,3,4]
# l2=[6,7,8]
# s=l1+l2
# print(s)
# l1.extend(l2)
# print(l1)

# l=[1,2,2,3,4]
# s=l.count(2)
# print(s)


# l=[1,3,4]
# l.insert(1,2)
# print(l)

# l=[1,2,3,4]
# s=[]
# for i in l:
#     s.append(i**2)
# print(s)  
    


#List Comprehension
# l=[1,2,3,4]
# s=[i**2 for i in l]
# print(s)
    
# s=[i**2 for i in range (1,11) if i%2==0]
# print(s)


# s=["even"if i%2==0 else"odd" for i in range (1,11)]
# print(s)

# l=['apple','banana','cherry']
# s=[i.upper() for i in l] 
# print(s)

# s="hi how are you"
# n=[i for i in s if i=="a" or i=="e" or i=="i" or i=="o" or i=="u"]
# print(n)


# n="my name is avanthi"
# s=n.split()
# print(s)
# l=[i[0] for i in s]
# print(l)

# l=[1,0,-3,4,-5]
# s=[i for i in l if i>0]
# print(s)

# l=[1,0,-3,4,-5]
# s=["0"if i< 0 else i for i in l  ]
# print(s)

# s=[(i,i**2) for i in range(1,11)]
# print(s)


# m=[i for i in range(2,51) if all (i%j!=0 for j in range(2,i))]
# print(m)
 
# s="avanthika"
# m=[i for i in s if i!=" " and s.count(i)==1]
# print(m)

# s=[i for i in range(1,100) if i%3==0 and i%5==0]
# print(s)

# a=[1,2,3]
# b=[4,5,6]
# s=[(i,j) for i in a for j in b]
# print(s)
  
# n="hell avanthika welcome"
# s=n.split(" ")
# l=[i for i in s if len(i)>4 ]
# print(l)

# n="hello my name is avanthika"
# s=n.split(" ")
# l=[(len(i),i) for i in s ]
# print(l)
 
# n=[2,3,4,5,6,7,8,9]
# l=[(i,i**2) for i in n if i%2!=0] 
# print(l)


# n=["avna","game56","ammaa4546"]
# l=[i for i in n if i.isalpha()]
# print(l)

# l=[1,2,3,4,5,6]
# l.pop(2)
# print(l)

# l=[1,2,3,4,5]
# l.clear
# print(l)

# l=[1,2,3,4,5]
# s=max(l)
# print(s)

# l=[1,2,3,4,5]
# s=min(l)
# print(s)


# l=[0,1,2,3,4,5]
# print(l[2] and l[4])


# l1=[1,2,3]
# l2=[4,5,6]
# print(l1+l2)

# l=[1,2,3,4,5]
# print(5 in l)
# print(4 in l)


# l=[1,2,3,4]
# l[1]=5
# print(l)

# l1=[1,2]
# l2=[3,4]
# print(l1+l2)

# l=[1,2,2,3,4,4,5]   
# s=set(l)
# print(s)
# l=list(s)
# print(l)

# s="hello"
# l=list(s)
# print(l)

# s="banana,apple,cherry"
# l=s.split(",")
# print(l)

# s=[1,2,3,4,5]
# sum=0
# for i in s:
#     sum=sum+i
# print(sum)    

# s=[i**2 for i in range(1,6)]
# print(s)
