def sort_words(str_n):
    words = str_n.split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)

str_n = input('Enter a string: ')
print(sort_words(str_n))