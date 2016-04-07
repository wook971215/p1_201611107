
"""
@author John
@since 160406
"""


def playUpAndDownGame():
	print "Let's Play Up & Down Game"
	print "-------------------------"
	print "First!"
	print "Input Range begin_end"

	begin=raw_input("Input Begin:")
	end=raw_input("Input End:")

	begin=int(begin)
	end=int(end)
	cor=0
	import random
	num=random.randrange(begin,end)

	print "-------------------------"
	print "Sceond!"

	print "Input that you're thinking number in range!"


	while(num!=cor):	

		cor=raw_input("Input Your Thinking Number:")
		cor=int(cor)
		if (num==cor):
			print "Congratulation Correct!"
		elif (num>cor):
			print "UP Please"
		elif (num<cor):
			print "Down Please"
		else :
			print "Please Input Number In Range !"

	print "-------------------------"
	print "Finish. Thank you for enjoy the game!"
	
	raw_input()

def main():
    playUpAndDownGame()


if __name__=="__main__":
    main()