import os
import random


def generateSmall():
    size = 50
    S = []
    P = []
    m = 20

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, m)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)

    # make sure 1 to m are in the subsets
    for i in range(1,m+1):
        for j in range(random.randint(1, size)):
            S[j].append(i)

    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def generateMedium():
    size = 50
    S = []
    P = []
    m = 200

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, m)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)

    # make sure 1 to m are in the subsets
    for i in range(1,m+1):
        for j in range(random.randint(1, size)):
            S[j].append(i)
    
    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def generateLarge():
    size = 50
    S = []
    P = []
    m = 2000

    for i in range(size):
        temp = []
        subsetSize = random.randint(1, m)
        for j in range(subsetSize):
            temp.append(random.randint(1, m))
        S.append(temp)
    
    # make sure 1 to m are in the subsets
    for i in range(1,m+1):
        for j in range(random.randint(1, size)):
            S[j].append(i)

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
    with open(fileName, 'r') as f:
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

def main():
    smallData = generateSmall()
    mediumData = generateMedium()
    largeData = generateLarge()

    saveToFile(smallData, 'dataset/small.txt')
    saveToFile(mediumData, 'dataset/medium.txt')
    saveToFile(largeData, 'dataset/large.txt')

if __name__ == '__main__':
    main()