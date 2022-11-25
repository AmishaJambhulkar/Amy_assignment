#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.What are the two values of the Boolean data type? How do you write them?

True and False are the two values of the Boolean data type. 
we have to specify that the first letter must be capital. 


# In[ ]:


# 2. What are the three different types of Boolean operators?

    and
    or
    not


# In[ ]:


# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
#    values for the operator and what it evaluate ).

True and True = True    True and False = False    False and True = False    False and False = False 

True or True = True     True or False = True      False or True = True      False or False = False 

not True = False        not False = True 


# In[ ]:


# 4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[1]:


(5 > 4) and (3 == 5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


# In[5]:


(True and True) and (True == False)


# In[6]:


(not False) or (not True)


# In[ ]:


# 5. What are the six comparison operators?

<   
>  
<= 
>= 
==  
get_ipython().system('=')


# In[8]:


# 6. How do you tell the difference between the equal to and assignment operators? Describe a
#    condition and when you would use one.

#    = its a assignment operator which used to assign a value to a variable.
#    == it represents equal to. 

#eg:
x = 11
y = 22
if x == y:
    print(True)
else:
    print(False) 
    
print('x =', x)
print('y =', y)


# In[ ]:


# 7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[9]:


spam = 0
if spam == 10:       # block 1
    print('eggs')
if spam > 5:         # block 2
    print('bacon')
else:                # block 3
    print('ham')
    print('spam')
    print('spam')


# In[10]:


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
#    Greetings! if anything else is stored in spam.

spam = int(input ('enter the spam numbers: '))
if spam == 1:
    print ('Hello')
elif spam == 2:
    print ('Howdy')
else:
    print ('Greetings!')


# In[ ]:


# 9.If your programme is stuck in an endless loop, what keys you’ll press?

ctrl+c


# In[ ]:


# 10. How can you tell the difference between break and continue?

break- break statement is used to terminate the loop
continue- continue statement is skip the current iteration and continue the next iteration in the loop


# In[11]:


# eg:
range(4)


# In[17]:


for i in range(4):
    if i==2:
        break
    print(i)
    
print('___________________')

for i in range(4):
    if i==2:
        continue
    print(i)      


# In[18]:


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

              ## no differnce shows in result.

for i in range(10):
    print(i, end=' ')
print()
for i in range(0,10):
    print(i, end=' ')
print()
for i in range(0,10,1):
    print(i, end=' ')


# In[19]:


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#     program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)


# In[20]:


i = 1
while i <= 10:
    print(i)
    i = i+1


# In[22]:


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

'spam.bacon()'

