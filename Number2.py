a = [1, 4, 6]
b = [11, 33, 22]

amin = min(a)
amax = max(a)

a.remove(min(a))
a.remove(max(a))

a.insert(0, amin)
a.insert(1, amax)

print(a)

# Вариант который подходит конкретно сюда, но работает :)