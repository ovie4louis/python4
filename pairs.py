def func(x, y):
    print(x,y)



pairs = [(1,2), (4,5)]
func(*pairs)

for pair in pairs:
    func(*pair)