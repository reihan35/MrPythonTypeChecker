def f (L, N):
    """ list[int] * list[int] -> int """
    #X : list[int]
    X = L
    X.append(3)
    #M : list[list[int]]
    M = [[1, 2, 3], X[:], L[:]]
    #W : list[list[int]]
    W = M[:]
    return 0

def f2(L):
    """ list[int] -> int """
    #M : list[int]
    return 0
    
assert f([1, 2, 3], [4, 5, 6]) == 0
assert f([7, 8, 9], [10, 11, 12]) == 0

assert f2([7, 8, 9]) == 0
assert f2([7, 8, 9]) == 0
