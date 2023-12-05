#Taking input in python
n = input("Enter your name: ")
print("My name is: ", n)
print(type(n))   #by default string type

#wthout typecasting
a = (input("Enter marks in english: "))
b = (input("Enter marks in urdu: "))
print("Total marks = ", a + b)

#by default datatype is string so we typecast the input and also for operators peoblem
#typecasting in input() function
a = int(input("Enter marks in english: "))
b = int(input("Enter marks in urdu: "))
print("Total marks =", a + b)

#typecasting in print() function
a = input("Enter marks in english: ")
b = input("Enter marks in urdu: ")
print("Total marks =", int(a) + int(b))

#Taking input from console 
#student = input()
#print(student)

#Taking multiple inputs from user
#by split() method
std1 , std2, std3 = input("Enter the name of students: ").split()
print("The name of 1st student is: ",std1)
print("The name of 2nd student is: ",std2)
print("The name of 3rd student is: ",std3)

#by list comprehension
n = [int(n) for n in input("Enter 5 values here ").split(",")]
print("The values are:" , n)

j , k , l =  [int(j) for j in input("Enter the value: ").split()]
print("The value for j is:",j)
print("The value for k is:",k)
print("The value for l is:",l)

#output using print() function
print("I am a good girl.")

#print without new line
print("mamoonash00", end = "@")  #end parameter
print("gmail.com")

print("moon","milli","tanii", sep = " , ")   #sep parameter

print("Mamoona" , "VU" , "BSCS",sep = " _ " , end = " _ ")        #Combine end and sep parameter
print("4TH")


#output formatting
#using % operator
name = "Mamoona"           #string
surname = "Shamraiz"
print("Name:%s  Surname:%s" % (name,surname))


w = 45                     # int, float
h = 5.4
print("Weight is:%d  Height is:%f" % (w,h))

#using {} 
n = "Mamoona"
w = 45                     
h = 5.4
print("Name is: {}  Weight is: {}  Height is: {}".format(n,w,h))

print("Maham is a {} girl.".format('good')) 

print("{0} do work {1}.".format('Ali','hard'))

print(f"{'Moon'} and {'Maaz'}")

#vulunerability of input() function in python 2.x

#x = raw_input("Enter the value: ")                #in python 2
#print (type(x))

#in python 3
x = input("Enter a number:")
print("Number is: ",x)
print(type(x))

#Simple method
a = input("Enter name of ypur sybject: ")
print(a)

#using inbuilt stdin
import sys
print("Enter a number here: ")
name = sys.stdin.readline()
print(name)

#input of List of integer
list = []
size = int(input("Size of list is: "))
for x in range(size):
    z = (input("Enter the element:"))
    list.append(z)
print("List is:  ", list)












