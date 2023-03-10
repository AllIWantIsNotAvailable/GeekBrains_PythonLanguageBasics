def greeting(who: str, say: str = 'Hello'):
    """
    Функция greeting() – эта функция относится ко второму типу: что-то принимает, но ничего не возвращает.
    Эта функция приветствует пользователя по имени и определенным образом. Как приветствовать и имя пользователя
    передаются параметрами функции.
    :param say: Как приветствует функция.
    :param who: Имя пользователя, которого приветствует функция.
    :return: None
    """
    print(f'{say}, {who}!')


def main():
    greeting('Leo')
    greeting('Max', 'Hi')
    greeting(say='What\'s up', who='Kate')


if __name__ == '__main__':
    main()