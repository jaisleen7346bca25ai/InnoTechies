x=int(input("Enter what Head 1 speaks: "))
y=int(input("Enter what Head 2 speaks: "))
z=int(input("Enter what Head 3 speaks: "))
if (x+y>z or x+z>y or y+x>z or y+z>x or z+x>y or z+y>x):
    print("PROCEED")
else:
    print ("HALT")
