class board(object):
		SLIME = 1
		MUSHROOM = 0
		COMPLETE = 0
		def __init__(self, height, width, streak, firstPlayer):

				self.height = height
				self.width = width
				self.gameOver = self.COMPLETE
				self.turn = firstPlayer
				
				self.STREAK = streak

				self.slimePiece = []
				self.mushroomPiece = []

				self.board = []
				#self.newBoard = [][]
				for i in range(height):
						self.board.append([-1]*width)
				
				self.avaiableMoves = []
				for x in range(width):
						for y in range(height):
								self.avaiableMoves.append(chr(x+65)+str(y))
								#self.coord.append(str(x)+str(y))

		def printBoard(self):
				count = 0
				for i in range(self.width):
					print(i, " ", end ="") 
				print("\n")
				for a in self.board:
					for b in a:
						if b == -1:
							print(".  ", end='')
						else:
							print(b, " ", end='')
					print('|',count ,'\n')
					count = count+1
				print("__________________________________")



		def getX(pog):
				return ord(pog[0])-65

		def getX(pog):
				return int(pog[1:3])
		
		def getAdj(self, x1, y1):
			dir = [[-1,-1,],[-1,0,],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
			abd = []
			
			if(self.board[x1][y1] != -1):
				for i in range(len(dir)):
					x = x1+dir[i][0]		# coord of adj x
					y = y1+dir[i][1]		# coord of adj y

					if(x < 0 or y < 0 or x > self.height-1 or y > self.width-1):
						continue 

					z = self.board[x][y]
					if(z != -1 and z == self.board[x1][y1] and (x*self.width+y) >= 0):
						abd.append(x*self.width + y)
			return abd

		def intToXY(self, intC):
			return [int(intC/len(self.board)), intC%len(self.board)]

		def XYToint(self, xy):
			return xy[0]*len(self.board) + xy[1]

		def availableMoves(self):	  
				return self.avaiableMoves

		def pop(self):
				self.avaiableMoves = self.avaiableMoves[:-1]

		def checkComp(self, x,y):
			test = 0
			
			origin = self.XYToint([x,y])
			pointer = origin
			
			#print(self.getAdj(x,y))
			adjPiece = self.getAdj(x,y)
			
			#print("in here", test, adjPiece, x,y)
			#print([(number-origin) for number in adjPiece])
			adjPiece = list(dict.fromkeys([abs(number-origin) for number in adjPiece]))			
			#print(test, adjPiece)
			#print("Adj Pieces: ", adjPiece)
			
			count = 1
			
			for dir in adjPiece:
				a = self.intToXY(pointer)
				c = d = 0		# place holder to test side bounds
				count = 1
				for i in range(2):
					
					b = self.intToXY(pointer + dir*((-1)**i))	#coordinate of next piece
					#print(b[0],b[1])
					while(pointer < self.width*self.height and \
					pointer >= 0 and \
					(b[0] < self.width and b[0] >= 0 and b[1] < self.width and b[1] >= 0)and \
					(c < 2 and d < 2)) and\
					(self.board[a[0]][a[1]] == self.board[b[0]][b[1]]):		# bounds checking
						a = self.intToXY(pointer)		#coordinate of current piece
						b = self.intToXY(pointer + dir*((-1)**i))	#coordinate of next piece
						c = abs(b[0]-a[0])				#x-distance between the two pieces
						d = abs(b[1]-a[1])				#y-distance between the two pieces
						
												
						if(pointer != origin):
							count = count + 1
							
						if count > self.STREAK:
							return count
						pointer = pointer + dir*((-1)**i)
						
					c = d = 0
					pointer = origin
				if count == self.STREAK:
					#print("you win ", count, self.STREAK)
					return count;
				if count == 3:
					test = test +1
					#print("3 in a row", test)
			if(test == 2):
				#print("double 3's at x:", x, "y:" ,y, "player: ", self.turn)
				return 10000
				
			return count
				
				
				
				
				
				
				
				
				
				
				
		# adjacent pieces that are the same and the current piece
		def checkCompletion(self, adjPiece, cur):
			if(self.avaiableMoves == 0):
				return true;
			origin = cur
			#print(adjPiece, self.intToXY(cur))
			
			## abs the dif and remove duplicates
			adjPiece = list(dict.fromkeys([abs(number-cur) for number in adjPiece]))
			
			#i is the dif
			for i in adjPiece:
				count = 0
				cur = origin 
				
				xy = self.intToXY(i)
				xycur = self.intToXY(cur)
				
				for j in range(2):
				##while inside the board and is equal
					
					while cur > -1 and cur < self.width*self.height and self.board[xycur[0]][xycur[1]] == self.board[xy[0]][xy[1]]:
						
						## going past the edge
						pow = -1**j
						x1 = xycur[1] + self.intToXY(i)[1] 
						x2 = xycur[0] + self.intToXY(i)[0]
						
						# if the next is out of bounds
						if(x1 > self.width-1 or x2 > self.height-1):
							break
							
						## 6+ is not win
						if(count > self.STREAK):
							print("too long")
							break
						
						xy = xycur
						if j == 0:
							cur = cur+i
						if j == 1:
							cur = cur-i
						xycur  = self.intToXY(cur)
						
						count = count+1
						
					xy = self.intToXY(i)
					cur = origin
					xycur = self.intToXY(cur-i)
				if count == self.STREAK:
						xycur = self.intToXY(cur)
						print("you win", count, xycur[0], xycur[1])
						return True
				#print("no win", count, self.STREAK)
			return False
			
		def gameCompleted():
				return true
				
		
