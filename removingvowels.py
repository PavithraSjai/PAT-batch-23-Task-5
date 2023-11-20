#Function to take a string and return it by removing of all the vowels
#String taken : Guvi Python Automation Testing
#Global variable x initialization to get the string
#initializing the vowel
x = "Guvi python automation testing"
vowel = ["a","e","i","o","u"]
result = {}
def novowel(a):
    for vow in x:
        if vow not in vowel:
            print(vow, end=" ")
novowel(x)