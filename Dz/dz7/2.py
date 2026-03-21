def it(maxi):
    a = 0
    for q in range(maxi):
        yield 2**a
        a+=1

for i in it(10):
    print(i)
