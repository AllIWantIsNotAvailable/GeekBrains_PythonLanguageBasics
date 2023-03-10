import copy


print('Чтобы создать полную копию, с учетом вложенности, используется метод библиотеки copy.deepcopy():')
a = [1, 2, [3, 4]]
print(f'\nИсходный список a[{a}]')

# Копия с помощью copy.deepcopy():
print('\nКопия с помощью copy.deepcopy():')
b = copy.deepcopy(a)
print(f'- Копия списка a[{a}] -> список b[{b}]')
b[2][1] = 200
print(f'- Меняем значение b[1] -> {b[2][1]}; теперь список b[{b}]\n'
      f'- Но, список a[{a}] не изменился')
