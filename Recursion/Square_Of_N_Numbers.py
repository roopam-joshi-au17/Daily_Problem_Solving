'''
Square of N Numbers
'''
def square(n):
    if n>0:
        k=n**2
        print(k)
        square(n-1)
n=int(input())
square(n)