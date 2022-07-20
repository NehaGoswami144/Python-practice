#!/usr/bin/env python
# coding: utf-8

# 1) Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# In[8]:


class vehicle:
    def __init__(blah,max_speed,mileage):
        blah.max_speed=max_speed
        blah.mileage=mileage
    def show(blah):
        print("max speed  is :",blah.max_speed,"milegae is:",blah.mileage)
obj=vehicle(120,57.9)
obj.show()


# 2) Create a Vehicle class without any variables and methods

# In[121]:


class vehicle:
        def show(self):
            pass
obj=vehicle()
obj.show()


# 3) Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# In[23]:


class vehicle:
    def __init__(blah,max_speed,mileage):
        blah.max_speed=max_speed
        blah.mileage=mileage
    def show(blah,name):
        print("max speed  is :",blah.max_speed,"milegae is:",blah.mileage)
class bus(vehicle):   
    def details(blah):
        print("bus details are:",blah.max_speed,blah.mileage)
obj=vehicle(120,89)
obj=bus(56,90)
obj.details()


# 4) Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# In[141]:


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
 


# 5) Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# 
# Use the following code for this exercise.

# In[150]:


class Vehicle:
    color="white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def show(self):
        print(f"Color: {Vehicle.color} Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
f=Vehicle("mercedes",210,75)
F=Vehicle("CTC Bus",210,75)
f.show()


# Create a class named Person, with firstname and lastname properties, and a printname method:

# In[20]:


class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printname(self):
        print(f"the full name of the person is {self.firstname} {self.lastname}")
x=Person("CHETAN","Sharma")
x.printname()
        
class Student(Person):
    def __init__(self,firstname,lastname,age):
        
        #self.firstname=firstname
        #self.lastname=lastname
        #Person.__init__(self,firstname,lastname)
        super().__init__(firstname,lastname)
        self.age=age
    def welcome(self):
        
        print(f"welcome {self.firstname} {self.lastname} of {self.age} year")
    
y=Student("Simran", "Kang",25)
y.welcome()


# Create a class named 'Student' with a string variable 'name' and an integer variable 'roll_no'. Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.

# In[64]:


class Student:
    name="john"
    roll_no=2
x=Student()
x.name


# Write a program to print the area and perimeter of a triangle having sides of 3, 4 and 5 units by creating a class named 'Triangle' with a function to print the area and perimeter.

# In[66]:


class Triangle:    
    
    
    def __init__ (self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def a(self):
        area= (1/2)*self.b*self.h
        perimeter= self.l+self.b+self.h
        print(area,perimeter)
        
        
t=Triangle(3,4,5)
t.a()


# Write a program to print the area of two rectangles having sides (4,5) and (5,8) respectively by creating a class named 'Rectangle' with a function named 'Area' which returns the area. Length and breadth are passed as parameters to its constructor.

# In[67]:


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def getarea (self):
        area=self.l*self.b
        print(area)
d=Rectangle(4,5)
f=Rectangle(5,8)
d.getarea()
f.getarea()


# Write a program by creating an 'Employee' class having the following functions and print the final salary.
# 1 - 'getInfo()' which takes the salary, number of hours of work per day of employee as parameters
# 2 - 'AddSal()' which adds $10 to the salary of the employee if it is less than $500.
# 3 - 'AddWork()' which adds $5 to the salary of the employee if the number of hours of work per day is more than 6 hours.

# In[111]:


class Employee:

    
    def getInfo(self,salary, number_of_hours):
        self.salary=salary
        self.number_of_hours=number_of_hours
    def AddSal(self):
        if self.salary<500:
            final_salary=self.salary+10
            print(final_salary)
        else:
            print(self.salary)
    def AddWork(self):
        if self.number_of_hours>6:
            final_salary=final_salary+5
            print(final_salary)
        else:
            print(self.salary)
    def final_sal(self):
        if self.number_of_hours>6 and self.salary<500:
            final_salary=self.salary+15
            print(final_salary)
        else:
            print(self.salary)
            
r=Employee()
r.getInfo(400,7)
r.final_sal()


# Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

# In[117]:


class Circle:
    def __init__(self,r):
        self.r=r
    def getArea(self):
        area=(22/7)*self.r**2
        print(area)
    def getCircumference(self):    
        Circumference=2*(22/7)*self.r
        print(Circumference)

c=Circle(4)
c.getCircumference()
c.getArea()


# In[155]:


class polygon:
    def __init__(self,shape,no_of_sides):
        self.shape=shape
        self.no_of_sides=no_of_sides
        
    def area_of_rec(self,length,bredth):
        area_of_Rectangle=self.length*self.bredth
        print(area_of_Rectangle)
    def area_sq(self,a):
        area_of_Square=self.a*self.a
        print(area_of_Square)
    def area_tri(self,h,b):
        area_of_tri=(1/2)*(self.b*self.h)
        print(area_of_tri)
#class rectangle(polygon):
    #def __init__(self,length,bredth):
        #self.length=length
        #self.bredth=bredth
    

ar=polygon(rectangle,2)
ar.


# In[ ]:




