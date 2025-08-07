## Exercise: Python Exception Handling

'''1. Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:

```
90–100 → A  
80–89  → B  
70–79  → C  
60–69  → D  
<60    → F
```

2. Your program should handle the following exceptions:
   - If the user enters a non-numeric value, catch the `ValueError` and display a user-friendly message.
   - If the user enters a number outside the valid range (0 to 100), raise a `ValueError` yourself with a custom message.

3. Use the `try–except–else–finally` structure:
   - `try`: Attempt to parse the input and compute the letter grade.
   - `except`: Handle conversion errors and invalid ranges.
   - `else`: Print the final grade if everything was successful.
   - `finally`: Print a goodbye message like `"Thank you for using the Grade Calculator. Goodbye!"` no matter what.

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/15_exception_handling/exception_handling_solution.py)
'''
try:
    grade = input("Enter your numeric grade (0-100): ")
    grade_float = float(grade)
    if grade_float < 0 or grade_float > 100:
        raise ValueError("Grade must be between 0 and 100.")
except ValueError as e:
    print(f"Error: {e}. Please enter a valid numeric grade between 0 and 100.")
else:
    if grade_float > 90 and  grade_float < 100:
        print("A")
    elif grade_float >= 80:
        print("B")
    elif grade_float >= 70:
        print("C")
    elif grade_float >= 60:
        print("D")
    else :
        print("F")
finally:
    print("Thank you for using the Grade Calculator. Goodbye!")
