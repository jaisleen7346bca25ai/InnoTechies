x= int(input("Enter the year: "))
if (x%4):
    print("GRYPHON SIGHTING")
elif (x%100):
    print("QUIET YEAR")
elif (x%100 and x%400):
    print("GRYPHON SIGHTING")
