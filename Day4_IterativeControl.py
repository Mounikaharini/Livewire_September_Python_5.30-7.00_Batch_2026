'''
i=1
while i<=5:
    print(i)
    i+=1

i=5
while i>=1:
    print(i)
    i-=1

#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
i=1
while i<=5:
    j = 1
    while j<=5:
        print("*",end=" ")
        j+=1
    print()
    i+=1

#Task: Continually ask a user to enter numbers. Add them together. Stop the program and print the final total only when the user types 0.
c=0
n=int(input("enter a number to start the loop or for stop enter '0' : "))
while(n!=0):
    n=int(input("enter a number to add or for stop enter '0' : "))
    c = c + n
print(c)

#count the digits
n=123
c=0
while(n>0):
    n//=10
    c+=1
print(c)

#sum of digits
n=123 #6
c=0
while(n>0):
    r=n%10
    c+=r
    n//=10
print(c)

#reverse a number
n=123 #321
c=0
while(n>0):
    r=n%10
    c=(c*10)+r
    n//=10
print(c)

#palindrome

n=123 #321
n1=n
c=0
while(n>0):
    r=n%10
    c=(c*10)+r
    n//=10
if n1==c:
    print("palindrome")
else:
    print("Not a palindrome")
Task:
Ask the user for an integer n. If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Repeat this process until n becomes 1,
printing the sequence along the way.

n=32
while(n!=1):
    if n%2==0:
        n//=2
    else:
        n=(n*3)+1
    print("n: ",n)
'''

#convert decimal into binary

n=32 #101
c=0
while(n>=0):
    r=n%2
    if (r==0):
        c=1*10+c
    else:
        c=(c*10)+r
    n//=2
print(c) 

#convert decimal to octal




