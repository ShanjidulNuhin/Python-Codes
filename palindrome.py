list1 = list(map(int, input("Enter some numbers separated by spaces: ").split()))
list_cop=list1.copy()
list_cop.reverse()
if(list_cop==list1):
    print("Palindrome")
else:
    print("Not Palindrome")


n = int(input("Enter some numbers: "))
list1 = []

for i in range(n):
    num = int(input(f"Enter {i+1} number: "))
    list1.append(num)

list_co = list1.copy()
list_co.reverse()

if list_co == list1:
        print("The list is palindrome!")
else:
    print("The list is not palindrome!")