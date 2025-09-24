pile1= int(input("Enter the number of gold coins in Pile 1: "))
pile2= int(input("Enter the number of gold coins in Pile 2: "))
pile3= int(input("Enter the number of gold coins in Pile 3: "))
if (pile1+pile2+pile3!=45 and pile1==10):
    print("PASS")
else:
    print("FAIL")
