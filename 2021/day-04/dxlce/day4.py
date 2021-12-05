#Honestly? It feels like a miracle I even managed to solve it

import copy
def main():

    inputs = []
    bingoBoards = []
    bingoBoard = []
    tempArr = []
    row = []

    checkRow = []
    checkColumn = []
    counter = 0
    iterator = 0
    winner = 0
    winningBoard = []
    winningNumber = 0
    lastBoard = False
    
    with open("input.txt", "r") as file:

        inputs = file.readlines()[0].strip().split(",")

        for i in range(0, len(inputs)):
            inputs[i] = int(inputs[i])

    with open("input.txt", "r") as file:
        moreLines = file.readlines()

        for thing in moreLines:
            if counter == 0:
                counter = counter + 1
                continue
            
            #Start of new bingo card
            if (thing == "\n"):
                if (iterator == 0):
                    iterator = iterator + 1
                    continue
            
            if (iterator != 0):
                temp = thing.split(" ")
                for element in temp:
                    if (element == ""):
                        continue
                        
                    if (element == "\n"):
                        continue

                    element = int(element.strip())
                    bingoBoard.append([element, False])

                iterator = iterator + 1

                if (iterator == 6):
                    bingoBoards.append(copy.deepcopy(bingoBoard))
                    bingoBoard = []

                    iterator = 0

    counter = 0
    for input in inputs:
        for board in bingoBoards:
            for elem in board:
                if (elem[0] == input):
                    elem[1] = True

        for board in bingoBoards:
            for elem in board:
                counter = counter + 1
                if (elem[1] == True):
                    winner = winner + 1
                if (counter == 5):
                    if (winner == 5):
                        winningBoard = board
                        winningNumber = input
                        break
                    counter = 0
                    winner = 0
            
            if (winner == 5):
                break
                
        if (winner == 5):
            break
            
        counter = 0
        winner = 0
        for board in bingoBoards:
            for i in range(0, 5, 1):
                for j in range(i, 20 + i + 1, 5):

                    counter = counter + 1
                    if (board[j][1] == True):
                        winner = winner + 1
                    if (counter == 5):
                        if (winner == 5):
                            winningBoard = board
                            winningNumber = input
                            break
                        counter = 0
                        winner = 0

                if (winner == 5):
                    break
            if (winner == 5):
                break
                
        if (winner == 5):
            break
        
    sum = 0
    for elem in winningBoard:
        if (elem[1] == False):
            sum = sum + elem[0]
    print(sum*winningNumber)
    
    
    with open("input.txt", "r") as file:

        inputs = file.readlines()[0].strip().split(",")

        for i in range(0, len(inputs)):
            inputs[i] = int(inputs[i])

    with open("input.txt", "r") as file:
        moreLines = file.readlines()

        for thing in moreLines:
            if counter == 0:
                counter = counter + 1
                continue
            
            #Start of new bingo card
            if (thing == "\n"):
                if (iterator == 0):
                    iterator = iterator + 1
                    continue
            
            if (iterator != 0):
                temp = thing.split(" ")
                for element in temp:
                    if (element == ""):
                        continue
                        
                    if (element == "\n"):
                        continue

                    element = int(element.strip())
                    bingoBoard.append([element, False])

                iterator = iterator + 1

                if (iterator == 6):
                    bingoBoards.append(copy.deepcopy(bingoBoard))
                    bingoBoard = []

                    iterator = 0

    counter = 0
    for input in inputs:
        for board in bingoBoards:
            for elem in board:
                if (elem[0] == input):
                    elem[1] = True

        for board in bingoBoards:
            for elem in board:
                counter = counter + 1
                if (elem[1] == True):
                    winner = winner + 1
                if (counter == 5):
                    if (winner == 5):
                        if (len(bingoBoards) == 1):
                            lastBoard = True
                            print(board)
                            winningBoard = board
                            winningNumber = input
                            break
                        bingoBoards.remove(board)
                        counter = 0
                        winner = 0
                        break
                    counter = 0
                    winner = 0
            
            if (winner == 5):
                break
                
        if (winner == 5):
            if (lastBoard):
                break
            
        counter = 0
        winner = 0
        for board in bingoBoards:
            for i in range(0, 5, 1):
                for j in range(i, 20 + i + 1, 5):

                    counter = counter + 1
                    if (board[j][1] == True):
                        winner = winner + 1
                    if (counter == 5):
                        if (winner == 5):
                            if (len(bingoBoards) == 1):
                                lastBoard = True
                                winningBoard = board
                                winningNumber = input
                                break
                            bingoBoards.remove(board)
                            counter = 0
                            winner = 0
                            break
                        counter = 0
                        winner = 0

                if (winner == 5):
                    break
            if (winner == 5):
                break
                
        if (winner == 5):
            if (lastBoard):
                break
        
    sum = 0
    print(winningBoard)
    
    for elem in winningBoard:
        if (elem[1] == False):
            sum = sum + elem[0]
    print(sum*winningNumber)

        


if __name__ == "__main__":
    main()
