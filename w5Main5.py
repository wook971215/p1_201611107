score=raw_input("get user input score(0~100):")
score=float(score)
print "My number is: %s"%score
def convertScoreToGrade(score):
	if (90<score<=100):
		grade='A'
	elif (80<score<=90):
		grade='B'
	elif (70<score<=80):
		grade='C'
	elif (60<score<=70):
		grade='D'
	else:
		grade='F'
	return grade
        
convertScoreToGrade(score)

result=convertScoreToGrade(score)

print "My grade is: %s"%result

raw_input("If you want to exit this program, click Enter")