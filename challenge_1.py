
"""
Task 2.1.Challenge file challenge_1.py

Start
1. Import math module to allow for more advance maths. In this case square root.
2. Request the user to enter the lengths of all three sides of a triangle.
3. Calculate the area of the triangle.
4. Print out the area of the triangle.
End

"""
# import math to use 'math.sqrt' or can also use 'from math import sqrt' then just put 'sqrt' before brackets. Could also not import math and end brackets with **0.5 to square root.

import  math

# Initialise variables, request the user to enter the lengths of all three sides of a triangle (as a float to allow for actual length in cm).

triangle_side1 = float(input("Please enter the length in 'cm' of side 1 of the triangle here : "))
triangle_side2 = float(input("Please enter the length in 'cm' of side 2 of the triangle here : "))
triangle_side3 = float(input("Please enter the length in 'cm' of side 3 of the triangle here : "))

# Then work out and print out: The area of the triangle in cm2 to two decimal places

semi_perimeter = (triangle_side1 + triangle_side2 + triangle_side3) / 2
print(f"\nThe semi-perimeter of the triangle where, s = (a + b + c)/2 is equal to: {semi_perimeter} cm\n")

triangle_area = math.sqrt(semi_perimeter * (semi_perimeter - triangle_side1) * (semi_perimeter - triangle_side2) * (semi_perimeter - triangle_side3))
print(f"The area of the triangle where, area = √(s(s-a)*(s-b)*(s-c)) is equal to: {triangle_area:.2f} cm2\n")


# Program ends