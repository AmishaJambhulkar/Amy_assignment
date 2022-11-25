#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.In the below elements which of them are values or an expression? eg:- values can 
# be integer or string and expressions will be mathematical operators.


*       expression

'hello' string

-87.8   float

-       expression

expression()

+       expression

6       integer 



expression: *, -, /, +
values: 'hello', -87.8, 6


# In[ ]:


# 2. What is the difference between string and variable?

string - strings are type of data that can be store in a variable and it is denoted by single or double quote.

variable - variables use to store data in a program.


# In[ ]:


# 3. Describe three different data types.

integer(int) - it holds numeric data -> only whole numbers. eg: 11, 3232, 96086
    
float - it holds numeric data but with decimal point. eg: 5.98, 3.086, 43.097
    
boolean(bool) - occupies only two terms -> True/False 


# In[ ]:


# 4. What is an expression made up of? What do all expressions do?

expression are used to perform mathematical operation
eg: a=i+4, 12+5*9


# In[ ]:


# 5. The assignment statements, like spam = 10. What is the difference between an expression and statement?

expression - expression are use for mathematical operation and it gives return in result value

statement - whatever we want to print it prints as it is 


# In[2]:


# 6. After running the following code, what does the variable bacon contain?
   
bacon = 22

bacon + 1


# In[3]:


# 7. What should the values of the following two terms be?      
#   'spam' + 'spamspam' 
#   'spam' * 3 

'spam' + 'spamspam'


# In[4]:


'spam' *3 


# In[ ]:


# 8. Why is eggs a valid variable name while 100 is invalid?

because variable name cannot start with a numeric digit


# In[5]:


# 9. What three functions can be used to get the integer, floating-point number, or string version of a value? 

x = 421

int(x) , float(x) , str(x)


# In[6]:


# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten'+99+'burrritos.'

'I have eaten'+99+'burrritos.'   # we can use str(99) or '99'.


# In[8]:


'I have eaten' + '99' + 'burrritos.'

