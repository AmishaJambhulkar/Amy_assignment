#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.Why are functions advantageous to have in your programs?
 
We can avoid rewriting the same code again and again in a program.
In a single program we can call this fuction multiple times and it make task easy to us.
The fuction can be reused in program as well as can share and used by other programmers.


# In[ ]:


# 2.When does the code in a fuction run: when it's specified or when it's called?

# when the function it's called.


# In[ ]:


# 3.What statement creates a function?

def keyword is a statement for defining a function.
e.g.: def name ():
        return ___


# In[ ]:


# 4.What is the difference between a function and a function call?

A function is nothing but just a set of statements which is written as a block to perform a task.
function code can write once.

A function call is the code used to pass control to a function.
and we reused this function using function call.


# In[ ]:


# 5.How many global scopes are there in a Python program? How many local scopes?

There's only one 'global scope' and one 'local scope' in a Python program.


# In[ ]:


# 6.What happens to variables in a local scope when the function call returns?

when the function call returns then the local variables are destroyed.


# In[ ]:


# 7.What is the concept of a return value? Is it possible to have a return value in an expression?

A return statement is used to end the execution of the function call and returns result,
if the return statement is without any expression then the value none is returned.


# In[ ]:


# 8.If a function does not have a return statement, what is the return value of a call to that function?

after executing without return statement it gives a default return value as a result.


# In[ ]:


# 9.How do you make a function variable refer to the global variable?

by using global keyword


# In[ ]:


# 10.What is the data type of None?

None type


# In[ ]:


# 11.What does the sentence import areallyourpetsnamederic do?

import provide a liabrary or a module areallyourpetsnamederic


# In[ ]:


# 12.If you had a bacon() feature in a spam module, what would you call it after importing spam?

spam.bacon()


# In[ ]:


# 13.What can you do to save a programme from crashing if it encounters an error?

we use the try and except statements to handle an errors and exit from the process that caused error.


# In[ ]:


# 14.What is the purpose of the try clause? What is the purpose of the except clause?

Try and except clause are used to catch and handle exceptions.
the try clause lets you test a code until exception is encountered and except clause handle the error.

