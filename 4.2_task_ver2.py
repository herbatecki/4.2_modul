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

checker = str_palindrome_check('prawda')
print(bool(checker))
print('----------------------------------------')
def str_palindrome_check2(word): # drugi sposób, ale nie rozumiem sam, co tutaj co wywołuje
    if word == word[::-1]:
        print('Yes')
        return True
    else:
        print('No')
        return False
    # return str_palindrome_check2
str_palindrome_check2('kajak') # sposób z pominięciem returna gdy funkcja ma wgrane wydruk czegoś
checker2 = str_palindrome_check2('prawda') # gdy stosujemy return - w tym przypadku dopisany jest return logiczny, ale też w funkcji jest wydruk, czyli wydrukuje po wywołaniu funkcji
print(bool(checker2)) # - tu sprawdzi logikę 