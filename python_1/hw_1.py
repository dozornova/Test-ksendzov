# 1) Создать переменную типа String
a = 'Sergey'

# 2) Создать переменную типа Integer
b = 10

# 3) Создать переменную типа Float
c = 10.5

# 4) Создать переменную типа Bytes
d = b'\x00\x00'

# 5) Создать переменную типа List
e = [1, 4, 8, 8, 'car', 'Amsterdam']

# 6) Создать переменную типа Tuple
f = (1, 2, 3, 4, 5)

# 7) Создать переменную типа Set
j = {1, 2, 3, 'Sergey', 'DOM', (1, 2, 3, 55)}

# 8. Создать переменную типа Frozen set
h = frozenset(j)

# 9) Создать переменную типа Dict
i = {'name': 'Sergey', 'age': 25, 'sex': 'male'}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print(type(j), j)
print(type(h), h)
print(type(i), i)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name = 'Sergey'
city = 'Saint Petersburg'
concat = name + ', ' + city
print(concat)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
number = 1
string = 'open'
print(type(number), type(string))

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

print(str(number) + ' ' + string)
