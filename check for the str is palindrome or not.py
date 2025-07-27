def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

s=input("Enter a string: ")
print("You entered:", s)
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
