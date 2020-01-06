import random
import sys
poems = open("lear.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n", " ").replace('"', '').split(' ')

index = 1
chain = {}
count = 30

for word in poems[index:]:
	key = poems[index - 1]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

first_word = 'There'
poem = first_word.capitalize()

while len(poem.split(' ')) < count:
	second_word = random.choice(chain[first_word])
	first_word = second_word
	poem += ' ' + second_word
	if len(poem.split(' ')) == count - 1:
		if not poem[len(poem) - 1] == '.':
			end = False
			while not end:
				end_word = random.choice(chain[first_word])
				for word in chain[first_word]:
					if word[len(word) - 1] == '.':
						end_word = word
						end = True
				second_word = end_word
				first_word = second_word
				poem += ' ' + second_word
				

print(poem)