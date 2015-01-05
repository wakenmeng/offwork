#coding: utf-8
from time import time

def logged(when):
    def log(func, *args, **kwargs):
        print """Called:
function: %s
args: %r
kwargs: %r""" % (func, args, kwargs)

    def pre_logged(f):
        def _wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)
        return _wrapper

    def post_logged(f):
        def _wrapper(*args, **kwargs):
            now = time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print "time delta: %s" % (time()-now)
        return _wrapper

    return {'pre': pre_logged}.get(when, post_logged)

@logged('post')
def hello(name):
    print "Hello,", name

hello('mengweikang')

