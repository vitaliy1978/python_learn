n = '7'
my_frozen = set()
for i in range(78):
    # print(my_frozen)
    my_frozen.add(int(n))
    n += '7'
my_frozen = frozenset(my_frozen)


