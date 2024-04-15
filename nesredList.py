
# take two variable to store score & students
scores = []
students = []
# ,,, given function
for n in range(int(input())):
    name = input()
    score = float(input())
    # ,,,
    # append score & students into variable
    scores.append(score)
    students.append([name, score])
    
# find lowest score with built-in min() function and count this with count() function.
minScore = min(scores)
count = scores.count(minScore)
for i in range(count):
    # remove the lowest score to get second lowest score
    scores.remove(min(scores))
        
secondLowest = min(scores)
    
students.sort()
output = [x for x in students if x[1] == secondLowest]
# print(output)
for i in output:
    print(i[0])