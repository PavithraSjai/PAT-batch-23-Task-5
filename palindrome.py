#Function to take a string and return True if it is palindrome and Falase if not
def palindrom(string):
        #checking that if string is equal to reverse of string using slicing 
        return string == string[::-1]
#Getting a string from user 
s=str(input("Enter a string :"))
#Function call
output = palindrom(s)
#Print true of palindrom , false otherwise
if output :
    print("True")
else:
    print("False")