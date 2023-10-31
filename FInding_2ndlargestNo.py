

n = int(input()) 
arr = list(set(map(int, input().split()))) # arr = [2 , 3 , 6 , 6 ,5]
arr.sort() # arr = [2 ,3 , 5 , 6]
print(arr[-2]) # 5