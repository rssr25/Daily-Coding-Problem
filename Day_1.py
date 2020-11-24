'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


def itAddsUp(numList, k):

    for i in range(0, len(numList)):
        for j in range(i+1, len(numList)):

            if numList[i] + numList[j] == k:
                return True, i, j

    return False, None, None


numList = [1, 10, 15, 100,  7, 90]
k = 101
print(itAddsUp(numList, k))
