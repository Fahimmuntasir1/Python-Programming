# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true


N = int(input())
mylist = []
for i in range(N):
    command = input().split()
    if command[0] == "insert":
        mylist.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(mylist)
    elif command[0] == "remove":
        mylist.remove(int(command[1]))
    elif command[0] == "append":
        mylist.append(int(command[1]))
    elif command[0] == "sort":
        mylist.sort()
    elif command[0] == "pop":
        mylist.pop()
    elif command[0] == "reverse":
        mylist.reverse()
