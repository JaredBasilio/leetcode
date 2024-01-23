def sumOfTwo(a, b):
    arr1 = convertToList(a)
    arr2 = convertToList(b)
    _sum = []
    carry = 0
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        _sum.append(arr1[i] ^ arr2[j] ^ carry)
        carry = (arr1[i] & arr2[j]) | (arr1[i] & carry) | (arr2[j] & carry)
        i += 1
        j += 1
    while i < len(arr1):
        _sum.append(arr1[i] ^ carry)
        carry = arr1[i] & carry
        i += 1
    while j < len(arr2):
        _sum.append(arr2[i] ^ carry)
        carry = arr2[j] & carry
        j += 1
    if carry:
        _sum.append(carry)
    return convertToBinary(_sum)

def convertToList(num):
    res = []
    while num:
        res.append(num & 1)
        num >>= 1
    return res

def convertToBinary(_list):
    res = 0
    for i in range(len(_list) - 1, -1, -1):
        res = res | (_list[i] & 1)
        res <<= 1
    return res >> 1

a = 1
b = 2
print("Input:", a, b)
print("Expected", 3)
print("Received", sumOfTwo(a,b))

a = 2
b = 3
print("Input:", a, b)
print("Expected", 5)
print("Received", sumOfTwo(a,b))

# add(a ^ b, (a & b) << 1)
# (a & b) is the front and we move the 1 
# then we ad a ^ b for the remaining