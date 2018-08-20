# Tugas Karya untuk SPARTA HMIF 2017
# Nama        : Leonardo
# NIM TPB     : 16517182
# NIM Jurusan : 13517048
# Deskripsi   : Game sederhana tentang "Guess the Point/Spot"
from random import randint

def rapiin(board):
	for row in board:
		print (" ".join(row))

def randrow(board):
	return randint(0, len(board)-1)

def randcol(board):
	return randint(0, len(board)-1)

#main Game
def mbleh():
	print ("WELCOME TO THE ZONK GAME" + "\n" + "\n")
	print ("Choose Mode!" + "\n")
	print ("1. PLAYER 1 VS BOT")
	print ("2. PLAYER 1 VS PLAYER 2" + "\n")

	pil = int(input())
	while ((pil < 1) or (pil > 2)) :
		pil = int(input("Must be 1 or 2! "))

	print ("Choose Board Size !")
	print ("Just input N for NxN board size" + "\n")
	print ("3. 3x3")
	print ("5. 5x5")
	print ("." + "\n" + "." + "\n" + "." + "\n")
	bny = int(input())
	while (bny < 2):
		bny = int(input("Must be at least 2x2 grid! "))

	if (pil == 1):
		board_pl1 = []
		board_bot = []

		for i in range(bny):
			board_pl1.append(["_"] * bny)

		for i in range(bny):
			board_bot.append(["_"] * bny)

		print ("PLAYER 1 's Board")
		rapiin(board_pl1)
		print ("\n" + "BOT 's Board")
		rapiin(board_bot)

		zonkpl1_row = randrow(board_pl1)
		zonkpl1_col = randcol(board_pl1)

		zonkbot_row = randrow(board_bot)
		zonkbot_col = randcol(board_bot)

		turn = 0
		done = False
		#mulai game (lawan bot)
		while (not(done)) :
			turn += 1;
			print ("\n")
			print ("Turn",turn)
			#giliran p1
			print ("PLAYER 1 's Turn")
			p1row = int(input("Guess ROW : "))
			p1row -= 1
			p1col = int(input("Guess COL : "))
			p1col -= 1

			if ((p1row == zonkbot_row) and (p1col == zonkbot_col)) :
				print ("PLAYER 1 WIN !!!")
				board_bot[p1row][p1col] = "O"
				done = True
			else :
				if ((p1row < 0) or (p1row > bny-1) or (p1col <0) or (p1col > bny-1)) :
					print ("Where R U trying?")
				elif (board_bot[p1row][p1col] == "X") :
					print ("U tried there already")
				else :
					print ("PLAYER 1 missed")
					board_bot[p1row][p1col] = "X"

			print ("PLAYER 1 's Board")
			rapiin(board_pl1)
			print ("\n")
			print ("BOT 's Board")
			rapiin(board_bot)

			if (not(done)):
				#giliran bot
				print ("\n" + "BOT 's Turn")
				botrow = randint(0, len(board_pl1)-1)
				botcol = randint(0, len(board_pl1)-1)
				while (board_pl1[botrow][botcol] == "X"):
					botrow = randint(0, len(board_pl1)-1)
					botcol = randint(0, len(board_pl1)-1)
				#endwhile

				if ((botrow == zonkpl1_row) and (botcol == zonkpl1_col)) :
					print ("BOT WIN !!!")
					board_pl1[botrow][botcol] = "O"
					done = True
				else :
					print ("BOT missed")
					board_pl1[botrow][botcol] = "X"

				print ("PLAYER 1 's Board")
				rapiin(board_pl1)
				print ("\n")
				print ("BOT 's Board")
				rapiin(board_bot)
			#endif
		#endwhile

	elif (pil == 2):
		board_pl1 = []
		board_pl2 = []

		for i in range(bny):
			board_pl1.append(["_"] * bny)

		for i in range(bny):
			board_pl2.append(["_"] * bny)

		print ("PLAYER 1 's Board")
		rapiin(board_pl1)
		print ("\n" + "PLAYER 2 's Board")
		rapiin(board_pl2)

		zonkpl1_row = randrow(board_pl1)
		zonkpl1_col = randcol(board_pl1)

		zonkpl2_row = randrow(board_pl2)
		zonkpl2_col = randcol(board_pl2)

		turn = 0
		done = False
		#mulai game (VS mode)
		while(not(done)):
			turn += 1
			print ("\n")
			print ("Turn",turn)
			#giliran p1
			print ("PLAYER 1 's Turn")
			p1row = int(input("Guess ROW : "))
			p1row -= 1
			p1col = int(input("Guess COL : "))
			p1col -= 1

			if ((p1row == zonkpl2_row) and (p1col == zonkpl2_col)) :
				print ("PLAYER 1 WIN !!!")
				board_pl2[p1row][p1col] = "O"
				done = True
			else :
				if ((p1row < 0) or (p1row > bny-1) or (p1col <0) or (p1col > bny-1)) :
					print ("Where R U trying?")
				elif (board_pl2[p1row][p1col] == "X") :
					print ("U tried there already")
				else :
					print ("PLAYER 1 missed")
					board_pl2[p1row][p1col] = "X"

			print ("PLAYER 1 's Board")
			rapiin(board_pl1)
			print ("\n")
			print ("PLAYER 2 's Board")
			rapiin(board_pl2)

			if (not(done)):
				#giliran p2
				print ("\n" + "PLAYER 2 's Turn")
				p2row = int(input("Guess ROW : "))
				p2row -= 1
				p2col = int(input("Guess COL : "))
				p2col -= 1

				if ((p2row == zonkpl1_row) and (p2col == zonkpl1_col)) :
					print ("PLAYER 2 WIN !!!")
					board_pl1[p2row][p2col] = "O"
					done = True
				else :
					if ((p2row < 0) or (p2row > bny-1) or (p2col < 0) or (p2col > bny-1)) :
						print ("Where R U trying?")
					elif (board_pl1[p2row][p2col] == "X") :
						print ("U tried there already")
					else :
						print ("PLAYER 2 missed")
						board_pl1[p2row][p2col] = "X"

				print ("PLAYER 1 's Board")
				rapiin(board_pl1)
				print ("\n")
				print ("PLAYER 2 's Board")
				rapiin(board_pl2)
			#endif
		#endwhile
	#endif
	re = input("Play Again? (Y for Yes and N for No) ")
	re = re.upper()
	if (re == 'Y'):
		mbleh()
	#endif
#endprocedure

mbleh()
