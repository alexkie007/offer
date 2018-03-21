def print_max_n(n):
    for i in range(10**n):
        print(i)

def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print('%c' % number[i], end='')
    print('')

def prin1ToMax(number, length, index):
    if index == length-1:
        print(''.join(number))
        return
    for i in range(10):
        number[index+1] =str(i)
        prin1ToMax(number,length,index+1)

def print_man(n):
    if n<=0:return

    number = ['0'] *n
    for i in range(10):
        number[0]=str(i)
        prin1ToMax(number, n ,0)


# print(print_max_n(3))
print(print_man(3))