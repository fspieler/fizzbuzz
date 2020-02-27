def fizzbuzz(ul=20, **kwargs):
    if not kwargs:
        kwargs = {
            'fizz': 3,
            'buzz': 5
        }
    items = sorted(kwargs.items(), key=lambda t:t[1])
    def fn(i, s, idx):
        if idx == -1:
            return s if s else i
        return fn(
            i,
            f'{items[idx][0]}{s}' if i % items[idx][1] == 0 else s,
            idx-1
        )

    return (fn(i, '', len(items)-1) for i in range(1,ul+1))

for val in fizzbuzz(41, fizz=3, buzz=4):
    print(val)


