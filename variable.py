#For string (string is a series of a character)
name="Shanjidul"
#you do not need to declare the variable type...it will understand the behavior  by the value
print(name)
food="burger"
print (f"Hi {name} and you like {food}")
#Here 'f' is f-string...f = format

#Integer (Integer is a hole number)
age = 10
print(age)
print(f"Hello {name}, you like {food} and your age is {age}")

#Float
price = 100.99
print (price)
print(f"Hello {name}, you like {food}...it's price is ${price} and your age is {age}")

#Double
number1=22.5
number2=3.1416
sum=number1+number2
minus=number1-number2
mul=number1*number2
div=number1/number2
print(f"I like to print two numbers {number1} and {number2}")
print(f"The sum is {sum}\nminus between these number is {minus}\nmultiplication is {mul} and the division is {div} ")

#Boolian
answer=True
if answer:
    print("The answer is true")
else :
    print("The answer is not true")

#code
print(f"This is a random code by {name}")
num1=3.1416
num2=10.88
num3=30
sum=num1+num2+num3
avg=(num1+num2+num3)/3
print(f"The sum is {sum}")
if (avg<20):
    print("The average of this number is not 20")
else:
    print("The average of the numbers is bigger then 20")


