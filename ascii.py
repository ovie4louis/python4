# x = "a"
# print(ord(x))

# print(not(False and True or True))


x = [ 4, True, "ovie", 5]

# y = x #change in  the y will affect y and x because making reference to the list not  copy the list
y = x[:] #change in any of x or y will not affect x and y because it was copy
print("this is x list", x)
print("this is y list", y)

y[0] = 10

print("this is x list", x)
print("this is y list", y)

x.append("ovie")

print("this is x list", x)
print("this is y list", y)