'''

Enter Height : 10

 * * * * *
         *
         *
         *
         *
        *
       *
      *
     *
    *
   *
  *
 *
*
**********

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1:
        print(' *'*(n//2))
    elif i == n:
        print('*'*n)
    elif i>=1 and i<=(n//2):
        print(' '*(n-1)+'*')
    if i == (3*(n//4)):
        for j in range(1,n):
            print(' '*(n-j-1)+'*')
            
        
