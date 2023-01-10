score = 20
highscore = 15

if score > highscore:
	highscore = score
	print("You beat your highscore!")
	print("New Highscore: " + str(highscore))
else:
	print("You didn't beat your highscore, Better luck next time!")
	print("Highscore: " + str(highscore))
	print("Score: " + str(score))