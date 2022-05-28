def f(x):
    if x <= -2:
        x = 1 - (x + 2)**2
    elif x > 2:
        x = (x - 2)**2 + 1
    else:
        x = - x / 2      
    return x 

print(f(3))
