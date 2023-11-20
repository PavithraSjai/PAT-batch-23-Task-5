#Function to take a string and return it by giving the unique character in it 
#Initializing the string 
y = "guvi guvi test"
def unique_char(b):
    #Nested for loop to iterate through each character of the string
    for i in range(0,len(y)):
        char = 0
        for j in range (0,len(y)):
            #Check if characters are same or different 
            if(y[i]==y[j] and i!=j):
                char=1
                break
        if(char==0):
            print(y[i],end=" ")
unique_char(y)