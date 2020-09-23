def sumatoria_cubica(n):
    numero=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            for k in range(j,i+j+1):
                numero=numero+1
    return numero

def sumatoria_constante(n):
    a=(n*(n+1)*(2*n+1))/6
    b=(n*(n+1))/2
    return (a+b)







