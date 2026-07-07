def imparesRegresivos(n):
    if n < 1:
        return None
    if (n %2 == 0):
        n = n - 1
    print(n)
    imparesRegresivos(n-2)
    return None
    
imparesRegresivos(10)

    