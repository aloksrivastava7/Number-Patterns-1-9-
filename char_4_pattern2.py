'''

Enter Height : 15

      **
     * *
    *  *
   *   *
  *    *
 *     *
 * * * * * * * * *
       *
       *
       *
       *
       *
       *
       *
       *
       *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1:
        for j in range(1,(n//2)):
            print(' '*((n//2)-j)+'*'+' '*(j-1)+'*')
    elif i == 5:
         print(' *'*(3*(n//4)))
    elif i>=(n//2) and i<=n:
         print(' '*(n//2)+'*')
