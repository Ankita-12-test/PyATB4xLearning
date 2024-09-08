def outer_func():
    ankita = 10
    print(ankita)

    def inner_fun_1():

        print(ankita)

    def inner_fun_2():

        print(ankita)

    inner_fun_1()
    inner_fun_2()


outer_func()
