def ginobacci(n,x,y):
    
    if n == 0:
        return x
    if n == 1:
        return y
    else:
    
        return ginobacci(n-1, x, y) - ginobacci(n-2, x, y)
        

print(ginobacci(3, 0, 1))


 