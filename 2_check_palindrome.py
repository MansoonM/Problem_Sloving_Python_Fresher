# check palindrome

def isPalindrome(user_input):
    rev_user_input=""
    for x in user_input:
        rev_user_input=x+rev_user_input
    if user_input==rev_user_input:
        return "It is a Palindrome."
    else:
        return "It is not a Palindrome."

user_input=input("Enter a string: ")

print(isPalindrome(user_input))