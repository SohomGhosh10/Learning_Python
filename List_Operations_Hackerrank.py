#Hackerrank problem of lists
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print



if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        x = input().split(' ')
        if x[0] == "insert":
            lst.insert(int(x[1]),int(x[2]))
        elif x[0] == 'remove':
            lst.remove(int(x[1]))
        elif x[0] == 'append':
            lst.append(int(x[1]))
        elif x[0] == 'sort':
            lst.sort()
        elif x[0] == 'pop':
            lst.pop()
        elif x[0] == 'reverse':
            lst.reverse()
        else:
            print(lst)