silver=int(input("Enter the amount of silver: "))
gold=int(input("Enter the amount of gold: "))
if (silver>50 or gold>5):
    print("RICH TAX")
elif (silver<10 and gold==0):
    print("TOO POOR")
else:
    print("NORMAL TOLL")
