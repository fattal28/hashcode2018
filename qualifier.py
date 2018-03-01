import random, re
fileName = "a_example.in"
inputFile = open(fileName, mode='r')
info = []
count = 1
def printArray(array):
    for subarray in array:
        print(subarray)
for line in inputFile:
    info.append(re.sub("[^\w]", " ",  line).split())
        
    count += 1

printArray(info)