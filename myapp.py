import threading
import multiprocessing
import asyncio

def limit_added_numbers(fn, *args, **kwargs):

    def inner(*args, **kwargs):
        args = args[:3]
        
        fn(*args[:3], **kwargs)
    return inner


def add_multiple_values(fn, *args, **kwargs):
    def inner(*args, **kwargs):
        a, b, *c = args

        first_result = fn(a, b)

        final_result = first_result

        if c is not None:
            for num in c:
                final_result += num
        
        if kwargs is not None:
            for _, num in kwargs.items():
                final_result += num
        return final_result
    return inner

#@limit_added_numbers
@add_multiple_values
def add(a: int, b: int):
    return a + b


def my_func():
    a = 5
    b = 3
    c = ['asdasd', 3, {1, 2, 3}]

    return a, b, c


def num_multiply(*args):
    result = 1
    for num in args:
        result *=num
    return result

""" if __name__ == "__main__":


    print('')
    a = 5
    b = a + 3
    print(add(3, 4, 4, 5, 6, 7, h=5, j=3, k=3))

    t = my_func()

    print(num_multiply(2, 3, 4))

    print(t[0])
    print(t[2][1])
   print(t[2][2].items())


'''

