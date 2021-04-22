# A function to compute the volume of a sphere using 4/3πr3.
#pi = 3.141592653589793
#const = 4/3

def print_volume(r):
    const = 4/3
    pi = 3.141592653589793
    rCube = r**3
    volume = const * pi * rCube
    print(volume)

#print_volume(5)

#Surface Area of a triangle= 1/2*b*h
import math
def print_surfaceArea (b, h):
    constant = 1/2
    surfaceArea = constant * b * h
    print(surfaceArea)

print_surfaceArea(math.log(4+1),math.pi)


