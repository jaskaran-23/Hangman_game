#i am gonna implement a python program to implement hangman game.
import random
def random_word():
	with open("words.txt","r")as f:
		words1=f.read().split(' ')
		return random.choice(words1)
actual_word=random_word()
for i in actual_word:
	print('*')
l=len(actual_word)
print("WELCOME TO HANGMAN")
print("word has ",l,"letters")
#now we gonna check if entered character is a matching character

def check_word(actual_word,my_guess,guess1):
	status=''
	matches=0
	for letter in actual_word:
		if letter in my_guess:
			status+=letter
		else:
			status+='*'
		if letter==guess1:
			matches+=1
	if matches>=1:
		print(matches,guess1)
	return status
def game():
	guess=0
	guessed=False
	my_guess=[]
	turns=len(actual_word)+1
	turns1=turns
	print("Total number of turns ",turns1)
	while guess<turns1:
		guess1=input("enter your guess ")
		turns-=1
		print("turns left ",turns)
		if guess1 in my_guess:
			print("already guessed ")
		elif len(guess1)==1:
			my_guess.append(guess1)
			result=check_word(actual_word,my_guess,guess1)
			if result==actual_word:
				guessed=True
				print("you won")
				print(actual_word)
				break
			else:
				print(result)
		else:
			print("invalid entry")
		guess+=1
	if guessed==False:
		print(actual_word)
		print("better luck next time")
game()
