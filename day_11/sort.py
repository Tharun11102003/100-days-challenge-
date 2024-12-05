"""
Sort a List Without Using the Sort Method
"""




a = [1, 2, 4, 3, 6, 9, 0]
b = []
while a:
    c = a[0]
    for i in a:
        if i < c:
            c = i
    b.append(c)
    a.remove(c)
print(b)