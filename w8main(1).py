﻿def charCount():
	d=dict()
	word=raw_input('input word :')
    
	for c in word:
		if c not in d:
			d[c]=1
		else:
			d[c]=d[c]+1
    
	print d

def lab8():
	charCount()

def main():
	lab8()

if __name__=="__main__":
	main()
	raw_input()