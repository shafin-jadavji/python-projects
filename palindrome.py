'''
Check if a user given string is a palindrome or not
'''

# get user_input
# create reverse_string from the reverse of the user input
# if user_input == reverse_string
# print Is palindrome
# else print not palindrome
 
user_input = input("Enter string to check for palindrome: ")

reverse_string = user_input[::-1]
# print(reverse_string)

if reverse_string == user_input:
    print(f"{user_input} is a palindrome")
else:
    print(f"{user_input} is not a palindrome")