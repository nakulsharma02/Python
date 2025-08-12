def Generators():
    yield "Hello"
    yield "How"
    yield "are"
    yield "you?"
a = Generators()
print(next(a))  # Output: Hello
print(next(a))  # Output: How
print(next(a))  # Output: are
print(next(a))  # Output: you?
