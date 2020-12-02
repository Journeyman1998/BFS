from timeit import default_timer as timer

def time(fun, *args):
    x = timer()
    ret = fun(*args)
    y = timer()
    return ret, y-x