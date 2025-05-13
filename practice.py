#swaping of two numbers without changing of values of variable
#By using addition and subtractiom
# a=90
# b=88
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
# by using division and multiplication
# a=5678
# b=906
# a=a*b
# b=a//b
# a=a//b
# print(a,b)
# print(int(str(a)[::-1]))

# def reversenum(n):
#     reverse=0
#     while n>0:
#      digit = n%10
#      reverse=reverse*10+digit
#      n=n//10
#     return reverse
     
# number = int(input("Enter the number to be reversed "))
# print(reversenum(number))

        
# def power(base,exponent):
#     if exponent==0:
#         return 1
#     else:
#         return base*power(base,exponent-1)
# base = int(input("Enter the number"))
# exponent = int(input("Enter the exponent"))
# print(power(base,exponent))
# 

# palindrome string
# def palindrome(str):
#     str = str.replace(" ","").lower()
#     return str == str[::-1]
# # str = input("Enter the string \n")
# # print(palindrome(str))
# c= 'yash'
# # print(*c,sep='#')
# print("#".join(c))
# import math
# def perfectsqrt(num):
#     if num<0:
#         return -1
#     sqrt = math.isqrt(num)
#     if sqrt*sqrt == num:
#         return 1
#     else:
#         return -1
# num = (input("Enter the number \n"))
# print(intperfectsqrt(num))

# def rightangled(n):
#     for x in range(1,n+1):
#         print('*'*x)
# n=int(input("enter the value of n"))
# rightangled(n)

# def loop1(n):
#     for x in range(1,n+1):
#         if x==1 or x==n:
#             print("*"*n)
#         else:
#             print("*",end="")
#             print(" "*(n-2),end="")
#             print("*")
# loop1(4)

# def invertedpy(n):
#     for x in range(1,n+1):
#         print("*"*(n+1-x))
# invertedpy(7)

# def inhollow(n):
#     for x in range(1,n+1):
#         if x==1:
#             print("*"*(n+1-x))
#         elif x==n:
#             print("*")
#         else:
#             print("*",end="")
#             print(" "*(n-x-1),end="")
#             print("*")            
# inhollow(8)

# def full(n):
#     for x in range(1,n+1):
#         print(" "*(n-x),end="")
#         print("*"*((2*x)-1))
# full(4)

# def hollow_triangle(n):
#     for x in range(1, n + 1):
#         print(" " * (n - x), end="")  # Print leading spaces
#         if x == 1 or x == n:
#             print("*" * ((2 * x) - 1))  # Print full row for top and bottom
#         else:
#             print("*" + " " * ((2 * x) - 3) + "*")  # Print hollow part
# hollow_triangle(4)

#Raise statement and error concept
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18")
#     else:
#         print("You are eligible!")

# try:
#     check_age(16)
# except ValueError as e:
#     print(f"Error: {e}")

#List comprehensions:create a new list with help of an existing list by applying an expession on each element in an iterable
# a = [1,2,3,4,5]
# b = [x**2 for x in a]
# print(b)

#perfect square no
# import math
# def isperfectsq(n):
#     sqrt=math.sqrt(n)
#     if sqrt==int(sqrt):
#         return True
# n=int(input("Enter the no "))
# if isperfectsq(n):
#     print("Perfect square no")
# else:
#     print("Not a perfect square")

# a=["a","b","c"]
# b = " ".join(a)
# print(b)
a=-(44)
b=7
print(a%b)
