#!/usr/bin/env python3
def fizzbuzz(ul=20, **kwargs):
    if not kwargs:
        items = [('fizz', '3'), ('buzz', '5')]
    else:
        items = list(kwargs.items())
    fn = (lambda f: lambda i, s, idx: f(f, i, s, idx))(
        lambda f, i, s, idx:
            f(
                f,
                i,
                f'{items[idx][0]}{s}' if i % int(items[idx][1]) == 0 else s,
                idx-1
            ) if 0 <= idx else s if s else i
    )
    return (fn(i, '', len(items)-1) for i in range(1,ul+1))

if __name__ == '__main__':
    from sys import argv
    for val in fizzbuzz(
        int(argv[1]) if len(argv) > 1 else 10,
        **dict([a.split('=') for a in argv[2:]])
    ):
        print(val)

