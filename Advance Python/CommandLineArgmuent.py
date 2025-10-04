# Positional Argument
# In Positional Argument you can't skip any argument during program execution 
'''import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="Second number")
    parser.add_argument("Operation",help="Operation")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.Operation == "add":
        result = n1 + n2
    elif args.Operation == "subtract":
        result = n1 - n2
    elif args.Operation == "multiply":
        result = n1*n2
    else:
        raise "Invalid Operation"
    print(result)'''
# Optional Argument
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="Second number")
    parser.add_argument("--Operation",help="Operation")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.Operation == "add":
        result = n1 + n2
    elif args.Operation == "subtract":
        result = n1 - n2
    elif args.Operation == "multiply":
        result = n1*n2
    else:
        raise "Invalid Operation"
    print(result)