# files Crud Operations

# Write And Update Operations
'''
f = open("D://Python//Files/file1.txt","w")
f.write("Hello This is the test of Overlapping")
f.close()
'''
'''
f= open("D://Python//Files/file1.txt","a")
f.write("\nThis is the test of Append Operation")
f.close()
'''
'''f= open("D://Python//Files/file1.txt","w+")
a = 20 
b = 80
lambda_function = lambda x, y: x + y
f.write(lambda_function(a, b).__str__())
f.seek(0)
print(f.read())
f.close()'''

# Read Operations
'''f = open("D://Python//Files/file1.txt","r")
read = f.read()
print(read)
f.close()'''

'''f= open("D://Python//Files/file1.txt","a+")
f.write("This is a new line for word count.\n")
f.seek(0)
read = f.readlines()
for line in read :
    print(line + " ")
    words  = line.split(" ")
    count = len(words)
    print("Number of words in line:", count)
f.close()
'''