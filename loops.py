#there are two types of loops in python for and while 
#while loop
# a=0
# while(a<=9):
#     print(a)
#     a+=1

#for loop
# a=['nine',45,'78',90]
# for x in range(1,4):
#     print(a)
#n term table using for loop:
# n=int(input("Enter the table no"))
# for x in range(1,11):
#     print(f'{n}X{x}={n*x}')
# Patterns
'''
  *
 ***
*****
 for n=3
'''
# n= int(input("Enter the number : "))
# for i in range(1,n+1):
#    print(" "*(n-i),end="")
#    print("*"*(2*i-1),end='')
#    print("")
'''
****
*  *
*  *
****
# for n=4
# '''
# n=int(input("Enter the value of n"))
# for i in range(1,n+1):
#    if(i==1 or i==n):
#       print("*"*n)
#    else:
#       print("*",end="")
#       print(" "*(n-2),end='')
#       print("*")   


n= int(input("Enter the no"))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*(2*(i)-1))