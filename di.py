#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 1
while(n==1):
    print(n)
    print('hello')
    n=2


# In[6]:


n=5
while(n!=6):
    n=int(input())
    if n==1:
        print('my number is 1')
    if n==2:
        print('my number is 2')
    if n==3:
        print('mjhjk')
    print('hello')


# In[8]:


for i in range(0,10):
    print(i)
    if i==5:
        break


# In[9]:


for i in range(0,10):
    if i==5:
        continue
    print("hello")
    print(i)


# In[7]:


print(n)


# In[2]:


n=2


# In[1]:


for i in range(2,100,2):
    if i%7==0:
        continue
    print(i)


# In[26]:


n=int(input())
i=2
while i<=n:
    if i%7==0:
        continue
    print(i)
    i=i+2
    


# i=1
# while i<3:
# j=0
# while j<5:
# 
# 

# In[5]:


n=int(input())
i=2
while i<=n:
    if i%7==0:
        i=i+2
        
        continue
    print(i)
    i=i+2
    


# In[15]:


i=1
while i<3:
    j=0
    while j<5:
        j=j+1
        if j==3:
            continue
        print(j,end=" ")
    i=i+1


# In[ ]:


i=1
while i<3:
    j=0
    while j<5:
        j=j+1
        
        if j==3:
            j=j+1
            continue
        print(j,end=" ")
    i=i+1


# In[27]:


i=1
while i<6:
    if i==4:
        i=i+1
        continue
    print(i,end=" ")
    i=i+1


# In[28]:


i=1
while i<6:
    if i==4:
        continue
    print(i,end=" ")
    i=i+1


# In[37]:


i=1
while i<10:
    if i==3:
        i=i+1
        continue
    
    print(i,end=" ")
    i=i+1


# In[57]:


l1=[1,2,3,4,5,6]
l1[0]
l1[2]
l1[0]=8
print(l1)
print(l1[1:5])
print(l1)


# In[74]:


l1=[1,2,3,4,5,6]
print(l1[1:4])
print(l1[1:])
print(l1[:])
print(l1[0:6])
print(l1[0:5])
l1.append("ram")
print(l1)
l1.insert(3,5)
print(l1)


# l2=[5,6,7,8,9]
# 

# In[76]:


l2=[5,6,7,8,9]
l2[:3]
l2[-1:]
print(l2[-1:])
l2[1:]
print(l2[1:])


# In[7]:


l1=[3,4,5,"ram",8,9]
for i in range l1:
    print(i)
    


# In[9]:


l1=[3,4,5,"ram",8,9]
for i in  l1:
    print(i)
    


# In[12]:


l1=[3,4,5,"ram",8,9]
for i in  l1:
    print(l1[i])


# n=int(input())
# li=[]
# for i in range (n) :
#     cur=int(input())
#     li.append(cur)
#     print(li)

# In[27]:


n=int(input())
li=[]
for i in range (n):
    curr=int(input())
    li.append(cur)
print(li)


# In[ ]:


p=int(input())
for i in range(p):
    str=input().split()
    n,m=int(str[0]),int(str[1])
    arr=[]
    for i in range(n):
        b=input().split()
        arrr=[int(x) for x in b]
        print(sum(arrr),end=" ")
    print()

