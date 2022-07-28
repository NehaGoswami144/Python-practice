#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
# Hints: Consider use range(#begin, #end) method 
# 

# In[5]:


a=range(2000,3201)
b=()
for i in a:
    if i%7==0 and i%5!=0:
        print(i,end=" ,")
    else:
        pass


# 2. Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
# Suppose the input is supplied to the program: 8 
# Then, the output should be: 40320 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# 

# In[15]:


n=int(input("Enter the value"))
def fac():
    x=1
    for i in range(1,n+1):
        x=x*i
    print (f"The factorial of {n} is : ",end="")
    print (x)
fac()


# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included) and then the program should print the dictionary. 
# Suppose the input is supplied to the program: 8 
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 
# 

# In[110]:


n=int(input("Enter your value /n:"))
d={}
def Dicti():
    for i in range(1,n+1):
        x=i*i
        k=i
        d.update({i,x})
        
        
        #print(i,x)
Dicti()


# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
# Suppose the input is supplied to the program: 34, 67, 55, 33, 12, 98 
# Then, the output should be: 
# ['34', '67', '55', '33', '12', '98'] 
# ('34', '67', '55', '33', '12', '98') 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple 
# 

# In[91]:


g=(input("enter your value")).split(",")
#g=list(map(34, 67, 55, 33, 12, 98 ))
d=list(g)
d
e=tuple(d)
e
print(d,e)


# 5. Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 
# Also please include simple test function to test the class methods. 
# Hints: Use __init__ method to construct some parameters 
# 
# 

# In[107]:


class Strin:
    def __init__(self):
        pass
    def getString(self):
        self.name=input("value")
    def printString(self):
        print(self.name.upper())
y=Strin()
y.getString()
print(y.printString())
        


# 6. Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18, 22, 24 
# Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) 
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 

# In[98]:


def CAL(D):
    C=50
    H=30
    Q =((2 * C * D)/H)**0.5
    
    k=round(Q)
    print(k)
        
CAL(100)

