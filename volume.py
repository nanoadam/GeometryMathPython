# General Vars
pi = 3.14159265359


# Volume Functions
def cylinderVolume():
    radius = input('Radius: ')
    height = input('Height: ')
    calc = pi * (int(radius) * int(radius)) * int(height)
    print(f'Answer: {calc}')


def coneVolume():
    radius = input('Radius: ')
    height = input('Height: ')
    calc = 3.14159265359 * (int(radius) * int(radius)) * int(height) / 3
    print(f'Answer: {calc}')


def prismVolume():
    length = input("Length: ")
    width = input("Width: ")
    height = input("Height: ")

    calc = (int(length) * int(width)) * int(height) / 3
    print(f'Answer: {calc}')


def halfCircleVolume():
    radius = input("Radius: ")

    calc = (4/3) * pi * (int(radius) * int(radius) * int(radius)) / 2

    print(f'Answer: {calc}')


# Make Sure to Run Program
