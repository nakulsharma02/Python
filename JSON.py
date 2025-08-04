Dictionary = {}
Dictionary["Ram"] = {
    'name': 'Ram',
    'age': 25,
    'phone': '1234567890'
}
Dictionary["Shyam"] = {
    'name': 'Shyam',
    'age': 30,
    'phone': '0987654321'
}
print(Dictionary)
print(type(Dictionary)) 
import json
# Convert the dictionary to a JSON string
json_string = json.dumps(Dictionary)
# Print the JSON string
print(json_string)
print(type(json_string))
# Convert the JSON string back to a dictionary
converted_dict = json.loads(json_string)
# Print the converted dictionary
print(converted_dict)
print(type(converted_dict))