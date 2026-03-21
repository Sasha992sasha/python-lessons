def it(maxi):
    a = 0
    for q in range(maxi):
        yield 3**a
        a+=1

for i in it(10):
    print(i)
#шось у мене чуйка шо я шось не так поняв