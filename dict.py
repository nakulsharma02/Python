my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}#dictionaries are mutable
# my_dict1=dict(name='Nakul',age='20',city='delhi')
# print(my_dict,type(my_dict))
# print(my_dict1,type(my_dict1))
# print("here name,age,city are the keys and Alice ,30 New York are the values")
# #Accessing  Values methods
# print(my_dict['name'])  # Output: Alice
# print(my_dict.get('age'))  # Output: 30
print(my_dict.get('country', 'USA'))  # Output: USA
