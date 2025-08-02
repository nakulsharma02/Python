#declaration and defination are apply at same time
# def hii():
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.say("Hii,I am Nakul Sharma Please give a Introduction")
#     engine.runAndWait()
# #function calling
# hii()

'''Now , The Concept of parameters and arguments
parameters are declared at the time of function defination and declaration
& Arguments are generally inserted in the function at the time of function calling
& Arguments are also referred to as the value of parameters and parameters are reffered to the variables'''
# def Intro(message=input("Convey Your Dialogue here in words = ")):
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.say(message)
#     engine.runAndWait()
#function calling
# Intro()
#Recursive function is a function which call itself 
# n=int(input("Enter the number"))

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(f'The factorial of {n} is',fact(n))
# Lambda Functions
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
lambdafunc = lambda a=0,b=0 : print(a+b) if a and b else print("Please enter valid numbers")
lambdafunc()
