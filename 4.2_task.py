inscription = "kryzys"
# print(dir(inscription))
inscription2 =inscription[::-1]
print(inscription2)
"""a=2
b=2
def num_equality_check():  # my own logical test
    if a == b:
        print('Yes')
    else:
        print('No')
num_equality_check()
print(bool(num_equality_check()))"""
def str_palindrome_check(word):
    return word == word[::-1]
print(str_palindrome_check('prawda'))

def str_palindrome_check2(word): # drugi sposób, ale nie rozumiem sam, co tutaj co wywołuje
    if word == word[::-1]:
        print('Yes')
    else:
        print('No')
    return str_palindrome_check2
str_palindrome_check2('prawda')
print(bool(str_palindrome_check2)) # dlaczego True? Ponadto jak się dopisze tutaj argument (słowo) to drukuje tutaj zarówno wynik spełnienia warunku z pętli, jak i wynik True/False