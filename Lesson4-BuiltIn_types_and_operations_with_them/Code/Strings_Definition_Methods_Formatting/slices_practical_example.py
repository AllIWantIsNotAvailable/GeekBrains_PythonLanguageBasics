top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов '
# Вывести строку: "Поздравляем: 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!

start = top5.find('1.')
stop = top5.find('4.')

top3 = top5[start:stop]

# Метод str.strip() удаляет лидирующие и оконечные пробелы в строке и возвращает строку,
# без пробелов в начале и конце.
result_output = f'Поздравляем: {top3.upper().strip()} с успехом!'
print(result_output)