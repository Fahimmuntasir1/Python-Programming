n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = max(arr)
# print(m)
c = arr.count(m)
for i in range(c):
    arr.remove(m)
# print(max(arr))
print(max(arr))


# Another Solution 
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# max1=arr[-1]
# arr.sort(reverse=True)
# for x in arr:
#         if x!=max1:
#             result = x
#             print(result)
#             break
