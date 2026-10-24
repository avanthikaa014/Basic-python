
# ///SORT/////
# BUBBLR SORT
# def bubble(a):
#     n=len(a)
#     for i in range(n):
#         for j in range((n-1)):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# l=[3,6,5,1,8,2,9,11,10]
# sorted_array=bubble(l)
# print(sorted_array)

# SELECTION SORT
# def sel(a):
#     n=len(a)
#     for i in range(n):
#         min_inderx=i
#         for j in range(i+1,n):
#             if a[j]<a[min_inderx]:
#                 min_inderx=j
#         a[i],a[min_inderx]=a[min_inderx],a[i]
#     return a
# l=[3,5,1,2,6,9,4]
# sortarray=sel(l)
# print(sortarray)



# ///SORT///

# Binary Sort

# arr=[10,20,30,40,50,60,70,80]
# key=40
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==key:
#         print("element found")
#         break
#     elif key< arr[mid]:
#         high=mid-1
#     else:
#         low =mid+1
# else:
#     print("element not found")            


# Linear Sort

# def linear(a,target):
#     for i in range(len(a)):
#         if a[i]==target:
#             return i
#     return -1
# l=[3,2,6,8,9,1]
# t=9
# print("targer found at the position",linear(l,t))




#////Linked list//////
# singly linked list
# class Node:
    # def __init__(self,data):
    #     self.data=data
#         self.next=None
# node1= Node(10)     
# node2=Node(20)   
# node3=Node(30)
# node4=Node(40)
# head=node1
# node1.next=node2
# node2.next=node3
# temp=head
# while temp is not None:
#     print(temp.data, end=" ")
#     temp=temp.next


# # /////Doubly linked list
# class Node:
#         def __init__(self,data):
#            self.data=data
#            self.prev=None
#            self.next=None

# head=Node(10)
# second=Node(20)
# third=Node(30)

# head.next=second
# second.next=third

# second.prev=head
# third.prev=second
# print("forwerd traversal")
# temp=head
# while temp is not None:
#     print(temp.data, end=" ")
#     temp=temp.next

# print("backwerd traversal")    

# temp=third
# while temp is not None:
#      print(temp.data, end=" ")
#      temp=temp.prev



#////   Circular
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1= Node(10)     
# node2=Node(20)   
# node3=Node(30)
# node4=Node(40)
# head=node1
# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=head
# temp=head
# while True:
#     print(temp.data, end=" ")
#     temp=temp.next


#     if temp==head:
#         break




#//STACK//#

#// with out using function

# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# print("stack after push",stack)

# stack.pop()
# print("stack after pop",stack)

#// using funxtion
# stack=[]
# def Push():
#     n=int(input("enter the numbers"))
#     stack.append(n)
#     print("stack after push",stack)
# def Pop():
#     if len(stack)<=0:
#         print("stack is empty")    
#     else:
#         x=stack.pop()    
#         print("stack after pop",stack)
# Push()
# Push()
# Push()
# Push()
# Pop()
# Pop()


# //QUEUE//

# queue=[]
# queue.append("A")
# queue.append("B")
# queue.append("C")
# queue.append("D")
# print("enqueue",queue)

# delelement=queue.pop(0)
# print("deleted elemment",delelement)
# print("queue after deque ",queue)


