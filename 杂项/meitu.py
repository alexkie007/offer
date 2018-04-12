import sys
def num_jiami(num):
    '''
        输入num为四位数，操作，每一位加5，然后分别替换为该数除以10取余数后的结果，然后1位和4位交换，
        2位和3位交换，再合起来。
    '''
    num_list=list(str(num))
    for i in [0,1,2,3]:
        num_list.append(str((int(num_list[0])+5)%10))
        num_list.pop(0)
    num_list.reverse()
    result=''.join(num_list)
    return result
num = input()
sys.stdout.write(num_jiami(num))