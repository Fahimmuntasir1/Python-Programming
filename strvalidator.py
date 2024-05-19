# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format

# A single line containing a string .

# Constraints


# Output Format

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True

# solution 1

# s = input("Input a string : ")
# num = alpha = digit = lower = upper = False
# for c in s:
#     if c.isalnum():
#         num = True
#     if c.isalpha():
#         alpha = True
#     if c.isdigit():
#         digit = True
#     if c.islower():
#         lower = True
#     if c.upper():
#         upper = True

# print(f"{num}\n{alpha}\n{digit}\n{lower}\n{upper}")


# Another solution
s = input("input a string")
print(any([x.isalnum() for x in s]))
print(any([x.isalpha() for x in s]))
print(any([x.isdigit() for x in s]))
print(any([x.islower() for x in s]))
print(any([x.isupper() for x in s]))
