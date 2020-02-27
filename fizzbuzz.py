def fizzbuzz(ul=20):
    items = [
        (3, 'fizz'),
        (5, 'buzz')
    ]

    def fn(i, s, idx):
        if idx == -1:
            return s if s else i
        return fn(
            i,
            f'{items[idx][1]}{s}' if i % items[idx][0] == 0 else s,
            idx-1
        )

    return (fn(i, '', len(items)-1) for i in range(1,ul))

for val in fizzbuzz(20):
    print(val)


