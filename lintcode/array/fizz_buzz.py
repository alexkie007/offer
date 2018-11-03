class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        result = [x for x in range(n)]
        for i in range(1,n+1):
            if i % 15 == 0:
                result[i] = "fizz buzz"
            elif i % 5 == 0:
                result[i] = "buzz"
            elif i % 3 == 0:
                result[i] = "fizz"

        return result

