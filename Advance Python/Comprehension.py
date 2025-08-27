# List Comprehensions
'''numbers = [1,2,3,'Hello',5,6]
even = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
print(even)
# Set Comprehension'''
'''set = {23,56,78,89}
set1 = {i for i in set if i%4 ==0}
print(set1)'''
# Dictiionary Comprehensions
cities = ['mumbai','Delhi','Rajasthan']
countries = ['India','America','Thailand']
# without comprehension
'''z = zip(cities,countries)
for a in z:
    print(a)
'''
# with 
d = {city:countries for city,countries in zip(cities,countries)}
print(d)