def my_func(arg):
    return arg


def arg_func():
    print("i'm function")


def fco(k):
    return (lambda n: n + 1)(k)


my_func(arg_func)()

num_100 = 100

print(fco(num_100))
