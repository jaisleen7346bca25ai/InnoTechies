age= int(input("Enter the age: "))
decree= input("Do you have a royal decree? ")
if (age<18):
    print("MINOR")
elif (66>age>17):
    print("ADULT")
elif (age==25 and bool(decree)):
    print("NOBLE")
elif (age>65):
    print("ELDER")
