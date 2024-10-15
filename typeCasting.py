#Typecasting is the process to convert a variable from one datatype to another datatype
name="Shanjidul"
age =24
num=32.82

print(f"The name is {name}which is {type(name)}")
print(f"Your age is {age}, Which is a/an {type(age)}")
print(f"a random number is {num}, which a/an {type(num)}")

#convert
age =float(age)
print(f"After converting the datatype the age is {age} which is a/an {type(age)}")
num=int(num)
print(f"After converting the datatype the number is {num} which is a/an {type(num)}")

