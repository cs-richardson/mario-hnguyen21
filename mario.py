'''
The marioMore code accepts integers from 0 to 23 and builds a pyramid
with a gap of 2. If the user input a number outside of the domain, the program
will reprompt the user.

The marioLess code accepts integers from 0 to 23 and builds a half-pyramid.
If the user input a number outside of the domain, the program
will reprompt the user.
By: Ben
'''

#Mario Less calculations
def marioLess(height):
    for i in range(2, height+2):
        spaces = " " * (height-(i-1))
        blocks = "#" * i
        print(spaces + blocks)

#Mario More calculations
def marioMore(height):
    for i in range(1, height+1):
        spaces = " " * (height-i)
        blocks = "#" * i
        print(spaces + blocks + "  " + blocks)

#User Input
height = input("Height: ")
while not(height.isdigit()) or int(height) > 23 or int(height) < 0:
    height = input("Height: ")

height = int(height)

marioLess(height)
marioMore(height)
