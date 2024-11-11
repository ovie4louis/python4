x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# def func(i):
#     i = i * 3
#     return i % 2 == 0
mp = filter(lambda i: i % 2 == 0, x)

print(list(mp))