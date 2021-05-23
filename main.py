from Omok import *
import random
import os

width = 15
height = 15
streak = 5
firstPlayer = 0

debugPrint = 0

for turn in range(1):
        print(turn)
        for z in range(225):
                history = []

                b = board(width, height, streak, firstPlayer)
                while len(b.avaiableMoves) > 0:
                        
                        
                        if(1 == 1):
                        
                                rng = random.randint(0,len(b.avaiableMoves)-1)

                                x = ord(b.avaiableMoves[rng][0])-65
                                y = int(b.avaiableMoves[rng][1:3])
                                b.board[x][y] = firstPlayer

                        while b.checkComp(x,y) == 10000:
                                #HOWEVER, there is an exception to this. When you or your opponent is forced to place a piece there or lose
                                #(i.e. when a row of 4 is formed, and you have to place it there to prevent the opponent from winning),
                                #you will be allowed to place your piece in the double-3 spot. In other words, if they allow you to do so, you generally win.
                                
                                if firstPlayer == 0:
                                        b.board[x][y] = 1
                                else:
                                        b.board[x][y] = 0
                                if b.checkComp(x,y) == streak:   
                                        #print("streak")
                                        b.board[x][y] = firstPlayer
                                        break
                                else:
                                        b.board[x][y] = -1
                                        rng = random.randint(0,len(b.avaiableMoves)-1)

                                        x = ord(b.avaiableMoves[rng][0])-65
                                        y = int(b.avaiableMoves[rng][1:3])
                                        b.board[x][y] = firstPlayer
                          
                        if(1 == 555):
                                if len(b.avaiableMoves)%2 == 0:     
                                        b.mushroomPiece.append(b.avaiableMoves[rng])
                                        b.board[x][y]= firstPlayer
                                else:
                                        b.slimePiece.append(b.avaiableMoves[rng])
                                        b.board[x][y] = firstPlayer

                        #print(b.avaiableMoves[rng],x, y, x*width+y)
                        history.append(x*width+y)
                        del b.avaiableMoves[rng]
                        
                        if b.checkComp(x,y) == streak:        
                                #print("last piece placed at:", x,y)
                                break;
                                
                        if firstPlayer == 0:
                                firstPlayer = 1
                        else:
                                firstPlayer = 0

        if debugPrint == 1:                                
                print("last piece placed at:", x,y)			
                b.printBoard()
                print(history)
        
        f=open('games.csv','a')
        f.write((str(firstPlayer) +", " +str(history).strip("[] ")+'\n').replace(" ", ""))
        f.close()

#b.printBoard()
#print(history)




##for i in range(len(b.board)):
##    print(b.board[i])
##
####print(b.mushroomPiece)
####print(b.slimePiece)
