lst = [1, 2, 3]

k1 = [(i, i * i) for i in lst]
k2 = list(zip(lst, [i * i for i in lst]))
k3 = list(map(lambda x: (x, x * x), lst))
k4 = list(zip(lst, map(lambda x: x * x, lst)))

print(k1, k2, k3, k4, end='\n')
