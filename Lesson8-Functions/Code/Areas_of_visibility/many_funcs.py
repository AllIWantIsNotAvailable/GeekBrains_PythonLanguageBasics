M = 'Меня видно везде'


def a():
    print('\nИз a():')
    print('1) Глобальная переменная "М":', M)
    ma = 'Меня виднов в b() и в a()'
    print('2) Локальная переменная "ma" функции a():', ma)

    def b():
        print('\nИз b():\n')
        print('1) Глобальная переменная "М":', M)
        print('2) Локальная переменная "ma" функции a():', ma)
        mb = 'Меня видно в c() и d b(), но не видно в a()'
        print('3) Локальная переменная "mb" функции b():', mb)

        def c():
            print('\nИз c():')
            print('1) Глобальная переменная "М":', M)
            print('2) Локальная переменная "ma" функции a():', ma)
            print('3) Локальная переменная "mb" функции b():', mb)
            mc = 'Меня видно только в c()'
            print('4) Локальная переменная "mc" функции c():', mc)
        c()
        # print(M, ma, mb, mc)

    b()
    # print(M, ma, mb, mc)


print('\nИз many_funcs.py:')
print('1) Глобальная переменная "М":', M)
a()
# print(M, ma, mb, mc)
