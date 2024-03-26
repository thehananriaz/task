def squarefuc(n):
    squared_n= {}
    for i in range(1,n+1):
        squared_n[i] = i*i
    return squared_n

n= int(input("Enter a number: "))
print(squarefuc(n))