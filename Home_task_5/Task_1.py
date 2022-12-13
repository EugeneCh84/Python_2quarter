some_txt = input('Enter some words and letters including "abc" \n')
#print(some_txt)
def del_letters(some_txt):
    some_txt = list(filter(lambda x: 'abc' not in x, some_txt.split()))
    return " ".join(some_txt)

some_txt = del_letters(some_txt)
print(some_txt)