
#sum of digits in string

def stringsum(s):
    total = 0
    for char in s:
        try:
            digit =int(char)
            total += digit
        except ValueError:
            print("non digits")
    return total

s='q2w3e4'
print(stringsum(s))

#square of dictionary values
def squarefuc(n):
    squared_n= {}
    for i in range(1,n+1):
        squared_n[i] = i*i
    return squared_n

n= int(input("Enter a number: "))
print(squarefuc(n))

#alphabatically string align
def sort_words(str_n):

    words = str_n.split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)

str_n = input('Enter a string: ')
print(sort_words(str_n))