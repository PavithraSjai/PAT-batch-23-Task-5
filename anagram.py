#Function to return true if the string is anagram of another string , false otherwise
def anagram(a,b):
    #Using sort method to check if the given string is anagram
    if sorted(a)==sorted(b):
        return (print("True"))

    else:
        return (print("False"))
x="heart"
y="earth"
anagram(x,y)