a = ["Are", "you", "listening", "to", "me?"]
# for i in a:
#     print(i)
# print(dir(a))

# iterator = iter(a)
# print(next(iterator))  # Output: Are
# print(next(iterator))  # Output: you
# print(next(iterator))  # Output: listening
# print(next(iterator))  # Output: to
# print(next(iterator))  # Output: me?
# reverse_iterator = reversed(a)
# print(next(reverse_iterator))  # Output: me?
# print(next(reverse_iterator))  # Output: to

#  Use of iterator in the class
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index = self.index + 1
            return result
        else:
            raise StopIteration

Iterator = MyIterator(a)
Itr = iter(Iterator)
print(next(Iterator)) # Output: Are
print(next(Iterator))  # Output: you
print(next(Iterator))  # Output: listening
print(next(Iterator))
# Output: to
print(next(Iterator))  # Output: me?
print(next(Iterator))  # Raises StopIteration