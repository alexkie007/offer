
def maxProduct(length):
    if length < 2:
        return 0
    if length ==2:
        return 1
    if length ==3:
        return 2
    products = [0]* (length+1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    for i in range(4, length+1):
        max = 0
        for j in range(1,i//2):
            product = products[j] * products[i-j]
            if max <product:
                max = product
            products.append(max)

    return max

if __name__=="__main__":
    print(maxProduct(4))


