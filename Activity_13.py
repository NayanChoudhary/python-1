lower=int(input("Enter the start number:"))
upper=int(input("Enter the stop number:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
