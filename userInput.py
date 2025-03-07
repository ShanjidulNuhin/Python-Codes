#cm²(Hold ALT+Num Lk+0178)
n=input("Enter any number :  ")
print(n)
#here the number is enter as a string variable

number=int(input("Enter any number: "))#convert the number into integer
number+=1
print(number)

#Exericise
num=float(input("Enter any number : "))
num2=float(input("Enter another number: "))
sum=num+num2
mul=num*num2
sub=num-num2
div=num/num2
avg=(num+num2)/2

print(f"The sum of the numbers are {sum}")
print(f"The mutiplication of the numbers are {mul}")
print(f"The substriction of the numbers  are {sub}")
print(f"The division of the numbers are {div}")
print(f"The average of the numbers age {avg}")

x=33.5
y=-4
z=2
print(round(x))#round keyword will make a round number
print(abs(y))#absulute value is a distance away from 0 as a whole number
print(pow(z,3))#power
print(max(x,y,z))#maximum value
print(min(x,y,z))#minimum value
# Relational Operators
a = 50
b=100
print(a==b)
print(a!=b)
#Logical Operators
print(not(a<b))