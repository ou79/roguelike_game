def concatenate1(head, *, tail, body='_'):
    return head + body + tail

def display_func(*args, **kargs):
    for key, value in kargs.items():
        print(key, value)

display_func(text='a', x1=4, x2=5, x3=6, x4=7)