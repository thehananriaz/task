
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


