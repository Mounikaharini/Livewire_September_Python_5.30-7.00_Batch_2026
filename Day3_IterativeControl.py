#iterative control

#entry check loop -> first check the condition after that execute the block

#for -> we know the count priorly
#increment , decrement , nested loop , for - else

#while -> we know the specified condition only
#increment , decrement , nested loop , while - else , condition based sums

#exit check loop -> first execute the block after that check the condition

#for variable in range(start,ending-1,inc/dec)
'''
for i in range(1,11,1):
    print(i)

for i in range(10,0,-1):
    print(i)

odd = 0
even = 0
n=int(input("Enter a number :"))
for i in range(n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i

print("Odd Sum",odd)
print("Even Sum",even)


3 x 1 = 3
3 x 2 = 6
.........
3 x 9 = 27
3 x 10 = 30

for i in range(1,11,1):
    print("3 x",i,"=",i*3)

for j in range(5):
    for i in range(5):
        print("*",end=" ")
    print()

* 
* * 
* * *  
* * * * 
* * * * * 

i j1 2 3 4 5
1 11
2 21 22
3 31 32 33
4 41 42 43 44
5 51 52 53 54 55

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
A B C D E
A       E
A       E
A       E
A B C D E
i   j
11 12 13 14 15
21          25
31          35
41          45
51 52 53 54 55

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print(chr(65+j),end=" ")
        else:
            print(" ",end=" ")
    print()
#factorial
#1!=1
#2!=1*2=2
#3!=1*2*3=6
#4!=1*2*3*4*=24
#5!=1*2*3*4*5=120

n = int(input("Enter a number :"))
c = 1
for i in range(1,n+1):
    c = c * i
print(c)

#sum of elements in a list
x = [1,2,4,2,3,1,4,2,43,28,6,5,7,8]
c = 0
for i in x:
    c = c + i
print(c)
'''
#prime or not

n = 3
c = 0
for i in range(1,n+1):
    if n%i==0:
        #print(i)
        c+=1
if c==2:
    print("Its a prime")
else:
    print("Its not a prime")




















