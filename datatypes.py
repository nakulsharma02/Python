# Numeric Datatype
# a = 6
# print(type(a))#int datatype
# b = 9.8 
# print(type(b))#floating point numbers
# k = 2 + 3j
# print(k) # complex numbers
# c = "this is type"
# print(type(c))#string #sequence 
# e = {'this','you','your'}
# print(type(e))#set data type
# f = ('this','you','your')
# print(type(f))#tuple #sequence
# g = ['this','you','your']
# print(type(g))#list #sequence
# h = {
#     'name' : 'your',
#     'value' : 'you'
# }
# print(type(h))#dictionary #mapping Datatype
# i = None
# print(type(i))#None DataType
##Bool Datatypes
# a=bool(56<200)
# print(a)
##Binary Datatypes
#bytes
x=b'hello'
print(x)
y=bytearray(x)
y[0]=72
print(y)
z=memoryview(y)
print(z[0]) 