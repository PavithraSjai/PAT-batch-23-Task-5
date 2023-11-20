#Fuction to return most frequent character in a string
#Initialzing the string
def freqchar(str1):
    #Initializing the frequency as an empty dictionary
    frequent = {}
    #For loop to iteriate through each char
    for char in str1:
        if char in frequent:
            frequent[char]+=1
        else:
            frequent[char]=1
    #Max method to take the frequnently used character count
    maximum_character = max(frequent, key=frequent.get)
    #Converting the max count to String and printing the frequent character
    print("Most frequent character in the given string : "+ str(maximum_character))
str1="tent"
freqchar(str1)