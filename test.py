from functools import partial

blocks =[]
f = open("file1.txt")
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
print blocks


l = [1, 2, 3, 4, 5]
print l[6:]