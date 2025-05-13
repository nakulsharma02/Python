# name = "Nakul"
#strings are immutable
# name = 'Nakul Sharma'
# name = '''Nakul Sharma'''
# print(name)
#strings methods
yup = "you # are very"
print(yup.capitalize())
# # print(yup.startswith("You"))
print(yup.endswith("end"))
# # print(yup.replace('my','mine'))
print(yup.split('are'))
# # print(yup.upper())
# # print(yup.lower())
print(yup.title())
print(yup.lstrip())
print(yup.rstrip())
print(yup.find("are"))
print(yup.strip())
# string functions
# print(len('hello'))
# t=9090
# print(type(str(t)))
# print(ord('b'))
# print(chr(15))
#slicing
name='nakulsharma'
Slice = name[0:5]
print(Slice)
# Slice1 = name[-6:-1]
# print(Slice1)
# Slice2 = name[:6]
# print(Slice2)
# Slice3 = name[3:]
# print(Slice3)
# print(name.join("yes"))
# print(name[::-1])
s = "apple,banana,grape"
fruit_list = s.split(',')
print(fruit_list)  
# Output: ['apple', 'banana', 'grape']
a=['N','A','K','U','L']
b=('').join(a)
c=b[::-1]
print(b)
print(c)
