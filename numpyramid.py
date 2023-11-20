#Pyramid of number using for loop
#Initializing the number to get input from user
number = int(input("Enter the number for pyramid: "))
#Using nested for loop to iterate each row and column to print a number pyramid
for row in range (1,number+1):
    n=1
    for col in range(1,row+1):
        print(n,end = " ")
        n+=1
    print()