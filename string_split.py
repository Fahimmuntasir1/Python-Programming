# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function Description

# Complete the split_and_join function in the editor below.

# split_and_join has the following parameters:

# string line: a string of space-separated words
# Returns

# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

# Sample Input

# this is a string
# Sample Output

# this-is-a-string

line = input("Enter a string to split : ")


def string_split(string):
    x = string.split()
    return "-".join(x)


print(string_split(line))
