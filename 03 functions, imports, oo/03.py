# Python3: from functools import map

def do_smth(*args, **kwargs):
    print map(lambda x: x * x, args)
    print kwargs


do_smth(10, 20)
do_smth(10, 20, 100500)
do_smth(10, 20, 7, 100, 10, 11, 1)
do_smth(10, 500, 1, id=10, number=20)