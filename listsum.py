# def sumtwo (num,t):
#     idx=[]
#     for i in range(len(num)):
#         val=t-num[i]
#         if val in num:
#             idx.append(i)
#     return idx
# num=[2,7,11,15]
# t=9
# print(sumtwo(num,t))

# 1.py=two sum

# num=[2,7,11,15]
# t=9
# i=0
# idx=[]
# while i<len(num):
#     val=t-num[i]
#     if val in num:
#         idx.append(i)
#     i=i+1
# print(idx)

# num=[3,2,4]
# t=6
# i=1
# idx=[]
# while i<len(num):
#     val=t-num[i]
#     if val in num:
#         idx.append(i)
#     i=i+1
# print(idx)

# num=[3,3]
# t=6
# i=1
# idx=[]
# while i<len(num):
#     val=t-num[i]
#     if val in num:
#         idx.append(i)
#     i=i+1
# print(idx)

# # 2.py reverse

# i=123
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# print(rev)

# i=120
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# print(rev)

# # 3.py palindrom

# i=121
# rev=0
# x=i
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# if x==rev:
#     print("true")
# else:
#     print("flase")

# i=-121
# rev=0
# x=i
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# if x==rev:
#     print("true")
# else:
#     print("flase")

# i=10
# rev=0
# x=i
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# if x==rev:
#     print("true")
# else:
#     print("flase")

# # 4.py duplicates

# num = [1,1,2]
# i=0
# d=[]
# c=0
# p=[]
# while i<len(num):
#     if num[i] not in d:
#         c=c+1
#         d.append(num[i])
#         a=d+p
#     i=i+1
# print(c,'sum=',a)

# num =[0,0,1,1,1,2,2,3,3,4]
# i=0
# d=[]
# c=0
# while i<len(num):
#     if num[i] not in d:
#         c=c+1
#         d.append(num[i])
#     i=i+1
# print(c,'sum=',d)

# # q5.py remove Element

# nums = [3,2,2,3]
# i=0
# c=0
# while i<len(nums):
#     if nums[i]==3:
#         c=c+1
#         nums.remove(3)
#     i=i+1
# print(c,nums)

# nums = [0,1,2,2,3,0,4,]
# i=0
# c=0
# while i<len(nums):
#     if nums[i]==2:
#         nums.remove(2)
#     else:
#         c=c+1
#     i=i+1
# print(c,'nums=',nums)

# # q6.py search insert position

# num = [1,3,5,6]
# c=1
# while c<len(num):
#     if num[c]==5:
#         print(c)
#     c=c+1

# l1 = [2,4,3]
# l2 = [5,6,4]
# i=0
# num=[]
# s=0
# while i<len(l1):
#     num.append(l1[i]+l2[i])
#     i=i+1
# print(num)

# # q6.py valid parentheses

# per="()"
# b=len(per)
# so=0
# sc=0
# i=0
# while (i<b):
#     if per[i] == "(":
#         so+=1
#     if per[i] == ")":
#         sc+=1
#     i+=1
# if so==sc:
# 	print("true")
# else:
# 	print("flase")

# per="()[]{}"
# b=len(per)
# so=0
# sc=0
# i=0
# while (i<b):
#     if per[i] == "(":
#         so+=1
#     if per[i] == ")":
#         sc+=1
#     i+=1
# if so==sc:
# 	print("true")
# else:
# 	print("flase")

# per="(]"
# b=len(per)
# so=0
# sc=0
# i=0
# while (i<b):
#     if per[i] == "(":
#         so+=1
#     if per[i] == ")":
#         sc+=1
#     i+=1
# if so==sc:
# 	print("true")
# else:
# 	print("flase")

# # q7.py remove dublicate

# head = [1,1,2,3,3]
# i=0
# l=[]
# while i<len(head):
#     if head[i] not in l:
#         l.append(head[i])
#     i+=1
# print(l)

# head = [1,1,2]
# i=0
# l=[]
# while i<len(head):
#     if head[i] not in l:
#         l.append(head[i])
#     i+=1
# print(l)

# # q8.py happy number

# n=19
# i=n
# while n>9:
#     d=0
#     sum=0
#     while n!=0:
#         d=n%10
#         sum=sum=d**2
#         n=n//10
#     n=sum
# if sum==1:
#     print("true")
# else:
#     print("flase")

# n=2
# i=n
# while n>9:
#     d=0
#     sum=0
#     while n!=0:
#         d=n%10
#         sum=sum=d**2
#         n=n//10
#     n=sum
# if sum==1:
#     print("true")
# else:
#     print("flase")

i=1
while i<=10:
	a=1
	c=0
	while a<=i:
		if i%a==0:
			c=c+1
		a=a+1
if c==2:
    print(i,"prime number")
i=i+1 

# i=1
# c2=0
# while i<=10:
#     a=1
#     c=0
#     while a<=i:
#         if i%a==0:
#             c=c+1
#         a=a+1
#     if c==2:
#         c2+=1
#     i=i+1
# print(c2)                  M                                                                                                  BBBBBBBBBBBBBBBBBBBBBBBBB                  BBBBBBBBBBBBBBBBBBBBBBB                 BBBBBBV                                                                         B         a=a+1
#     if c==         a=a+1
#     if c== a=a+1
#     if c==a=a+1
#     if c==         a=a+1
#     if c==         a=a+1
#     if c== a=a+1
#     if c==