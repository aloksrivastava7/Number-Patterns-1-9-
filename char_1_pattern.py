'''

Enter Height : 15

     **
    * *
   *  *
  *   *
 *    *
*     *
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
***************

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == n:
        print('*'*n)
    elif i == 1:
        for j in range(1,(n//2)):
            print(' '*((n//2)-j-1)+'*'+' '*(j-1)+'*')
    else :
        print(' '*((n//2)-1)+'*')
