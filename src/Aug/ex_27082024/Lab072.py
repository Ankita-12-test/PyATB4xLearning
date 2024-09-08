def decorator_1(func1):
    def ankita():
        print("that what")
        func1()

    return ankita


def decorator_2(func2):
    def dipika():
        print("hello jelo")
        func2()
    return dipika


@decorator_2
@decorator_1
def greet():
    print("Hello there")

greet()
