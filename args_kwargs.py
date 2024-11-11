def func(*args, **kwargs):
    print (args, kwargs)
    print (*args, kwargs)


func (2,45,6,789,908,0, one = 34, two = 5)
