# check anagram

# check anagram
def isAnagram(a,b):
    if len(a)==len(b):
        if sorted(a)==sorted(b):
            return "It is an Anagram"
        else:
            return "It is not an Anagram"
    else:
        return "It is not an Anagram"

a=input("Enter a string: ")
b=input("Enter a string: ")

result=isAnagram(a,b)
print(result)