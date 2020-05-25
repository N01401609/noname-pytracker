# Getting Started with Python
* Ensure your IDE is installed with Python 3.x.x
* Mac will come pre-installed with a legacy version of Python.  Do not touch that
* No curly bracets in Python.  Colon followed by an indentation on the next line will take their place. 
* You can run your code right in VSC or through the terminal if you are using a different IDE
* Make sure you are in the directory where the file is located
* Enter: python3 then the the file name(ie/ helloworld_start.py)
Comments in python are declared using the pound symbol(#)

## Variables
Python is a strongly typed language
ex/ you cannot combine types (int and string)
You can declare a variable as global with the keyword global
You can undefine a variable in real time with the keyword del

## Functions


### Defining a basic function
```python
	def func1()
		print ("I am a funtion")
```
### Defining a function that returns a value
```python
	def cube(x)
		Return x*x*x
```
### Defining functions that takes arguments
```python
	def funct2(arg1, arg2)
		print(arg1, “ “, arg2)
```
### Define function with default value for an argument
```python 
	def power(num, x=1)
		result = 1
	for i in range(x):
		result = result * num
		return result 
```

The star symbol (*) means you can pass in a variable number of arguments. Each variable will just be added to a running total then returned at the end

## Conditional Structures
* elif has replaces else if
* No replacement for switch place block in python
* Conditional statement lets you use “a” if condition else “b”

## Loops
* Python only has the while loop and the for loop
* For loop does not have the loop counter variable
* The loops are iterators.  

### You give it the range(the start point and when to end)
```python
   for x in range(5, 10):
      print(x)
```



### You can loop over a collection or Array (will print the elements of the array)
```python
 days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
 for d in days:
   print (d)
```

### Using the break statement in a loop (will only print 5, 6 then exit the loop)
```python
for x in range(5, 10):
   if(x==7): break
   print(x)
```

### Using the continue statement in a loop (will only print 5, 7, 9)
```python
for x in range(5, 10):
  if(x%2 == 0):continue
   print(x)
```

Since there is no iteration, if you need the indexes you will have to enumerate your loop 

### Using enumerat to print an indexed list of the days of the week)
```python
   days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
   for i,d in enumerate(days):
   print (i,d)
```

## Classes
Inside a class you can define functions, just like you would define any other function
```python
   class myClass():
   def method1(self):
       print("myClass method1")
   
   def method2(self, someString):
       print("myClass method2" + someString)
```
The first argument in a method in a class is the ‘self’ argument
The self argument refers to the particular instance of the object being operated on (like the ‘this function in JS)
You don’t need to pass an argument for the ‘self’ arg, just the defined arguments

Classes can inherit other classes (the class ‘anotherClass’ is inheriting ‘myClass’
```python
class anotherClass(myClass):
```

