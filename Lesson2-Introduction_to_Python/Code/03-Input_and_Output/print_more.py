# строка целиком
print('Привет, меня зовут Кеша мне 2 года')

# У нас есть 2 переменные
name = 'Кеша'
age = 2

# Как вывести строку вместе с переменными в терминал?
print('Строки с переменными:')
print('Привет, меня зовут', name, 'мне', age, 'года')
print(name, age)
print('------>')
print()
# Замена разделителя (sep) аргуентов print()
print('Строка с персонализированным разделителем')
print(name, age, sep='/')
print('------>')
print()

# Замена "символа переноса строки" (end) функции print()
print('Строка с персонализированным переносом:')
print('end="\\n"')
print(name)
print(age)
print()
print('end="_"')
print(name, end='_')
print(age, end='_')
print('года')
