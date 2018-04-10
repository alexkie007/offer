def isCompare(string):
        size = len(string)
        sl,sr,st,flag =0,0,0,0
        for i in range(size):
            if string[i]=='(':
                sl+=1
                st+=1
            else:
                sr+=1
                if st==0:
                    flag +=1
                    st+=1
                else:
                    st -=1
        if sl==sr and (st==2 and flag) or (st==0 and size >2):
            print("Yes")
        else:
            print("No")

# n = int(input())
# string = []
# for i in range(n):
#     string.append(input())
#
# for i in string:
#     isCompare(i)
import math
def comdiv(num):

    s = int(math.sqrt(num))

    for i in range(2,s+1):
        if num % i ==0:

            print(int(num/i),i)
            break
        if i ==s:
            print("No")

comdiv(10)
comdiv(5)
