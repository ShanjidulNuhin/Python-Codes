import math

x=10.88
print(math.pi)#The value of pi=3.1416....
print(math.e)#The value of e =2.71....
print(math.sqrt(x))#Square root
print(math.ceil(x))#Ceiling value
print(math.floor(x))#Floor value

#Exercise
red=float(input("Enter the radius of a circle: "))
result=2*math.pi*red
print(f"The circumference of the circle is = {result}")

#Exercise2
num1=float(input("Enter any number: "))
num2=float(input("Enter another number: "))
result=math.sqrt(pow(num1,2)+pow(num2,2))

print(f"You enter two numbers are {num1} and {num2}")
print(f"The square root of all number square is {result} ")