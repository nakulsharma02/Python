# Question 1
'''dictionary = {
    'China' : 143,
    'India' : 136,
    'USA' : 32,
    'Pakistan' : 21,
}
user = input("Enter the Operation 'print' , 'add', 'remove', 'query' : ")
if user == 'print':
    for keys in dictionary:
        print(f"{keys}==>{dictionary[keys]} ")
elif user == 'add':
    country = input("Enter the country name : ")
    if country not in dictionary.keys():
        population = int(input("Enter the population of the country : "))
        dictionary[country] = population
    else:
        print("Country already exists in the dictionary.")
    for keys in dictionary:
        print(f"{keys}==>{dictionary[keys]} ")
elif user == 'remove':
    country = input("Enter the country name to remove : ")
    if country not in dictionary.keys():
        print(f"{country} is not in the dictionary.")
    if country in dictionary.keys():
        dictionary.remove(country)
    if country not in dictionary.keys():
        print(f"{country} has been removed from the dictionary.")
        for keys in dictionary:
             print(f"{keys}==>{dictionary[keys]} ")
elif user == 'query':
    country = input("Enter the country name to query : ")
    if country in dictionary.keys():
        print(f"The population of {country} is {dictionary[country]} crores.")
    else:
        print(f"{country} is not in the dictionary.")
else:
    print("Invalid operation. Please enter 'print', 'add', 'remove', or 'query'.")
'''
# Question 2
'''stock = {
    'info' : [600,630,620],
    'ril' : [1430,1490,1567],
    'mtl' : [234,180,160]
}
UserInput = input("Enter The Operation 'print', 'add':")
if UserInput == 'print':
    for keys in stock:
        avg = sum(stock[keys]) / len(stock[keys])
        print(f"{keys}==>{stock[keys]}==> avg: {avg:.2f}")
elif UserInput == 'add':
    stockTicker = input("Enter the stock ticker : ")
    price = input("Enter the stock price : ")
    if stockTicker not in stock.keys():
        stock[stockTicker] = [int(price)]
    else:
        stock[stockTicker].append(int(price))
    for keys in stock:
        avg = sum(stock[keys]) / len(stock[keys])
        print(f"{keys}==>{stock[keys]}==> avg: {avg:.2f}")
else :
    print("Invalid operation. Please enter 'print' or 'add'.")'''

# Question 3
# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them
radius = float(input("Enter the radius of the circle: "))
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    diameter = 2 * radius
    circle = {
        'area': area,
        'circumference': circumference,
        'diameter': diameter
    }
    print(circle)
circle_calc(radius)
