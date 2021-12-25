myInput = open("main.txt", "r")

numsStr = myInput.readline()
numsList = numsStr.split(',')
n = 0
while n in range(len(numsList)):
    try:
        numsList[n]=int(numsList[n])
        n += 1
    except:
        numsList.pop(n)

print(myInput)
print(numsList)

boards = myInput.read().split('\n\n')
print("FIRST BOARDS\n")
print(boards)

i = 0
while i in range(len(boards)):
    if boards[i]=='':
        boards.pop[i]
    else:
        i += 1

for i in range(len(boards)):
    boards[i]=boards[i].split('\n')

print("BOARDS SPLIT BY ROW\n")
print(boards)

for i in range(len(boards)):
    j = 0
    while j in range(len(boards[i])):
        if boards[i][j]=='':
            boards[i].pop(j)
        else:
            j += 1

for i in range(len(boards)):
    for j in range(len(boards[i])):
        boards[i][j]=boards[i][j].split(' ')

print("BOARDS SPLIT BY ROW SPLIT INTO CHARS\n")
print(boards)

for i in range(len(boards)):
    for j in range(len(boards[i])):
        k = 0
        while k in range(len(boards[i][j])):
            if boards[i][j][k]=='':
                boards[i][j].pop(k)
            else:
                k += 1

for i in range(len(boards)):
    for j in range(len(boards[i])):
        k = 0
        while k in range(len(boards[i][j])):
            try:
                boards[i][j][k]=int(boards[i][j][k])
                k += 1
            except:
                boards[i][j].pop(k)

print("COMPLETE BOARDS\n")
print(boards)

WIN = False
winningBoard = 0
numJustCalled = 0

n = 0

while WIN==False:

        for i in range(len(boards)):
            for j in range(len(boards[i])):
                for k in range(len(boards[i][j])):
                    if boards[i][j][k]==numsList[n]:
                        boards[i][j][k] = -1

        for i in range(len(boards)):
            for j in range(5):
                if (boards[i][j][0]==-1 and\
                    boards[i][j][1]==-1 and\
                    boards[i][j][2]==-1 and\
                    boards[i][j][3]==-1 and\
                    boards[i][j][4]==-1):

                    WIN = True
                    winningBoard = i
                    numJustCalled = numsList[n]

        for i in range(len(boards)):
            for j in range(5):
                if (boards[i][0][j]==-1 and\
                    boards[i][1][j]==-1 and\
                    boards[i][2][j]==-1 and\
                    boards[i][3][j]==-1 and\
                    boards[i][4][j]==-1):

                    WIN = True
                    winningBoard = i
                    numJustCalled = numsList[n]

        n += 1

def getScore(board):

    score = 0

    for j in range(5):
        for k in range(5):
            if boards[board][j][k]>0:
                score += boards[board][j][k]

    score *= numJustCalled

    return score

winningScore = getScore(winningBoard)

print("The winning board is at ", winningBoard)

print("The winning score is ", winningScore)