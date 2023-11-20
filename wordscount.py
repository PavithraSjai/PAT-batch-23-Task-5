
#Function to take a string and return the number of words in it 
def countword(a):
    #Conting a word using len function along with split 
    #split helps to divide word after space
    wordscount=len(a.split())
    return(print("Number of words: ",wordscount))
#Sentence defined
str = "Python Automation Testing Guvi"
countword(str)