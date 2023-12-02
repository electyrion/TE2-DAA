import os
import sys
import random


def generateSmall():
    print("Generating small dataset...")
    size = 20
    S = []
    P = []
    m = random.randint(1, 100)

    for i in range(size):
        temp = []
        for j in range(random.randint(1, 10)):
            temp.append(random.randint(1, m))
        S.append(temp)

    for i in range(size):
        P.append(random.randint(1, 100))
    
    return [m, S, P]

def generateMedium():
    print("Generating medium dataset...")

def generateLarge():
    print("Generating large dataset...")


if __name__ == '__main__':
    res = generateSmall()
    print(res[0])
    print(res[1])
    print(res[2])