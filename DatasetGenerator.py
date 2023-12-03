import os
import io
import sys
import random


def generateSmall():
    size = 20
    S = []
    P = []
    m = random.randint(1, 100)

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, 5)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)

    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def generateMedium():
    size = 200
    S = []
    P = []
    m = random.randint(1, 100)

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, 10)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)

    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def generateLarge():
    size = 2000
    S = []
    P = []
    m = random.randint(1, 100)

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, 100)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)

    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def saveToFile(arr, fileName):
    with open(fileName, 'w') as f:
        m = arr[0]
        S = arr[1]
        P = arr[2]

        f.write(str(m) + '\n')
        for i in range(len(S)):
            f.write('[')
            for j in range(len(S[i])):
                f.write(str(S[i][j]) + ', ')
            # delete the last space and comma
            f.seek(f.tell() - 2, os.SEEK_SET)
            f.write('] ')
        # delete the last space
        f.seek(f.tell() - 1, os.SEEK_SET)


        f.write('\n')
        f.write('[')
        for i in range(len(P)):
            f.write(str(P[i]) + ', ')
        # delete the last space and comma
        f.seek(f.tell() - 2, os.SEEK_SET)
        f.write(']')
        
        f.write('\n')

def readFromFile(fileName):
    with open('test.txt', 'r') as f:
        m = int(f.readline())
        S = []
        P = []
        temp = f.readline()
        for i in range(len(temp)):
            if temp[i] == '[':
                subset = []
                j = i + 1
                tempStr = ''
                while j < len(temp) and temp[j] != ']':
                    if temp[j] != ',' and temp[j] != ' ': 
                        tempStr += temp[j]
                    elif temp[j] == ',' or temp[j] == ']':
                        if tempStr != '':
                            subset.append(int(tempStr))
                        tempStr = ''
                    j += 1
                subset.append(int(tempStr))
                S.append(subset)
        temp = f.readline()
        for i in range(len(temp)):
            if temp[i] == '[':
                j = i + 1
                tempStr = ''
                while j < len(temp) and temp[j] != ']':
                    if temp[j] != ',' and temp[j] != ' ': 
                        tempStr += temp[j]
                    elif temp[j] == ',' or temp[j] == ']':
                        if tempStr != '':
                            P.append(int(tempStr))
                        tempStr = ''
                    j += 1
                P.append(int(tempStr))
    f.close()
    return [m, S, P]

if __name__ == '__main__':
    res = readFromFile('test.txt')
    print(res[0])
    print(res[1])
    print(res[2])
    
    # res = generateSmall()
    # res = generateMedium()
    # res = generateLarge()
    # print(res[0])
    # print(res[1])
    # print(res[2])
    # saveToFile(res, 'test.txt')
    # print(len(res[1]))
    # print(len(res[2]))