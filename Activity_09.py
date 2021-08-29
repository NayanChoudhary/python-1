l=float(input())
b=float(input())
h=float(input())
PI= 3.141
x=l**2
y=b**2
z=h**2
k=x+y+z
volume = (y*z)/(k**.500)
radius = ((volume*.750)/PI)**(1/3)
print(format(volume, ".3f"))
print(format(radius, ".3f"))
