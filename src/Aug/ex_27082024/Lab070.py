import time
def kanha(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time take by function {end_time - start_time}")
    return wrapper


@kanha
def time():
    print("Add function delay")
    time.sleep(2)

@kanha
def time_1():
    print("Add function delay")
    time.sleep(5)
