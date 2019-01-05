from functools import partial

blocks = []
f = open("file1.txt")
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
print blocks

l = [1, 2, 3, 4, 5]
print l[6:]


def hash_a(item):
    # type: (object) -> int
    # Fails; an object does not have a 'magic' method.
    item.magic()
    return item


def hash_b(item):
    # Typechecks
    item.magic()


test = [[1, 2], [2, 3], [3, 4], [4, 5]]
for t in test[4]:
    print t
