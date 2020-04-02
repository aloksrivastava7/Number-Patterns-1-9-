'''

Enter Height : 10

*****
*
*
*
*****
    *
    *
    *
    *
*****

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == n//2 or i == n:
        print('*'*(n//2))
    elif i>=1 and i<=(n//2):
        print('*')
    elif i>=(n//2) and i<=n:
        print(' '*((n//2)-1)+'*')
