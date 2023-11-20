#Program to find the count of total vowel and count of each individual vowel:
#count of a, e,i, o, u in "greetings for you "
#Initializing the sentence, vowels 
sentence = "Guvi Geeks Network Private Limited"
vowel = ["a","e","i","o","u"]
count = 0
#Finding the count of each vowel using count method
countvowel = [sentence.count(i) for i in vowel]
#For loop to iterate through each char and find the count of all vowel
for char in sentence:
    if char in vowel:
        #If vowel is identified the count is incremented
        count+=1
#Printing the output                
print("Total number of vowel present:",count)
print("Number of each vowel : ",countvowel)