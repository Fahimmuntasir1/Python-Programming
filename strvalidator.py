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

s = input("Input a string : ")

for c in s:
    if c.isalnum:
        num = True
    else:
        num = False
    if c.isalpha:
        alpha = True
    else:
        alpha = False
    if c.isdigit:
        digit = True
    else:
        digit = False
    if c.islower:
        lower = True
    else:
        lower = False
    if c.upper:
        upper = True
    else:
        upper = False

print(f"{num}\n{alpha}\n{digit}\n{lower}\n{upper}")
