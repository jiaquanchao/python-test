def decoration(s):
    def tem1(func):
        def tem2(*args, **kw):
            print('you input %s, call %s()' % (s, func.__name__))
            return func(*args, **kw)
        return tem2
    return tem1

@decoration('haha')
def now():
    print('66-66-66')

now()
