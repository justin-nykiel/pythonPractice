#1
def sum_to(n):
    numsArr = []
    for num in range(n+1):
        numsArr.append(num)
    return sum(numsArr)
​
print(sum_to(4))
print(' ')
​
#2
def largest(arr):
    arr.sort()
    return arr.pop()
​
print(largest([10, 4, 2, 231, 91, 54]))
print(' ')
​
#3
#string method
# def occurances(string1, string2):
#     return string1.count(string2)
​
#longer version
def occurances(string1, string2):
    count = 0
    length = len(string2)
    while (string2 in string1):
        index = string1.index(string2)
        string1 = list(string1)
        del string1[index: (index + length)]
        count += 1
        string1 = ''.join(string1)
    return count
​
print(occurances('fleeep floop', 'e'))
print(occurances('fleep fleep', 'ee'))
print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee')) # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0
print(' ')
​
#4
def product(*argv):
    product = 1
    for arg in argv:
        product *= arg
    return product
​
print(product(4, 5, 7, 8))