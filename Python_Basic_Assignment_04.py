#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.What is exactly [] ?

it is an empty list.


# In[8]:


# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
#    third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam = [2, 4, 6, 8, 10]


# In[9]:


spam.insert(3, 'hello')


# In[10]:


spam


# In[11]:


# 3. What is the value of spam[int(int('3' * 2) / 11)]?

[int(int('3' * 2) / 11)]

# '3' is in string and data type int is given that's why result is not right. answer come in float datatype.


# In[12]:


# 4. What is the value of spam[-1]?

spam[-1]


# In[13]:


# 5. What is the value of spam[:2]?

spam[:2]


# In[14]:


bacon = [3.14, 'cat', 11, 'cat', True]


# In[15]:


# 6. What is the value of bacon.index('cat')?

bacon.index('cat')


# In[16]:


# 7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)


# In[17]:


bacon


# In[18]:


# 8. How does bacon.remove('cat') change the look of the list in bacon?

bacon.remove('cat') 


# In[19]:


bacon


# In[ ]:


# 9. What are the list concatenation and list replication operators?

for list concatenation is  +
and for list replication   *


# In[ ]:


# 10. What is difference between the list methods append() and insert()?

append is used for adding an element in a list but we can add in end of the list.

insert is also used for adding an element in a list but we can add an element in between or anywhere in a list by specifying the position. 


# In[ ]:


# 11. What are the two methods for removing items from a list?

clear()
pop()
remove()


# In[ ]:


# 12. Describe how list values and string values are identical.

list values are identify by this [] bracket.
numbers in the list.

string values are identify by this '' or this "" symbol.
characters in the string.


# In[ ]:


# 13. What's the difference between tuples and lists?

tuples are immutable.

lists are mutable.


# In[20]:


# 14. How do you type a tuple value that only contains the integer 42?

t = (42)


# In[21]:


t


# In[ ]:


# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

by using function name() is used to convert the tuples to list and create a list of tuples
and convert list to tuples and create a tuple list.


# In[ ]:


# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

variables will contain references to list values. 


# In[ ]:


# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

copy create reference or duplicate to original object if you changed copied object you change the original object.
deepcopy creates new object and makes a new copy and if you changed copied object the original one is not affect.

