# Arbitrary Base Converter
This tool was made in response to a challenge from a friend. It takes a number, in any base from 2-35, and will convert it to any other base from 2-35. It uses capital
lettering to represent values beyond 9, as in hexadecimal. This base would be up to pentatriacontal, I suppose. It utilizes the tkInter library for Python to create a UI,
and implements a very basic algorithm to convert from one base to another.

Additionally, it will attempt to solve for a number in an unknown base, provided you know it's overall quantity in another base representation.
E.g. You have the number 1000 in base 10, and you have the number "1HG" in a base you don't know. The solution will populate in the plain-text box.
