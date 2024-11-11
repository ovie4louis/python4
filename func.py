def func(x, y):
    def add_():
       print(x + y ) 
    return  add_
print(func(2, 4))
func(2, 4)()

z = func(3,3)
z()
