'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new 
array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''


def mulArray(data):
    ansArray = []
    

    for i in range(0, len(data)):
        result = 1
        for j in range(0, len(data)):
            if j == i:
                continue
            else:
                result = result * data[j]

        ansArray.append(result)
    
    return ansArray

            


data = [1, 2, 3, 4, 5]
print(mulArray(data))