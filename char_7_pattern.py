'''

Enter Height : 15

***************
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
*

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1:
        print('*'*(n))
    elif i == n:
        for j in range(1,n):
            print(' '*(n-j-1)+'*')
