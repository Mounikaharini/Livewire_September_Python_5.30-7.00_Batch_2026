#Control Flow Statements
#sequence control -> Default Control -> line by line execution
#selection control -> Execute the block selectively ->if , if else , elif , nested if
#iterative control -> for loop , while loop
#jumping control -> break , continue , pass

#selection control
#simple if
'''
a = int(input("Enter a number : "))
if a==10:
    print("Hi")

#if - else
a = input("Enter Gpay / Phonepe : ")
if a=="Gpay" or a=="gpay" or a=="GPAY":
    print("Welcome to Gpay")
else:
    print("Welcome to Phonepe")
    
#elif
a = input("Enter Phonepe / Gpay : ")
if a=="Gpay" or a=="gpay" or a=="GPAY":
    print("Welcome to Gpay")
elif a=="Phonepe" or a=="phonepe" or a=="PHONEPE":
    print("Welcome to Phonepe")
else:
    print("Invalid Transaction Application")
'''
#nested if
a = input("Enter Phonepe / Gpay : ")
if a=="Gpay" or a=="gpay" or a=="GPAY":
    print("Welcome to Gpay")
    pin = int(input("Enter the pin number : "))
    if pin==1234:
        amt = int(input("Enter the Amt :"))
        if amt>=1 and amt<=5000:
            print("Transfered Successfully")
        else:
            print("Invalid Amount / Limit Reached")
    else:
        print("Invalid Pin Number")
elif a=="Phonepe" or a=="phonepe" or a=="PHONEPE":
    print("Welcome to Phonepe")
    pin = int(input("Enter the pin number : "))
    if pin==1234:
        amt = int(input("Enter the Amt :"))
        if amt>=1 and amt<=5000:
            print("Transfered Successfully")
        else:
            print("Invalid Amount / Limit Reached")
    else:
        print("Invalid Pin Number")
else:
    print("Invalid Transaction Application")









