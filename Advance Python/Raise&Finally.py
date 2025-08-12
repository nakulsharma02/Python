class UserException(Exception):
    def __init__(self, message):
        self.message = message
    def print_exception(self):
        print(f"UserException: {self.message}")
try:
    raise UserException("This is a user-defined exception")
except UserException as e:
    e.print_exception()
finally:
    print("This block always executes, regardless of whether an exception was raised or not.")