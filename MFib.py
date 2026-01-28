def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def mortalfibo(n,m):
    if n <= m:
        return fibo(n)
    else:
        return mortalfibo(n-2,m) + mortalfibo(n-3,m)

string=input("Enter both numbers with a space: ")
nos=string.split()
n=int(nos[0])
m=int(nos[1])

print(mortalfibo(n,m))
