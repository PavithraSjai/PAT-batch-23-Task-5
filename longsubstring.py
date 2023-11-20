#Function to take 2 strings and return the longest common substring between them 
def substring(str1,str2):
    #Nested for loop to get the common string
    for i in range(0,len(str1)):
        char=0
        for j in range(0,len(str2)):
            #Using if condition to take the common sub string 
            if(str1[i]==str2[j]):
                char=1
                print(str1[i],end = " ")
                break
        if (char==0):
            print()
#Initializing 2 strings 
str1 = "python classes sylabus"
str2 = "python guvi classes sylabus"
substring(str1,str2)