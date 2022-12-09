import random
a = [random.randint(0,10) for i in range (20)]
print(a)


b = [x for i, x in enumerate(a) if i != a.index(x)]
lst = [set(a) ^ set(b)]     #   ( s1 ˆ s2 )    the set of elements in precisely one of s1 or s2
print(lst)

        