@startuml 
 
 
title Up & Down Game 
 
 
 
 
start 
:get user input range; 
:get admin choose number in range¡æA; 
repeat 
:user choose number in range¡æB; 
  
if (A=B) then (yes) 
:print Correct!; 
elseif (A>B) then (yes) 
:print Up; 
elseif (A<B) then (yes) 
:print Down; 
else (Error!) 

 
endif 
:correct or up or down; 
 
 
repeat while (If you failed the answer) 
 
 
stop 

 
@enduml


 
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

